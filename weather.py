import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('CHXX5650')
#yahoo_result = pywapi.get_weather_from_yahoo('CHXX5650')


print("Weather.com says: It is " + str.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Zhuzhou.\n\n")

#a=pywapi.get_location_ids('zhuzhou')
#print(a)
