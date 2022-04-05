<p align="center">
<br>
<img src="img/arlo.jpg" width= "10%" height= "10%" alt="Arlo logo">
<img src="img/azure.JPG" width= "5%" height= "5%" alt="Azure logo">
<br>
<strong> Arlo Camera Flask App on Azure </strong>
</p>

Simple Flask Application in <a href="https://azure.microsoft.com/en-us/services/app-service/">Azure App Service</a> to handle Arlo Camera event storage in Azure SQL Server and Azure Blog Storage.

## Prerequisites
The project code utilizes the following library:
* [Python](https://www.python.org/) v3.8.6
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) v2.0.1
* [pyaarlo](https://github.com/twrecked/pyaarlo) v0.8.0a6
* [azure.storage.blob](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python) v12.8.1
* [pyodbc](https://pypi.org/project/pyodbc/) v4.0.31

## Code
This project is based on

https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-app-service-on-linux-01


Deploy Python apps to Azure App Service on Linux from Visual Studio Code


## Testing

Before deployment to Azure App Service, creating a virtual enviroment is recommended for a succesful local execution test:

### Create Enviroment (named .venv)
    python -m venv .venv

### Activate enviroment
    .venv\scripts\activate

### Install dependencies in .venv
    pip install -r requirements.txt

### Run Flask App
    cd C:/Github/arlo_azure_service
    $env:FLASK_APP = "execute:app"

### Deactivate and Delete (optional)
    deactivate
    rm -r .venv
