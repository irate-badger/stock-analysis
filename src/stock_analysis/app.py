import pandas as pd
from datetime import datetime
from pandas_datareader import data as web

import flask
from flask import request


def root() -> str:
    # The root path for the webservice. Performs a lookup on Yahoo for the given stock symbol
    # Parameters:
    #   Symbol (str): Optional. Defaults to Apple if not provided
    # Returns:
    #   data (json): Json string containing the data for January 2021 for a given stock symbol

    symbol = request.args.get("ticker", default="AAPL")

    start = datetime(2021, 1, 1)
    end = datetime(2021, 2, 1)

    print(f"We have received: {symbol}")

    df = web.DataReader(symbol, "yahoo", start, end)
    return df.to_json()


def rolling() -> str:
    # A rolling value endpoint for the webservice.
    # Performs a lookup on Yahoo for the given stock symbol
    # Parameters:
    #   Symbol (str): Optional. Defaults to Apple if not provided
    # Returns:
    #   data (json): Json string containing the data for January 2021 for a given stock symbol

    symbol = request.args.get("ticker", default="AAPL")

    start = datetime(2021, 1, 1)
    end = datetime(2021, 12, 8)

    print(f"We have received: {symbol}")

    df = web.DataReader(symbol, "yahoo", start, end)
    close_px = df["Adj Close"]
    mavg = close_px.rolling(window=10).mean()

    return mavg.to_json()


def create_app():
    app = flask.Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def root_() -> str:
        return root()

    @app.route("/rolling", methods=["GET", "POST"])
    def rolling_() -> str:
        return rolling()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
