import yfinance as yf
from flask import Flask

#msft = yf.Ticker("MSFT")

#print(msft.dividends)




app = Flask(__name__)


@app.route("/<ticker1>")

def dividends(ticker1):
    stock = yf.Ticker(str(ticker1))
    return  str(stock.dividends[-1])

if __name__ == '__main__':
    app.run()