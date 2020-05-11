import json
import requests
import argparse

KEY = "<alphavantage free account key>"
TREND = {}


def get_quote(symbol, api_key):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(symbol, api_key)
    request = requests.get(url)
    json_dict = eval(json.loads(json.dumps(request.text)))
    return json_dict


def avg_prices(trend_data):

    sum_o = 0
    sum_h = 0
    sum_l = 0
    sum_c = 0

    for key in trend_data:
        open_price = float(trend_data[key]["1. open"])
        high_price = float(trend_data[key]["2. high"])
        low_price = float(trend_data[key]["3. low"])
        close_price = float(trend_data[key]["4. close"])

        sum_o += open_price
        sum_h += high_price
        sum_l += low_price
        sum_c += close_price

    avg_result = {
        "avg_open": round(sum_o / len(trend_data), 3),
        "avg_high": round(sum_h / len(trend_data), 3),
        "avg_low": round(sum_l / len(trend_data), 3),
        "avg_close": round(sum_c / len(trend_data), 3),
    }

    return avg_result


def max_prices(trend_data):

    sum_o = 0
    sum_h = 0
    sum_l = 0
    sum_c = 0

    for key in trend_data:
        open_price = float(trend_data[key]["1. open"])
        high_price = float(trend_data[key]["2. high"])
        low_price = float(trend_data[key]["3. low"])
        close_price = float(trend_data[key]["4. close"])

        if open_price > sum_o:
            sum_o = open_price

        if high_price > sum_h:
            sum_h = high_price

        if low_price > sum_l:
            sum_l = low_price

        if close_price > sum_c:
            sum_c = close_price

    max_result = {
        "max_open": round(sum_o, 3),
        "max_high": round(sum_h, 3),
        "max_low": round(sum_l, 3),
        "max_close": round(sum_c, 3),
    }

    return max_result


def min_prices(trend_data):

    sum_o = []
    sum_h = []
    sum_l = []
    sum_c = []

    for key in trend_data:
        open_price = float(trend_data[key]["1. open"])
        high_price = float(trend_data[key]["2. high"])
        low_price = float(trend_data[key]["3. low"])
        close_price = float(trend_data[key]["4. close"])

        sum_o.append(open_price)
        sum_h.append(high_price)
        sum_l.append(low_price)
        sum_c.append(close_price)

    min_result = {
        "min_open": round(min(sum_o), 3),
        "min_high": round(min(sum_h), 3),
        "min_low": round(min(sum_l), 3),
        "min_close": round(min(sum_c), 3),
    }

    return min_result


def spaces(s, sep_val):
    space = " " * (sep_val - len(s))
    return space


def divider(num):
    print("-" *num)


def visual(name, quantity, price, avg, maxx, minn):
    print("Stock price analysis for {}\n\n".format(name))

    print("Assets:")
    divider(50)
    print("Quantity: {} @ rate: {} = {}\n\n".format(quantity, price, quantity*price))

    print("Price variation:")

    divider(50)
    print("TYPE {} {} {} {} {} {}".format(spaces("TYPE", 10), "AVERAGE", spaces("AVERAGE", 10), "MAX", spaces("MAX", 10), "MIN"))
    divider(50)
    print("Open:{} {} {} {} {} {}".format(spaces("Open", 10), avg["avg_open"], spaces(str(avg["avg_open"]), 10), maxx["max_open"], spaces(str(maxx["max_open"]), 10), minn["min_open"]))
    print("High:{} {} {} {} {} {}".format(spaces("High", 10), avg["avg_high"], spaces(str(avg["avg_high"]), 10), maxx["max_high"], spaces(str(maxx["max_high"]), 10), minn["min_high"]))
    print("Low:{} {} {} {} {} {}".format(spaces("Low", 10), avg["avg_low"], spaces(str(avg["avg_low"]), 10), maxx["max_low"], spaces(str(maxx["max_low"]), 10), minn["min_low"]))
    print("Close:{} {} {} {} {} {}".format(spaces("Close", 10), avg["avg_close"], spaces(str(avg["avg_close"]), 10), maxx["max_close"], spaces(str(maxx["max_close"]), 10), minn["min_close"]))
    divider(50)

    print("\n\nGains:")
    divider(50)
    print("Average possible {} = {}".format(spaces("Average possible", 16), round((avg["avg_close"] * quantity) - (quantity * price), 2)))
    print("Highest possible {} = {}".format(spaces("Highest possible", 16), (maxx["max_high"] * quantity) - (quantity * price)))
    print("Lowest possible {} = {}".format(spaces("Lowest possible", 16), (minn["min_low"] * quantity) - (quantity * price)))
    divider(50)

    now_data = {}
    now_date = ""
    for key in TREND:
        now_date = key
        now_data = TREND[key]
        break

    print("\n\nGains on {}:".format(now_date))
    divider(50)
    print("Actual possible {} = {}".format(spaces("Average possible", 16), round((float(now_data["4. close"]) * quantity) - (quantity * price), 2)))
    print("Highest possible {} = {}".format(spaces("Highest possible", 16), (float(now_data["2. high"]) * quantity) - (quantity * price)))
    print("Lowest possible {} = {}".format(spaces("Lowest possible", 16), (float(now_data["3. low"]) * quantity) - (quantity * price)))
    divider(50)

    print("\n\nProfile Score: ")
    divider(50)
    num = (avg["avg_close"] * quantity) - (quantity * price)
    if num > 0:
        percent = round((num * 100) / (quantity * price), 3)
    else:
        percent = 0

    print("{} %".format(percent))
    divider(50)


def main(name, quantity, price):
    quote = get_quote(name, KEY)
    time_series_data = quote["Time Series (Daily)"]

    for key in time_series_data:
        date = key
        data = time_series_data[key]
        TREND[date] = data

    avg = avg_prices(TREND)
    maxx = max_prices(TREND)
    minn = min_prices(TREND)

    visual(name, quantity, price, avg, maxx, minn)


parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Symbol of the stock to chase', required=True)
parser.add_argument('--quantity', help='Quantity of stocks that you purchased', required=True)
parser.add_argument('--price', help='Price of stock at which you purchased', required=True)

args = parser.parse_args()

try:
    main(str(args.name), int(args.quantity), float(args.price))
except Exception as error:
    print("There was some error while execution. \n\nError: {}".format(error))
