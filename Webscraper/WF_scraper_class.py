from bs4 import BeautifulSoup
import requests


class wind_finder_scraper:
    '''
    This class is a class that has included all things we need to scrape 
    wind forcast data from the webserver of Windfinder 
    (see: https://www.windfinder.com )
    '''
    
    def __init__(self, url):
        # we pass the coresponding url of the respecting data directly by the constructor
        self.url     = url
        
        # we define the possible header styles
        self.headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}) 
        
    def get_data(self):
        def get_dir_val(strng): 
            '''
            To extract value of wind direction from html string
            '''        
            strng = str(strng)
            for val in strng.split(' '):
                if val != '':
                    try:
                        z = int(val.replace('°', ''))
                        return z
                    except:
                        pass              

        def get_magnitude(strng):
            '''
            To extract value of wind direction from html string
            '''                    
            strng = str(strng)
            strng = strng.strip('<span class="units-ws">')
            strng = strng.strip('</span>')    
            return int(strng)
        
        
        try:
            self.response = requests.get(self.url, headers=self.headers)
        except Exception as e:
            return 'request_err'
            exit()
            
            
        try:
            self.parsed = BeautifulSoup(self.response.content, features='lxml')
        except Exception as e:
            return 'parsing_err'
            exit()
            

        data = {
            "day_0" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },

            "day_1" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },

            "day_2" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },

            "day_3" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },

            "day_4" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },   

            "day_5" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },    

            "day_6" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },  

            "day_7" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },  

            "day_8" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            },    

            "day_9" : {
                "direction"      : 'dir',
                "mean_magnitude" : 'mean',
                "max_magnitude"  : 'max'
            }    
        }
        
        self.all_10_data_tables = self.parsed.findAll('div', {'class': 'weathertable__body hours-8'})
        
        
        for i in range(1, 11):
            self.wind_magnitudes = self.all_10_data_tables[i-1].findAll('span', {'class': 'units-ws'})
            self.wind_directions = self.all_10_data_tables[i-1].findAll('span', {'class': 'data-direction-unit units-wd units-wd-deg data--minor weathertable__cell'})

            
            MEAN_MAGNITUDES = []
            MAX_MAGNITUDES  = []

            j = 0
            for magnitude_strng in self.wind_magnitudes:
                if j % 2 == 0:
                    MEAN_MAGNITUDES.append(get_magnitude(magnitude_strng))
                else:
                    MAX_MAGNITUDES.append(get_magnitude(magnitude_strng))

                j += 1

            DIRECTIONS = []    
            for dir_data in self.wind_directions:
                DIRECTIONS.append(get_dir_val(dir_data))    
                
            data['day_{}'.format(i-1)]['direction']      = DIRECTIONS
            data['day_{}'.format(i-1)]['mean_magnitude'] = MEAN_MAGNITUDES
            data['day_{}'.format(i-1)]['max_magnitude']  = MAX_MAGNITUDES
            
        return data
    
    
    
###############################################################################

# Intervalle = [01h, 04h, 07h, 10h, 13h, 16h, 19h, 22h]           

           
# scraper_obj = wind_finder_scraper('https://de.windfinder.com/forecast/potsdam')     
   
# data = scraper_obj.get_data()        
	
