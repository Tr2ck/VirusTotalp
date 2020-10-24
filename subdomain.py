import requests
import time
import json
import base64


domains = "qq.com"




def get(number):
        try:
                cursor="I"+str(number*10)+"\n."
                bs64 = base64.b64encode(cursor)
                header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"}
                url = "https://www.virustotal.com/ui/domains/"+domains+"/subdomains?relationships=resolutions&cursor="+str(bs64)+"&limit=10"
                print url
                res = requests.get(url,headers=header)
                t = json.loads(res.text)
                if t.has_key('error') != 'Ture':
                        for x in range(10):
                                print t['data'][x]['id']

        except:
                pass


if __name__ == "__main__":
        for x in range(1,10):
                get(x)
