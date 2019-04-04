import requests
import json


def getdata():
    api_key = '0466ad07eb8e68af9cd1923bf5fbf9cb85ab13c8'
    guid = 'SALUD-99027'
    url = 'http://api.datosabiertos.presidencia.go.cr/api/v2/dashboards/' + guid + '.json/?auth_key=' + api_key
    response = requests.get(url) #use request to get data from url
    if response.status_code == 200:
        print(response.content)  # show data in json format
        data = json.loads(response.content)  # convert json format to python object
        print(data)  # show python object (dict)
        print(data["user"])  # access to an element from dict by example user


getdata()
