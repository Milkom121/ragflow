"""
Conftest to ensure frontend API tests import their local common module before any other.
"""
import os
import sys

# Ensure local common module is loaded first when importing by name
sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)),
)
import pytest
import requests
from requests.exceptions import RequestException

# Skip frontend API tests if server is not available
HOST_ADDRESS = os.getenv("HOST_ADDRESS", "http://127.0.0.1:9380")
try:
    requests.get(HOST_ADDRESS, timeout=1)
except RequestException:
    pytest.skip("HTTP API server not available, skipping frontend API tests", allow_module_level=True)