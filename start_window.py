from work_with_api import *
from tkinter import *

root = Tk()
root.title("W E A T H E R   F O R E C A S T")
root.geometry("400x300+500+150")


hello_text = Label(text="Hello! \nLet's take a look at the weather forecast: ", fg="#fff", bg="#550AAC")
hello_text.pack()


def show_weather_info():
    text_data = 'City: \t\t{city} \nCoordinates: \t{coord}\nTemperature: \t{temp} ' \
                '\nWind speed: \t{wind} \nPressure: \t{press} \nHumidity: \t{humid} ' \
                '\nThe state of sky: \t{sky} \nCloud today: \t{cloud}'\
        .format(city=get_city(), coord=get_coordinate(), temp=get_temperature(),
                wind=get_wind_speed(), press=get_pressure(), humid=get_humidity(),
                sky=get_sky(), cloud=get_clouds())

    main_information = Label(text=text_data, justify=LEFT)
    main_information.pack()


show_weather_info()
root.mainloop()
