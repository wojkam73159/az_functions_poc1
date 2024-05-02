import azure.functions as func
from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

import logging
import requests

from azure.identity.aio import DefaultAzureCredential
def get_key_vault_secret(vault_url: str, secret_name: str) -> str:
    credential: DefaultAzureCredential = DefaultAzureCredential()
    secret_client: SecretClient = SecretClient(vault_url=vault_url, credential=credential)
    return secret_client.get_secret(secret_name).value

def create_blob_service_client(account_url: str, storage_account_key: str) -> BlobServiceClient:
    return BlobServiceClient(account_url=account_url, credential=storage_account_key)

def get_or_create_blob_container(client: BlobServiceClient, container_name: str) -> ContainerClient:
    container_client: ContainerClient = client.get_container_client(container_name)
    
    if not container_client.exists():
        container_client.create_container()

    return container_client

def download_data_from_api(api_url: str) -> bytes:
    received_data = requests.get(api_url)
    received_data.raise_for_status()
    return received_data.content

def upload_blob(container_client: ContainerClient, blob_name: str, data: bytes) -> None:
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

app = func.FunctionApp()
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    try:
        key_vault_url = r'https://wkv3dc.vault.azure.net/'
        storage_account_url = r'https://azpoc1storage.blob.core.windows.net/'
        api_url = r'https://www.wroclaw.pl/open-data/f91dd592-95fe-416f-a43e-97838fbb0147/Deszczomierze.csv'
        
        logging.info('debug: Python HTTP trigger function processed a request.')

        storage_account_key = get_key_vault_secret(key_vault_url, "poc1AccountStorageKey")
        logging.info('debug: got a storage_account key')

        blob_service_client = create_blob_service_client(storage_account_url, storage_account_key)

        container_client = get_or_create_blob_container(blob_service_client, 'input')
        logging.info('debug: got a storage container input')

        received_data = download_data_from_api(api_url)
        logging.info('debug: api_return:{}'.format(received_data))

        upload_blob(container_client, "poc1.csv", received_data)
        logging.info('debug: save successful')

    except Exception as ex:
        logging.error('Exception:')
        logging.error(ex)
        return func.HttpResponse(
            str(ex),
            status_code=500
        )

    return func.HttpResponse(
        "operation successful, data saved to blob",
        status_code=200
    )
