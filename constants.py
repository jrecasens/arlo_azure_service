import socket
import os
from azure.storage.blob import BlobServiceClient, __version__
import sqlalchemy as db
import urllib
from dotenv import load_dotenv
import logging

# Set Main Logger
logging.basicConfig()
__logger_main = logging.getLogger("main")
__logger_main.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('log_history.log') # creates handler for the log file
handler.setFormatter(formatter)
__logger_main.addHandler(handler) # adds handler to logger

# Turn off SQLAlchemy logging
logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

#########################################
# Initialize
#########################################

# Get machine name (works in Windows and Linux)
host_name = socket.gethostname()
__logger_main.info("Using hostmachine:" + host_name)
print(222)

# Get environment variables
load_dotenv()
arlo_username = os.getenv('ARLO_USERNAME')
arlo_password = os.getenv('ARLO_PASSWORD')

arlo_imap_username = os.getenv('ARLO_IMAP_USERNAME')
arlo_imap_password = os.getenv('ARLO_IMAP_PASSWORD')

azure_connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

#########################################
# Azure Blob Storage
#########################################

try:
    __logger_main.info("Using Azure Blob Storage v" + __version__)
    # Quick start code goes here
    azure_container_name = 'publiccontainer'
    # Create the BlobServiceClient object which will be used to create a container client
    azure_blob_service_client = BlobServiceClient.from_connection_string(azure_connect_str)

except Exception as ex:
    __logger_main.error("Exception:" + ex)

#########################################
# Azure SQL Server
#########################################

azure_sql_server = os.getenv('AZURE_SQL_SERVER')
azure_sql_db_name = os.getenv('AZURE_SQL_DB_NAME')
azure_sql_db_user = os.getenv('AZURE_SQL_DB_USER')
azure_sql_db_pwd = os.getenv('AZURE_SQL_DB_PWD')
azure_sql_driver = os.getenv('AZURE_SQL_DRIVER')

params = urllib.parse.quote_plus(r'Driver=' + azure_sql_driver + ';'
                                r'Server=' + azure_sql_server + ';'
                                r'Database=' + azure_sql_db_name + ';'
                                r'Uid=' + azure_sql_db_user + ';'
                                r'Pwd=' + azure_sql_db_pwd + ';'
                                r'Encrypt=yes;'
                                r'TrustServerCertificate=yes;'
                                r'Connection Timeout=30;')

conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine = db.create_engine(conn_str, echo=False)

__logger_main.info("Succesful connection to Azure SQL Server")

metadata = db.MetaData()
connection = engine.connect()
camera_detection_history = db.Table("camera_detection_history", metadata, autoload_with=engine, extend_existing=True)

__logger_main.info("Succesful loading of DB schema")