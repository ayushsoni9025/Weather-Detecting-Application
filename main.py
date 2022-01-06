from tkinter import *
from tkinter import messagebox
import requests
import time
# app data
developer_name = ["Ayush Soni", "Abhay", "Sharad Pratap Singh", "Yogit Patel"]
community_name = "ARTIFICIAL LOGIC FIRM"
version = "1.0.0"
cradit = {developer_name[0]: "\tSearch API Data Provider",
          developer_name[1]: "\tSeach History Development",
          developer_name[2]: "\tInterface Design",
          developer_name[3]: "\tDefault Weather Condition"
          }
data_source = "https://openweathermap.org/current"
refrences = "Tkinter by freecodecamp.org\n\thttps://youtu.be/YXPyB4XeYLA \n Web Scraping by freecodecamp.org\n\thttps://youtu.be/XVv6mJpFOb0 \n API by freecodecamp.org\n\thttps://youtu.be/GZvSYJDk-us"
history_list = []
with open("default.txt", "r") as file:
    default = file.read()
i = 0


from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")


class WeatherApp:
    def __init__(self, weather_app):
        self.weather_app = weather_app
        # creating interface
        weather_app.title("Weather Application")
        weather_app.iconbitmap("app_icon.ico")
        device_height = weather_app.winfo_screenheight()
        device_width = weather_app.winfo_screenwidth()
        weather_app.geometry(str(device_width)+"x"+str(device_height)+"+0+0")
        # frame
        global option_frame
        option_frame = Frame(weather_app, bd=3, bg="#0A0A2A")
        option_frame.place(x=0, y=0, width=device_width /
                           4, height=device_height/2-100)

        global history_frame
        history_frame = Frame(weather_app, bd=3, bg="#819FF7")
        history_frame.place(x=0, y=device_height/2-100,
                            width=device_width/4, height=device_height/2+100)

        global live_frame
        live_frame = Frame(weather_app, bd=3, relief=RIDGE, bg="#0B0B61")
        live_frame.place(x=device_width/4, y=0,
                         width=(device_width*3)/4, height=device_height/4)

        self.seached_data(default, live_frame, history_frame)

        global data_moniter_frame
        data_moniter_frame = Frame(
            weather_app, bd=3, relief=RIDGE, bg="#2E2EFE")
        data_moniter_frame.place(x=device_width/4, y=device_height/4,
                                 width=(device_width*3)/4, height=(device_height*3)/4)

        # lables
        logo_alfa = Label(option_frame, text="Alफा", font=(
            "times new roman", 30, "bold"), bg="#0A0A2A", fg="white")
        logo_alfa.grid(row=0, column=0)

        logo_weather = Label(option_frame, text="Weather", font=(
            "times new roman", 30, "bold"), bg="#0A0A2A", fg="#A9A9F5")
        logo_weather.grid(row=0, column=1, sticky="w")

        search_bar = Entry(option_frame, font=("times new roman", 14),
                           relief="sunken", width=int(device_width/20-35))
        search_bar.grid(row=1, column=0, columnspan=2,
                        pady=25, padx=20, sticky="w")

        # button
        search_button = Button(option_frame, text="Search", font=(
            "times new roman", 11), relief="raised", width=12, command=lambda: [self.seached_data(search_bar.get(), data_moniter_frame, history_frame), self.remove_history(search_bar)])
        search_button.grid(row=2, column=1, padx=40, sticky="e")

        about_app = Button(option_frame, text="About Alफा Weather", font=(
            "times new roman", 11), relief="raised", width=int(device_width/20-40), command=self.about_app)
        about_app.grid(row=3, column=0, columnspan=2, pady=20)

        exit_app = Button(option_frame, text="Exit App", font=("times new roman", 11),
                          relief="raised", width=int(device_width/20-40), command=weather_app.quit)
        exit_app.grid(row=4, column=0, columnspan=2)

        #keyboard Shortcut
        weather_app.bind('<Control-x>', quit)
    # functions
    @staticmethod
    def about_app():
        actual_message = "Weather App is Opensource Application\nBuild by : "+community_name+"\n"+"Version -- "+version+"\n"+"Developers are:\n" + \
            developer_name[0]+":\n"+cradit[developer_name[0]]+"\n\n"+developer_name[1]+":\n"+cradit[developer_name[1]]+"\n\n" + \
            developer_name[2]+":\n"+cradit[developer_name[2]]+"\n\n" + \
            developer_name[3]+":\n"+cradit[developer_name[3]]+"\n\nData Source :\n\tOpen Weather App API\n\t" +\
            data_source+"\n\nRefrences : \n\n"+refrences
        messagebox.showinfo("About App", actual_message)

    def default_name(self, Text):
        self.Text = Text.strip()
        with open("default.txt", "w") as file:
            file.write(Text)
        global default
        default = Text

    def set_default(self):
        default_button.destroy()
        default_bar = Entry(live_frame, font=("times new roman", 14),
                           relief="sunken")
        default_bar.grid(row=0, column=5, columnspan=2)
        save_button = Button(live_frame, text="Save Default", bg="#0B0B61", fg="white", font=(
            "times new roman", 11), relief="raised", width=9, command=lambda: [self.seached_data(default_bar.get(), live_frame, history_frame)])
        save_button.grid(row=0, column=7)

    def default_write(self, frame, default):
        global default_button
        default_button = Button(live_frame, text="Set Default", bg="#0B0B61", fg="white", font=(
            "times new roman", 11), relief="raised", width=11, command = lambda: self.set_default())
        default_button.grid(row=0, column=7)
        row_0 = ["Temperature", "Min. Temperature", "Max. Temperature",
                 "Pressure", "Humidity", "Wind", "Sunrise", "Sunset"]
        row_1 = [temperature, min_temperature, max_temperature,
                 pressure, humidity, wind, sunrise, sunset]
        j = 0
        while(j < 8):
            Label(live_frame, text=row_0[j], bg="#0B0B61", font=(
                "new times roman", 14, "italic"), fg='white').grid(row=2, column=j, pady=10, padx=5)
            Label(live_frame, text=row_1[j], bg="#0B0B61", font=(
                "new times roman", 14, "italic"), fg='white').grid(row=3, column=j, pady=10, padx=5)
            j += 1
        global default_lable
        default_lable=Label(live_frame, text=default, font=("new times roman", 24,
                                              "bold italic"), bg="#0B0B61", fg='white').grid(row=0, column=5, columnspan=2)
        Label(live_frame, text=condition, font=("new times roman", 18,
                                                "italic"), bg="#0B0B61", fg='white').grid(row=0, column=0, padx=45, pady=10)
        with open("default.txt", "w") as file:
            file.write(default)

    def writing_data_moniter_frame(self, Text, data_frame):
        Label(data_frame, text=Text, font=("new times roman", 24,
                                           "bold italic"), fg='white', bg="#2E2EFE").grid(row=0, column=3, padx=45)
        Label(data_frame, text=condition, font=("new times roman", 18,
                                                "italic"), fg='white', bg="#2E2EFE").grid(row=1, column=3, padx=45)
        coloum_0 = "\tTemperature\t\n\tMin. Temperature\t\n\tMax. Temperature\t\nPressure\t\nHumidity\t\nWind\t\nSunrise\t\nSunset\t"
        Label(data_frame, text=coloum_0, font=("new times roman", 14, "italic"),
              fg="white", bg="#2E2EFE").grid(row=2, column=0, padx=60, pady=50)
        coloum_1 = "-\n-\n-\n-\n-\n-\n-\n-"
        Label(data_frame, text=coloum_1, font=("new times roman", 14, "italic"),
              fg="white", bg="#2E2EFE").grid(row=2, column=1, pady=50)
        coloum_2 = str(temperature)+'°C\t\n'+str(min_temperature)+'°C\t\n'+str(max_temperature)+'°C\t\n' + \
            str(pressure)+'hPa\t\n'+str(humidity)+'%\t\n' + \
            str(wind)+'m/s\t\n'+str(sunrise)+'\t\n'+str(sunset)
        Label(data_frame, text=coloum_2, font=("new times roman", 14, "italic"),
              fg="white", bg="#2E2EFE").grid(row=2, column=2, padx=60, pady=50)

    def write_history(self, Text, data_moniter_frame, history_frame):
        global i
        writer = Button(history_frame, text=Text, command=lambda: [self.seached_data(Text, data_moniter_frame, history_frame), self.writing_data_moniter_frame(
            Text, data_moniter_frame), self.write_history(Text, data_moniter_frame, history_frame)], width=35, font=("new times roman", 12, "italic"))
        if Text not in history_list:
            writer.grid(row=i, column=0, padx=5, pady=2)
            i += 1
            history_list.append(Text)

    def seached_data(self, Text, frame, history_frame):
        Text = Text.strip()
        try:
            api = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
                Text+'&appid='+api_key
            json_data = requests.get(api).json()
            global condition
            global temperature
            global min_temperature
            global max_temperature
            global pressure
            global humidity
            global wind
            global sunrise
            global sunset
            condition = json_data['weather'][0]['main']
            temperature = int(json_data['main']['temp']-273.15)
            min_temperature = int(json_data['main']['temp_min']-273.15)
            max_temperature = int(json_data['main']['temp_max']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise = time.strftime("%I:%M:%S", time.gmtime(
                json_data['sys']['sunrise']-19800))
            sunset = time.strftime("%I:%M:%S", time.gmtime(
                json_data['sys']['sunset']-19800))
            for widgets in frame.winfo_children():
                widgets.destroy()
            if frame is live_frame:
                default = Text
                self.default_write(frame, default)
            elif frame is data_moniter_frame:
                self.writing_data_moniter_frame(Text, frame)
                self.write_history(Text, frame, history_frame)
        except:
            actual_message = Text+" is not in our database"
            messagebox.showwarning("Invalid City Name", actual_message)

    def remove_history(self, entry):
        entry.delete(0, 'end')

root = Tk()
Weather = WeatherApp(root)
root.mainloop()