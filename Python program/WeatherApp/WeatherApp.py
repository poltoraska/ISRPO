import requests
import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import os
import ttkbootstrap as tb

translate_dict = {
    "clear sky": "ясно",
    "few clouds": "малооблачно",
    "scattered clouds": "переменная облачность",
    "broken clouds": "облачно с прояснениями",
    "overcast clouds": "пасмурно",
    "drizzle": "моросящий дождь",
    "rain": "дождь",
    "thunderstorm": "гроза",
    "snow": "снег",
    "mist": "туман",
}

def get_weather(city):
    api_key = "91e2bf5cd630b2efe10aefb5a5983468"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric&lang=ru"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def save_data(name, city):
    data = {"name": name, "city": city}
    with open("user_data.json", "w") as file:
        json.dump(data, file)

def load_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            return json.load(file)
    return {"name": "", "city": ""}

def create_gui():
    root = tb.Window(themename="flatly")
    root.title("Прогноз погоды")
    root.geometry("400x600")

    style = ttk.Style()
    style.theme_use('clam')

    def apply_theme(theme):
        if theme == "dark":
            bg_color = "#282c34"
            fg_color = "#61dafb"
            entry_bg = "#3c3f41"
            button_bg = "#3c3f41"
            button_fg = "#ffffff"
            name_entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
            city_entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
            style.configure('TLabel', background=bg_color, foreground=fg_color)
        else:
            bg_color = "#eeedf4"
            fg_color = "#000000"
            entry_bg = "#ffffff"
            button_bg = "#65568f"
            button_fg = "#ffffff"
            style.configure('TButton',
                            background=button_bg,
                            foreground=button_fg,
                            padding=10,
                            relief="flat",
                            bordercolor=button_bg,
                            borderradius=20)  # Закругляем края кнопки
            style.map('TButton', background=[('active', button_bg)])
            name_entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
            city_entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)
            style.configure('TLabel', background=bg_color, foreground=fg_color)

        root.configure(bg=bg_color)
        name_label.config(background=bg_color, foreground=fg_color)
        greeting_label.config(background=bg_color, foreground=fg_color)
        city_label.config(background=bg_color, foreground=fg_color)
        temp_label.config(background=bg_color, foreground=fg_color)
        pressure_label.config(background=bg_color, foreground=fg_color)
        humidity_label.config(background=bg_color, foreground=fg_color)
        desc_label.config(background=bg_color, foreground=fg_color)
        wind_label.config(background=bg_color, foreground=fg_color)
        weather_frame.config(background=bg_color)
        theme_frame.config(background=bg_color)

    user_data = load_data()

    name_label = ttk.Label(root, text="Ваше имя:", font=("Helvetica", 14))
    name_label.pack(pady=10)
    name_entry = tk.Entry(root, font=("Helvetica", 14))
    name_entry.pack(pady=10)
    name_entry.insert(0, user_data["name"])

    def get_weather_button():
        name = name_entry.get()
        city = city_entry.get()
        save_data(name, city)
        greeting = get_greeting()
        greeting_label.config(text=f"{greeting}, {name}!")
        weather_data = get_weather(city)
        if weather_data:
            temp_label.config(text=f"{round(weather_data['main']['temp'])}°C")
            pressure_label.config(text=f"{weather_data['main']['pressure']} hPa")
            humidity_label.config(text=f"{weather_data['main']['humidity']}%")
            desc_label.config(text=weather_data['weather'][0]['description'])
            wind_label.config(text=f"{weather_data['wind']['speed']} м/с")
        else:
            temp_label.config(text="Город не найден")
            pressure_label.config(text="")
            humidity_label.config(text="")
            desc_label.config(text="")
            wind_label.config(text="")

    button = ttk.Button(root, text="Получить прогноз", command=get_weather_button, style='TButton')
    button.pack(pady=10)

    city_label = ttk.Label(root, text="Город:", font=("Helvetica", 14))
    city_label.pack(pady=10)
    city_entry = tk.Entry(root, font=("Helvetica", 14))
    city_entry.pack(pady=10)
    city_entry.insert(0, user_data["city"])

    greeting_label = ttk.Label(root, text="", font=("Roboto", 24))
    greeting_label.pack(pady=10)

    weather_frame = tk.Frame(root)
    weather_frame.pack(pady=20)

    temp_label = ttk.Label(weather_frame, text="", font=("Roboto", 48))
    temp_label.grid(row=0, column=0, padx=20)

    pressure_label = ttk.Label(weather_frame, text="", font=("Roboto", 14))
    pressure_label.grid(row=1, column=0, padx=20)

    humidity_label = ttk.Label(weather_frame, text="", font=("Roboto", 14))
    humidity_label.grid(row=2, column=0, padx=20)

    desc_label = ttk.Label(weather_frame, text="", font=("Roboto", 14))
    desc_label.grid(row=3, column=0, padx=20)

    wind_label = ttk.Label(weather_frame, text="", font=("Roboto", 14))
    wind_label.grid(row=4, column=0, padx=20)

    theme_frame = tk.Frame(root)
    theme_frame.pack(pady=10)
    ttk.Label(theme_frame, text="Тема:", style='TLabel').grid(row=0, column=0, padx=5)
    ttk.Button(theme_frame, text="Светлая", command=lambda: apply_theme("light")).grid(row=0, column=1, padx=5)
    ttk.Button(theme_frame, text="Тёмная", command=lambda: apply_theme("dark")).grid(row=0, column=2, padx=5)

    apply_theme("light")  # Устанавливаем начальную тему

    root.mainloop()

if __name__ == "__main__":
    create_gui()
