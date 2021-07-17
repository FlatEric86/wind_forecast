#!/usr/bin/python3


from WF_SCRAPER import wind_finder_scraper as wfs
import json
import datetime
import time
import random as rand
import os

urls = {
    'cospunder_see'   : "https://de.windfinder.com/forecast/cospudener",
    'fahrlaender_see' : "https://de.windfinder.com/forecast/potsdam",
    'mueritz'         : "https://de.windfinder.com/forecast/klink_mueritz"
}


# sleeper with random delay time to avoid static request pattern
# that may make us black listed 
#... I know, this equal distributed random is definetly also a non natural
# pattern. As analyst i would immidiatly recognize that in request log files. 
# Human behavior in terms of repeatly actions to certain time points is 
# not equal distributed regarding those timepoints
# but rather such as skewed binomial. 
# But Web-Server Architects mostly not beeing so clever...Thats why we use
# simply a equal distributed random time delay ;) 
time.sleep(rand.randint(0, 400))


# recently date_time stamp to label our data 
date = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")

# the path were we store the data
DIR  = '/home/pi/Desktop/WIND_FORECAST_DATA/DATA/' + date

os.mkdir(DIR)

# we do iterate across the 3 Url's we want to scrape
for site_name in urls:

    # a further sleeper with random delay time to avoid request pattern
    time.sleep(rand.randint(5, 30))

    # we pull the recent url from its dictionary
    url = urls.get(site_name)
    
    # we scrape the wind data from  windfinder
    wfs_obj = wfs(url)
    data    = wfs_obj.get_data()


    # we write here the data as json file into the 
    # corresponding directory
    
    
    with open(DIR + '/' + site_name + '.json', 'w') as fout:
        json.dump(data, fout)






