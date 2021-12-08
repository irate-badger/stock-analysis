<h1>Stock Analysis Example Demo</h1>
<h2> Setup workspace with:</h2>

```sh
. setup-workspace.sh
```

This will setup your virtual environment and install required packages

<h2>To run the webservice:</h2>

```sh
python src/stock_analysis/app.py
```

This will provide access to stock details for a given symbol. By default the ticket is AAPL.

You can read the data from the stand along webservice by using curl and jq which will format it for you.

```sh
curl http://127.0.0.1:5000/ | jq .

or
curl http://127.0.0.1:5000/?ticker=GOOG | jq .
```