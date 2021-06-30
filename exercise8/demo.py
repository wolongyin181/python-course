import requests

base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&"
data_param="date=2021-06-16"
nasa_image=requests.get(base_url+data_param)

nasa_data = nasa_image.json()

print(nasa_data["url"])

import datetime

today=datetime.date.today()
yesterday=today-datetime.timedelta(days=2)
print(yesterday.strftime('%Y-%m-%d'))