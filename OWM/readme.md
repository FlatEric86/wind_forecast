The script <getter.py> is a function that fetch the recently weather data from the OpenWeatherMap Server by its API.

<get_weather_data.py> calls this funtion and pass the unique API-Key (you can request such as one on the website at: [**link**](https://openweathermap.org/) )
and gets the weather data. In addition it writes the data as a json fileformat on the drive.

The json file hase included all site definition regarding their GPS coordinates and ID for the API.

These sites were sampled of a large list of all given observation stations. More detailed Infos is the regarding directory.

Via cron job and a bot based on the second script the weather data get downloaded approxamatly each 10'th minute.
