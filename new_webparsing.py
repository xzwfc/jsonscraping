
#parse inside json file
import json

f=open("app_ranking_list", "r")

soup = json.load(f)

f.close()