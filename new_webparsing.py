
#parse inside json file
import json
import pandas

# f=open("app_ranking_list.json", "r")

# soup = json.load(f)

# f.close()

# df=pandas.DataFrame()
# # print (soup[0][0]['app_id'])
# for i in soup:
# 	for j in i:
# 		df =df.append({"app_id": j['app_id'], 'name':j['name'],"os":j['os']}, ignore_index=True)
# print(df)


f=open("app_ranking_list.json", "r")

soup = json.load(f)

f.close()

df=pandas.DataFrame()
# print (soup[0][0]['app_id'])
for i in soup:
	for j in i:
		print (j["app_id"])
		df =df.append(j, ignore_index=True)
df.to_csv("result.csv")