import json
import urllib.request
import geopy.distance

key= 'ab5bf4b0970860437fc442604639d812' # for openweathermap
data = []

def space_data():
  global latitude, longitude
  url_space = "http://api.open-notify.org/iss-now.json" # ISS spacecraft url to get the data
  response = urllib.request.urlopen(url_space) # requesting ISS data
  result = json.loads(response.read()) #save data in variable result
  longitude = result['iss_position']['longitude'] #latitude of ISS
  latitude = result['iss_position']['latitude'] #longitude of ISS
  data.append(longitude) # add data to list
  data.append(latitude)
  return(data)
  

space_data()


def weather_data():
  weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}"
  response = urllib.request.urlopen(weather_url)
  result = json.loads(response.read())
  #print(result)

  weather_info = result['weather'][0]['description'] #weather_info variable has weather description
  temp_celcius = round(result['main']['temp'] - 273.15, 2) #get temperature in celcius from Kelvin
  temp_feels = round(result['main']['feels_like']- 273.15, 2)
  #feels like temp in celcius
  humidity = result['main']['humidity']
  #visibility = result['main']['visibility']

  weather_details = f"The weather of this location is {weather_info}. The temperature is {temp_celcius}C at the moment but it feels like {temp_feels}C. Due to this, the humidity is {humidity}. "
  data.append(weather_details)
  return(data)


weather_data()

def geolocation(): # function to get location based on lon and lat
  global country_code
  key = 'toIFCz693DvWw1kNlCKAsNl7gUqRCAM6'

  url = f"http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={latitude},{longitude}&includeRoadMetadata=true&includeNearestIntersection=true"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  country_code = result['results'][0]['locations'][0]['adminArea1']
  data.append(country_code)
  return(data)

 
  

geolocation()

  
def flag(): #flag function to get country name and flag
  if country_code != 'XZ':
    url =f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = urllib.request.urlopen(url)
      #Store the data in resul4 variable
    result = json.loads(response.read())
    country = result[0]['name']['common']
    flag_url = result[0]['flags']['png']

    message_country = f"ISS is currently over {country}"
    data.append(message_country)
    data.append(flag_url)
    return(data)

   
  else:
    message_country = "ISS is currently over the Ocean."
    imageurl = 'static/images/ocean.jpeg'
    data.append(message_country)
    data.append(imageurl)
    return(data)
  
flag()


def my_location():
  key = 'toIFCz693DvWw1kNlCKAsNl7gUqRCAM6' #key for mapquestapi

  location = '49_Charcoal_Way,Brampton'

  url = f"http://www.mapquestapi.com/geocoding/v1/address?key={key}&location={location}"
  
  response = urllib.request.urlopen(url)  #Store data in result variable
  result = json.loads(response.read()) #Storing my latitude and longitude in variable

  my_lat = result['results'][0]['locations'][0]['latLng']['lat']
  my_lon = result['results'][0]['locations'][0]['latLng']['lng']

  my_loc = (float(my_lat), float(my_lon)) #my current location lat and longitude
  iss_loc = (float(latitude), float(longitude))

  distance =f"The ISS craft is currently {round(geopy.distance.geodesic(my_loc, iss_loc).km, 2)} KM away from my location."
  data.append(distance)
  return(data)
  

my_location()


def api_data():
  return(data)



            


  
  

  
