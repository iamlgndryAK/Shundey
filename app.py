from datetime import datetime
from flask import Flask, render_template
from requests import get


app = Flask(__name__)
count = 0


@app.route("/", methods=["POST", "GET"])
def home():
    global count
    now = datetime.now()
    day = now.timetuple().tm_yday
    response = get(url="https://www.quotepub.com/api/widget/?type=qotd_t")
    quote = response.json()['quote_body']
    today = now.strftime("%B %d")
    count = 10 + (day - 59)
    second = now.now()

    return render_template("index.html", count=count, today=today, quote=quote, second=second)


if __name__ == "__main__":
    app.run(debug=True)
