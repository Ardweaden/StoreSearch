import requests
import json

def get_details(id,url="https://wso2.lavbic.net:9443/api/am/store/v0.11/apis/"):
	r = requests.get(url+id)
	return json.loads(r.text)

def make_api_call(details,call,parameters=None,auth="Bearer cd65c205-5af9-376c-9f8c-12cb25b4cd6d",https=True):
	urls = details["endpointURLs"][0]["environmentURLs"]
	urlHTTPS = urls["https"]
	urlHTTP = urls["http"]

	apis = json.loads(details['apiDefinition'])

	request_type = list(apis["paths"][call].keys())[0]

	if request_type == "get":
		request_url = urlHTTPS + call
		print(urlHTTPS,call)
		request_url = request_url.format(days=parameters[0])
		print(request_url)
		request_url = "https://wso2.lavbic.net:8243/AlifePortal-Api/api/public/v1 /top10Activities/4"
		r = requests.get(request_url,headers={"Authorization": auth})
		r = requests.get(request_url)
		print(r.text)
	elif request_type == "post":
		r = requests.post(urlHTTPS + call)


token = "cd65c205-5af9-376c-9f8c-12cb25b4cd6d"

a = get_details('0815aeb4-b191-48ca-aad5-244f12be701c')
b = a["endpointURLs"][0]["environmentURLs"]
urlHTTPS = b["https"]
urlHTTP = b["http"]
c = json.loads(a['apiDefinition'])
calls = list(c["paths"].keys())
print(calls[0])
print(c["paths"][calls[0]])
parameters = ["days"]
#print("/top10Activities/{days}".format(days=4))

make_api_call(a,"/top10Activities/{days}",parameters=[4])

