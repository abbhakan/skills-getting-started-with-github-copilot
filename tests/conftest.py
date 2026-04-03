import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = app_module.get_initial_activities()
    yield
    app_module.activities = app_module.get_initial_activities()


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client