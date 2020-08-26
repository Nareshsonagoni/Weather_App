import tkinter as tk
# from PIL import ImageTk
import requests as rq

Height = 500
Width = 600


def test_function(entry):
    print("This is the entry", entry)


def format_weather(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (*C): %s' % (
            name, desc, temp)
    except:
        final_str = 'There is a problem retrieving the information'

    return final_str


def get_weather(city):
    weather_key = "a1391ae778b5b595e6aa29d9a1340eea"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = rq.get(url, params=params)
    weather = response.json()

    label['text'] = format_weather(weather)


# a1391ae778b5b595e6aa29d9a1340eea  bg='#33FFA1'

# api.openweathermap.org/data/2.5/forecast?id={city ID}&appid={your api key}


root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

# background_image = tk.PhotoImage(file='natural.png')
background_label = tk.Label(root, bg='#33FFA1')
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()
