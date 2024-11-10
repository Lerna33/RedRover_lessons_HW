import pytest
from my_api_tests.api_tests.utils.api_client import client


@pytest.fixture
def api_client():
    return client
