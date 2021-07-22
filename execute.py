import constants
import helper_functions
import logging
import sys
import pyaarlo
from flask import Flask

app = Flask(__name__)

__logger_main = logging.getLogger("main")

logger_flask = logging.getLogger('werkzeug') # grabs underlying WSGI logger
logger_arlo = logging.getLogger('pyaarlo') # grabs underlying ARLO logger
logger_flask.addHandler(constants.handler) # adds handler to the werkzeug WSGI logger
logger_arlo.addHandler(constants.handler) # adds handler to the werkzeug ARLO logger

@app.route("/")
def execute():

    # log in
    arlo = pyaarlo.PyArlo(username=constants.arlo_username,
                            password=constants.arlo_password,
                            #tfa_type='SMS', tfa_source='console',
                            tfa_type='email', tfa_source='imap',
                            tfa_host='imap.gmail.com',
                            tfa_username=constants.arlo_imap_username,
                            tfa_password=constants.arlo_imap_password,
                            synchronous_mode=False,
                            save_session=True,
                            save_state=False,
                            dump=True,
                            storage_dir='aarlo',
                            verbose_debug=True
                            # ,refresh_devices_every=3,
                            # reconnect_every=90,
                            # request_timeout=120
                            )

    if not arlo.is_connected:
        __logger_main.error("Arlo failed to login({})".format(arlo._last_error))
        sys.exit(-1)

    __logger_main.info("Succesful connection to Arlo Event Stream!!!")
    camera = arlo.cameras[1]
    __logger_main.info("Using camera: name={},device_id={},state={}".format(camera.name,camera.device_id,camera.state))
    camera.add_attr_callback('*', helper_functions.baby_attribute_changed)

    return "App running on Azure App Service for Linux"