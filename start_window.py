import requests
from tkinter import *

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


def starting_gui():
    root = Tk()
    root.title("W E A T H E R   F O R E C A S T")
    root.geometry("400x300+500+150")

    hello_text = Label(text="Hello! \nLet's take a look at the weather forecast: ", fg="#fff", bg="#550AAC")
    hello_text.pack()

    show_weather_info_gui()
    root.mainloop()


def show_weather_info_gui():
    text_data = 'City: \t\t{city} \nCoordinates: \t{coord}\nTemperature: \t{temp} ' \
                '\nWind speed: \t{wind} \nPressure: \t{press} \nHumidity: \t{humid} ' \
                '\nThe state of sky: \t{sky} \nCloud today: \t{cloud}'\
        .format(city=get_city(), coord=get_coordinate(), temp=get_temperature(),
                wind=get_wind_speed(), press=get_pressure(), humid=get_humidity(),
                sky=get_sky(), cloud=get_clouds())

    main_information = Label(text=text_data, justify=LEFT)
    main_information.pack()


def show_weather_info_console():
    text_data = 'City: \t\t{city} \nCoordinates: \t{coord}\nTemperature: \t{temp} ' \
                '\nWind speed: \t{wind} \nPressure: \t{press} \nHumidity: \t{humid} ' \
                '\nThe state of sky: \t{sky} \nCloud today: \t{cloud}' \
        .format(city=get_city(), coord=get_coordinate(), temp=get_temperature(),
                wind=get_wind_speed(), press=get_pressure(), humid=get_humidity(),
                sky=get_sky(), cloud=get_clouds())

    print(text_data)


show_weather_info_console()
