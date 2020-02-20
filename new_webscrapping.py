# this page is firstly loaded by html (a blank page) and then run java program to get info into this page
from urllib.request import urlopen
f=open("app_ranking_list.json", 'wb')

# response=urlopen("https://sensortower.com/ios/rankings/top/iphone/us/all-categories?date=2020-02-20")
response=urlopen("https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-20T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0")
html=response.read()

f.write(html)
f.close()

# get the link that actually contains the info
# inspect
# network
# XHR
# copy address
# it is a json file not a html
# https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-20T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0

