import requests
import json
def get_page(url):
    try:
        page = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        print("Error ->>>>>>>> "+str(e))
    if page.status_code == 200:
        return page.text

def post_page(data):
    url = "http://192.168.0.143:8080/ipapi/api/ip/batch"
    print(type(data))
    try:
        page = requests.post(url=url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    except Exception as e:
        print("Error ->>>>>>>> " + str(e))
    if page.status_code == 200:
        print(page.text)
        return page.text


if __name__ == '__main__':
    url= "http://192.168.0.143:8080/ipapi/api/ip/batch"
    data = ("185.93.120.126","185.193.20.122","85.93.120.114")
    post_page( data)
