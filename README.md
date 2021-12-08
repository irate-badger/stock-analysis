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

To get a rolling result for a 10 day period from 1-Jan-2021 to 8-Dec-2021 request the folling end point:

```sh
curl http://127.0.0.1:5000/rolling | jq .
```

This also accept the alternative ticker for looking at different values