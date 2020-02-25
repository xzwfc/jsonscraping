

from urllib.request import urlopen
f=open("app_ranking_list2.json", 'wb')

# response=urlopen("https://sensortower.com/ios/rankings/top/iphone/us/all-categories?date=2020-02-20")
response=urlopen("https://api.twitter.com/1.1/search/tweets.json")

json=response.read()

f.write(json)
f.close()