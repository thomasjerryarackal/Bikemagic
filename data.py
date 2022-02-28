import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'S.no': "1",   
                            'Bike_company': "Bajaj",   
                            'Bike_model': "Avenger 220",   
                            'Manufactured_year': "2020",   
                            'Engine_warranty': "5",   
                            'Engine_type': "Single",   
                            'Fuel_type': "Petrol",   
                            'CC(Cubic capacity)': "220CC",   
                            'Fuel_Capacity': "10 Litres",   
                            'Price': "113000",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7ab040608ddd442ca70947f12c3fa36e/services/4ae250a336cb40b8bd208c185542f33e/execute?api-version=2.0&format=swagger'
api_key = 'o/gOETzMPvRujiwxy99/x29lp/vfrg793oAma845ntH0pfeHZEQkDhfg5oLrgRXH4+C33KmUNw5rFxXQ2XULUw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))