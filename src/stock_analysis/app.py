import pandas as pd
import datetime
from pandas_datareader import data as web
from pandas import Series, DataFrame

import flask
from flask import request


def root() -> str:
    # The root path for the webservice. Performs a lookup on Yahoo for the given stock symbol
    # Parameters:
    #   Symbol (str): Optional. Defaults to Apple if not provided
    # Returns:
    #   data (json): Json string containing the data for January 2021 for a given stock symbol

    symbol = request.args.get("ticker", default="AAPL")

    start = datetime.datetime(2021, 1, 1)
    end = datetime.datetime(2021, 2, 1)

    print(f"We have received: {symbol}")

    df = web.DataReader(symbol, "yahoo", start, end)
    return df.to_json()


def create_app():
    app = flask.Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def root_() -> str:
        return root()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
