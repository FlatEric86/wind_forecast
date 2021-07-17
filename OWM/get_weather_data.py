
#!/usr/bin/python3

from getter import get_weather_data as gwd
import json
import datetime
import time
import os



api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


#### get the weatherdate from open weather server
DATA = gwd(api_key)


date = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")

with open('/home/pi/Desktop/WEATHER_DATA/DATA/' + date + '.csv', 'w', encoding='utf8') as fout:
    # write header
    fout.write('site, T, v, alpha, p, t\n')
    for site in DATA:
        site_name = site.replace(' ', '_')
        #json.dump(DATA[site], fout)
        T     = DATA[site]['T']
        v     = DATA[site]['v']
        alpha = DATA[site]['alpha']
        p     = DATA[site]['pressure']
        t     = DATA[site]['time']
        fout.write('{},{},{},{},{},{}\n'.format(site, T, v, alpha, p, t))
