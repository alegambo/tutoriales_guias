import requests
import json

if __name__ == '__main__':

    api_key = 'baf0fa5633774e38fc5ce95b7945b884a8dd26dd'
    guid = 'INVER-EN-ID-SEGUN-AREA'
    url = 'http://micit.cloudapi.junar.com/api/v2/visualizations/' + guid + '.json/?auth_key=' + api_key
    response = requests.get(url)  # use request to get data from url
    if response.status_code == 200:
        print(response.content)  # show data in json format
        data = json.loads(response.content)  # convert json format to python object
        print(data)  # show python object (dict)
        print(data["user"])  # access to an element from dict by example user


