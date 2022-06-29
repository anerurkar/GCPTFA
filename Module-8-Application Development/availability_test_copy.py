import requests
import threading
def call_api():

    url = "https://a-rqe45r6mgq-uc.a.run.app/welcome"

    payload={}
    headers = {
        'Accept': '*/*'
    }

    for i in range(0,100000000):
        response = requests.request("GET", url, headers=headers, data=payload)
        #print(response.text)
        print(response.text)

def create_threads():

    # creating thread
    for k in range(0,1000):
        thread_var = threading.Thread(target=call_api, args=())
        thread_var.start()



if __name__ == "__main__":
 create_threads()