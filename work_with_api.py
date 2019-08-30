import requests

data_from_api = requests.get('http://api.openweathermap.org/data/2.5/weather?'
                             'lat=49.235194&lon=28.428332&appid=8b55cc8d48eb884c83251946930bc0d5&units=metric')

data = data_from_api.json()
# print("Json formatted: \n", data, "\n\n")


def get_coordinate():
    coord_x = data['coord']['lon']
    coord_y = data['coord']['lat']
    return coord_x, coord_y


def get_city():
    return data['name']


def get_temperature():
    temp = data['main']['temp']
    res = str(temp) + ' degrees Celsius'
    return res


def get_wind_speed():
    a = str(data['wind']['speed']) + ' m/s'
    return a


def get_pressure():
    return str(data['main']['pressure']) + ' hPa'


def get_humidity():
    return str(data['main']['humidity']) + ' %'


def get_sky():
    a = data['weather'][0]['description']
    return a


def get_clouds():
    return str(data['clouds']['all']) + ' %'

# ---------------------------------------------------------------------------------
