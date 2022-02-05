
# Weather Monitoring App

Weather Monitoring App is a python GUI for Monitoring 
current weather condition.\
It gives cities weather condition in following
parameters:\
1 Weather condition \
2 Temperature\
3 Minimum Temperature\
4 Maximum Temperature\
5 Humidity\
6 Wind Speed\
7 Sunrise Time\
8 Sunset Time\
It has facility to search according to city name.\
It has default setting that saves user time.


## API Reference

#### Get all items

```http
https://openweathermap.org/price
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}|

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `['weather'][0]["main"]`      | `int` |Weather Condition|
| `['main']['temp']`      | `int` |Temperature|
| `['main']['mintemp']`      | `int` |Min. Temperature|
| `['main']['maxtemp']`      | `int` |Max. Temperature|
| `['main']['pressure']`      | `int` |Pressure|
| `['main']['humidity']`      | `int` |Humidity|
| `['wind']['speed']`      | `int` |Wind Speed|
| `['sys']['sunrise']`      | `int` | Sunrise Time|
| `['sys']['sunset']`      | `int` | Sunset Time|

#### Currently API Condition
currently code has my personal API but later i will adjust my code for your api


## Features
It gives cities weather condition in following
parameters:\
1 Weather condition \
2 Temperature\
3 Minimum Temperature\
4 Maximum Temperature\
5 Humidity\
6 Wind Speed\
7 Sunrise Time\
8 Sunset Time\
It has facility to search according to city name.\
It has default setting that saves user time.

## Authors

- [@ayushsoni9025](https://github.com/ayushsoni9025)


![Logo](https://raw.githubusercontent.com/ayushsoni9025/Weather-Detecting-Application/master/app_icon.ico)AlFA Weather Application


## How to run in your PC

step 1: Download Zip file from the about code

requirement:\
1 python
```bash
  https://www.python.org/downloads/
```
2 Tkinter(already comes with python) but if not\
download it from the python or any other terminal
```bash
  pip install tk-tools
```
3 Requests\
download it from the python or any other terminal
```bash
  pip install requests
```
step 2: Run main.py (main programme to be execute)
*Note :-* make sure all the code files in same folder otherwise the programme throw error
## 🚀 About Me
I'm a Electronic and communication student of Indore Institute of Science and Technology

Programming Skills:\
1 C++\
2 Python\
3 Data Stucture and Algorithm\
4 Electronic schematic and pcb design 



