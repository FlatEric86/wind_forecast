import json, requests
import time
import datetime


def get_weather_data(api_key):




    with open('/home/pi/Desktop/WEATHER_DATA/site_sample.json', encoding='utf8') as fin:
        city_data = json.load(fin)


    DATA = {}
    i = 0
    for key in city_data:
        ID      = city_data[key]["open_weather_city_id"]

        uri = "https://api.openweathermap.org/data/2.5/group?id={}&appid={}".format(ID, api_key)

        #### make request to server
        try:
            http_response = requests.get(uri)
        except Exception as e:
            print(e)
            # if excaption occoured, the data dictionary gets null values
            DATA.update({key: {'T': None, 'v': None, 'alpha': None, 'pressure': None, 'time': None}})
            i += 1
            continue

        data_as_json = http_response.json()
        #### we do here extract all the relevant data from the json file

        T     = data_as_json['list'][0]['main']['temp']     # temperature
        v     = data_as_json['list'][0]['wind']['speed']    # wind velocity
        alpha = data_as_json['list'][0]['wind']['deg']      # wind direction
        p     = data_as_json['list'][0]['main']['pressure'] # pressure of air
        t     = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")

        #### here we put the extracted data into the data Dictionary
        DATA.update({key: {'T': T, 'v': v, 'alpha': alpha, 'pressure' :p, 'time': t}})

        i += 1

        if i%60 == 0:
            time.sleep(120)

    return DATA
