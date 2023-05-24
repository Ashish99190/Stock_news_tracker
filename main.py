import requests
from twilio.rest import Client
STOCK = "Reliace"
COMPANY_NAME = "Reliance Ind."
STOCK_API = "3K577W9XKESH4GK1"
account_ssid = "your_SSID"
acct_token ="your_token"
NEWS_API = "3e9cefde8ee04721ba2401e41a594e41"
STOCK_ENDPOINT = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=3K577W9XKESH4GK1"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


n_url = 'https://newsapi.org/v2/everything?q=RIL%20share&language=en&apiKey=3e9cefde8ee04721ba2401e41a594e41'
n = requests.get(n_url)
news_data = n.json()
articales = news_data["articles"][:3]
titles = [articales[x]["title"] for x in range(3)]
description = [articales[x]["description"] for x in range(3)]




# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=3K577W9XKESH4GK1'
r = requests.get(url)
data = r.json()

time_series = list(data["Time Series (Daily)"].items())

today_data = float(time_series[0][1]["4. close"])
yesterday_data =float(time_series[1][1]["4. close"])

differnce = abs(yesterday_data - today_data)
diff_per = (differnce/today_data)*100
print(today_data)
print(yesterday_data)
print(diff_per)

if diff_per >= 0.2 :
        client = Client(account_ssid, acct_token)
        for i in range(3):
            message = client.messages.create(
                body=f"Reliance: 🔻5% \n Headline:{titles[i]} (Reliance)?. \n Brief:{description[i]} ",
                from_="+13204139003",
                to="+818097708193"
            )
            print(message.status)

