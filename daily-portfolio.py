import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

symbol = "MSFT"


#Capturing data

import csv

with open('portfolio.csv','w+') as file:
    myFile=csv.writer(file)
    myFile.writerow(["stock", "shares"])
    stock=input("What is the ticker of the stock you own?")
    shares=input("How many shares do you own?")
    myFile.writerow([stock,shares])











# 1. INFO INPUTS

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)
#print(type(response)) #> requests.models.Response
#print(response.text) #> 200

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: sort to ensure latest day is first. currently assuming latest day is on top 

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]
latest_open = tsd[latest_day]["1. open"]





#breakpoint()



# 2. INFO OUTPUTS

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")

print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"LATEST OPEN: {to_usd(float(latest_open))}")


