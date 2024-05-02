import pytest
from unittest.mock import Mock, patch, MagicMock

from azure.functions import HttpRequest, HttpResponse
from src.function_app import (
    get_key_vault_secret,
    create_blob_service_client,
    get_or_create_blob_container,
    download_data_from_api,
    upload_blob,
    http_trigger
)



def test_get_or_create_blob_container_exists():


    assert 1 == 1#


