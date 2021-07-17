This project will be a really interesting project. But it really needs a lot of data within a large period of time and so far the project progress is 
still in getting that data.

It is about a time series analysis problem to correct badly predicted wind speed data provided by a certain company called "Windfinder".
The background is that I am a windsurfer, so I want good forecast results. But so often the predicted wind should be good and I have invested a lot of
money and a lot of time to go to the surf spot, but who was not there? Yep, the wind...
The really strange thing is that, from my observations, the wrong forecast has a very biased character. It tends to predict a lot of wind, not less.
Actually, we would also take the case that the forecast says less wind, but we get a lot of wind instead, right? 
But I could not observe this case in a significant value. 
So it was decided to record the forecast data over a longer period of time to analyze it.

This project is divided into several sub-instances. The first is a web scraper that fetches wind data from 3 specific locations in Germany.
In parallel, the free web service of "Open wether map" retrieves further weather data for 300 different locations around these 3 surf spots with a gaussian distribution 
with respect to the distance to them. The data includes the typical weather data like wind speed and direction, air pressure and temperature etc.

After analyzing the time series of the wind data with respect to my hypothesis of the strange distribution of the forecast results, I will try to 
build a model to correct the forecast using the weather data. I hope to do this using an LSTM or CNN based artificial neural network.
That's why I'm also getting the wether data.

Both tools are running as a bot on my Raspberry Pi.


Everything regarding the webscraper to fetch the wind forecast data is contained in the <webscraper> directory. 
The stuff regarding the tool for fetching wether data is in the <OWM> directory.

So far, my bots have fetched data from a period of about half a year. I think this is too little. Therefore, the project status should be only this 
described data. 
Later I will write the other stuff and do the data analysis.



######

<locate_sites_in_map.py> plots all sites of the weather observation points on a map


