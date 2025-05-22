from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

def fetch_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            "name": info.get("longName", "N/A"),
            "price": info.get("currentPrice", "N/A"),
            "marketCap": info.get("marketCap", "N/A"),
            "sector": info.get("sector", "N/A"),
            "dayHigh": info.get("dayHigh", "N/A"),
            "dayLow": info.get("dayLow", "N/A")
        }
    except Exception as e:
        return {"error": str(e)}

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol:
            stock_data = fetch_stock_info(symbol)
    return render_template("index.html", stock=stock_data)

if __name__ == "__main__":
    app.run(debug=True)
