import requests
import json

ip="127.0.0."
filename = "log.txt"

def get(number):
	try:
		url = "https://www.virustotal.com/vtapi/v2/ip-address/report?apikey=<APIkey>&ip="+str(ip)+str(number)
		print url
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
		response = requests.get(url,headers=headers)
		jsonstr = json.loads(response.text)     
		hostname = jsonstr['resolutions']
		for x in hostname:
			print x['hostname']
		f = open(filename,'a')
		f.write(json.dumps(hostname,ensure_ascii=False))
		f.write('\n')
		f.close()
	except:
		pass




def main():
	for number in range(1,255):
		get(number)



if __name__ == "__main__":
	main()
