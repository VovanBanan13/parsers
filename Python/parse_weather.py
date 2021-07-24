# Python

import requests
import json
import time

API_KEY = "0cb94b92bd681d0cc1c1f97810e8c4a1"

lat  = 54.1838  # широта
lon = 45.1749  # долгота

pressure_arr = []
temperature_diff = []
temperature_diff_day = []

temp = {
    "day": temperature_diff_day,
    "diff": temperature_diff
    }

api_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&lang=ru&appid={API_KEY}").text
json_response = json.loads(api_response)

for i in range(5):    
    pressure_arr.append(json_response["daily"][i]["pressure"])
    temp["day"].append(json_response["daily"][i]["dt"])
    temp["diff"].append(abs((json_response["daily"][i]["temp"]["morn"])-(json_response["daily"][i]["temp"]["night"])))

real_dt = time.strftime("%a, %d %b %Y", time.localtime(temp["day"][temp["diff"].index(min(temp["diff"]))]))

print("Максимальное давление за предстоящие 5 дней: ", max(pressure_arr), "Па")
print("День с минимальной разницей между ночной и утренней температурой: ", real_dt, " (разница {0:.2f} \u2103 )".format(min(temp["diff"])))