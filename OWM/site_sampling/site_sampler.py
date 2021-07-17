from sklearn.metrics.pairwise import haversine_distances
from math import radians
import json
import random as rand
from tqdm import tqdm

'''
This script is used to select an appropriate set of observation sites from a large list of all the
possible weather stations that we can access via the Open Weather Map API.
We want to obtain approximately evenly distributed sample points around the center representing our area of interest.
'''




# reference coordinate (site: Leipzig) [lat, lon]
ref_coord = (51.27071, 12.33569) 
ref_rad   = [radians(ref_coord[0]), radians(ref_coord[1])]

  

# all cities
with open('./city.list.json', encoding="utf8") as fin:
    city_data = json.load(fin)
    
# here we shufle the list of the city data
rand.shuffle(city_data)    


# core area will get cities in a near feald area regarding the
# reference site
core_area = []
second_ordary_area = []

flag_a = 0
flag_b = 0

for city in tqdm(city_data):
    lon = city['coord']['lon']
    lat = city['coord']['lat']
    
    x_1 = [radians(lat), radians(lon)]
    
    
    dist = haversine_distances([ref_rad, x_1])*6371
    dist = max(max(dist[0]), max(dist[1]))

    # for the core area we want to get near field sites but without clusters
    0
    if dist <= 450:
        if flag_a == 0:
            core_area.append(city)
            flag_a = 1
            continue
            
        if flag_a == 1:
            eval_vec = []
            for city_ in core_area:
                lat_ = city_['coord']['lat']
                lon_ = city_['coord']['lon']
                
                
                x_0 = [radians(lat_), radians(lon_)]
                
                dist_ = haversine_distances([x_0, x_1])*6371
                dist_ = max(max(dist_[0]), max(dist_[1]))
                
                if dist_ > 60:
                    eval_vec.append(1)
                else:
                    eval_vec.append(0)
                    
            if len(eval_vec) == sum(eval_vec):
                core_area.append(city)
        
    # for the second ordary we want to get sites with more distance to any 
    # other than like core area and also without clusters  
        
    if dist <= 2500 and dist > 500:
        if flag_b == 0:   
            second_ordary_area.append(city)
            flag_b = 1
            continue
        if flag_b == 1:
            eval_vec = []
            for city_ in second_ordary_area:
                lat_ = city_['coord']['lat']
                lon_ = city_['coord']['lon']
                
                
                x_0 = [radians(lat_), radians(lon_)]
                
                dist_ = haversine_distances([x_0, x_1])*6371
                dist_ = max(max(dist_[0]), max(dist_[1]))
                
                if dist_ > 200:
                    eval_vec.append(1)
                else:
                    eval_vec.append(0)
                    
            if len(eval_vec) == sum(eval_vec):
                second_ordary_area.append(city)      


    if len(core_area) >= 60 and len(second_ordary_area) >= 180:
        break


##### random choice

if len(core_area) > 60:
    core_area = rand.sample(core_area, 60)
 
if len(second_ordary_area) > 180: 
    second_ordary_area = rand.sample(second_ordary_area, 180)


all_sets = core_area + second_ordary_area

##### write sample as json file

with open('../sample.json', 'w', encoding="utf8") as fout:
    fout.write('{\n')
    
    i = 0
    for city in all_sets:
    
        if i < len(all_sets)-1:
            fout.write('\t' + '"' + str(city['name']) + '" : {\n')
            fout.write('\t\t' + '"open_weather_city_id" : ' + str(city['id']) + ',\n')
            fout.write('\t\t' + '"lat" : ' + str(city['coord']['lat']) + ',\n')
            fout.write('\t\t' + '"lon" : ' + str(city['coord']['lon']) + '\n')
            fout.write('\t},\n')
            
        if i == len(all_sets)-1:
            fout.write('\t' + '"' + str(city['name']) + '" : {\n')
            fout.write('\t\t' + '"open_weather_city_id" : ' + str(city['id']) + ',\n')
            fout.write('\t\t' + '"lat" : ' + str(city['coord']['lat']) + ',\n')
            fout.write('\t\t' + '"lon" : ' + str(city['coord']['lon']) + '\n')
            fout.write('\t}\n')
            
        i += 1
        
    fout.write('}\n')







