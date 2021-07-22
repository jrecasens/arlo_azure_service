from PIL import Image
import time
import io
import string
import random
import constants
import os

# code to trap when attributes change
def baby_attribute_changed(device, attr, value):
    print('attribute_changed', time.strftime("%H:%M:%S"), device.name + ':' + attr + ':' + str(value)[:80])
    if attr == "presignedLastImageData":

        # ////// SAVE TO BLOB STORAGE //////
        img = Image.open(io.BytesIO(value))
        # img.show()
        local_path = "./tmp"
        if not os.path.exists('tmp'):
            os.makedirs('tmp')

        random_license = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        local_file_name = str(random_license) + ".jpg"
        upload_file_path = local_path + "/" + local_file_name

        print("saving image....")
        img.save(upload_file_path)

        # Create a blob client using the local file name as the name for the blob
        azure_blob_client = constants.azure_blob_service_client.get_blob_client(container=constants.azure_container_name,
                                                                                blob=local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            azure_blob_client.upload_blob(data)
            url = azure_blob_client.url

        os.remove(upload_file_path)

        # ////// SAVE TO SQL SERVER //////
        print("\nSaving record to Azure SQL Server DB:\n\t" + url)

        stmt = constants.db.insert(constants.camera_detection_history).values(
            device_source_id='sample_device',
            vehicle_license_plate=random_license,
            vehicle_direction='q',
            vehicle_other='q',
            image_url=url
        )
        constants.connection.execute(stmt)
