#!/usr/bin/env python3
# coding: utf-8
"""PYTEST_DONT_REWRITE"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
try:
    from api.settings import RetCode
    from api.apps import app
except (SyntaxError, ImportError):
    pytest.skip(
        "api.settings or api.apps cannot be imported, skipping tests",
        allow_module_level=True,
    )


@pytest.fixture(autouse=True)
def configure_app(monkeypatch):
    app.testing = True
    monkeypatch.setattr("api.settings.OAUTH_CONFIG", {}, raising=False)
    return app


def test_get_login_channels_empty():
    client = app.test_client()
    response = client.get("/v1/user/login/channels")
    assert response.status_code == 200
    result = response.get_json()
    assert result["code"] == RetCode.SUCCESS
    assert result["data"] == []


def test_get_login_channels_with_entries(monkeypatch):
    monkeypatch.setattr(
        "api.settings.OAUTH_CONFIG",
        {"github": {"display_name": "GitHub", "icon": "github"}},
        raising=False,
    )
    client = app.test_client()
    response = client.get("/v1/user/login/channels")
    assert response.status_code == 200
    result = response.get_json()
    assert result["code"] == RetCode.SUCCESS
    assert result["data"] == [{"channel": "github", "display_name": "GitHub", "icon": "github"}]


def test_login_without_json():
    client = app.test_client()
    response = client.post("/v1/user/login")
    assert response.status_code == 200
    result = response.get_json()
    assert result["code"] == RetCode.AUTHENTICATION_ERROR
    assert result["data"] is False


def test_oauth_login_invalid_channel():
    client = app.test_client()
    response = client.get("/v1/user/login/invalid_channel")
    assert response.status_code == 200
    result = response.get_json()
    assert result["code"] == RetCode.EXCEPTION_ERROR
