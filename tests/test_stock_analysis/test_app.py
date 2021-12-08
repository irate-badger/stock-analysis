import pytest
from unittest.mock import MagicMock, patch
import json

from flask import Flask
from flask_testing import TestCase
from grappa import expect

from stock_analysis.app import create_app


class dummy_dataframe:
    def to_json(self):
        return json.dumps(
            {
                "High": {
                    "1609718400000": 133.6100006104,
                },
                "Low": {
                    "1609718400000": 126.7600021362,
                },
                "Open": {
                    "1609718400000": 133.5200042725,
                },
                "Close": {
                    "1609718400000": 129.4100036621,
                },
                "Volume": {
                    "1609718400000": 143301900,
                },
                "Adj Close": {
                    "1609718400000": 128.6170959473,
                },
            }
        )


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("stock_analysis.app.web")
def test_root(mocked_datareader, client):
    def data_reader(symbol, source, start, end):
        return dummy_dataframe()

    mocked_datareader.DataReader = data_reader

    response = client.get("/")

    response.status_code | expect.to.be.equal.to(200)

    json.loads(response.data) | expect.to.be.equal.to(
        {
            "High": {
                "1609718400000": 133.6100006104,
            },
            "Low": {
                "1609718400000": 126.7600021362,
            },
            "Open": {
                "1609718400000": 133.5200042725,
            },
            "Close": {
                "1609718400000": 129.4100036621,
            },
            "Volume": {
                "1609718400000": 143301900,
            },
            "Adj Close": {
                "1609718400000": 128.6170959473,
            },
        }
    )
