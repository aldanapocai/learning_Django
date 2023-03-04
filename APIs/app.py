import requests
import json

response = requests.get("https://api.tomitokko.repl.co/") #url is the API endpoint

#print(response.status_code) #Status_code -> 200: everything ok, we get a response. 
                                            #301, 400, 401(auth), 
                                            # 403(no access) , 404(endpoint not found), 503(is not ready, too much requests, etc)

#print(response.text) #response.text is a big string

res = json.loads(response.text) #load to json format 
#print(res)

for data in res:
    print(data)