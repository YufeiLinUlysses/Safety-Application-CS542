import pandas as pd
import datetime
result = pd.DataFrame()
boston = pd.read_csv("Boston.csv")
boston["date_time"] = pd.to_datetime(
    boston["date_time"], format='%Y-%m-%d %H:%M:%S')
result["date"] = boston["date_time"].dt.date
result["time"] = boston["date_time"].dt.hour
# in celcius
result["temperature"] = boston["HeatIndexC"]
# humidity in percentage
result["humidity"] = boston["humidity"]
# in kilometer per hour
result["windspeed"] = boston["windspeedKmph"]
# air pressure, kpa
result["pressure"] = boston["pressure"]
result["visibility"] = boston["visibility"]
# round up to nearest hour
result["sunrise"] = pd.to_datetime(
    boston["sunrise"], format="%I:%M %p").dt.round("H").dt.hour
# round up to nearest hour
result["sunset"] = pd.to_datetime(
    boston["sunset"], format="%I:%M %p").dt.round("H").dt.hour
result["weather"] = boston["weatherDesc"].apply(lambda x: x[12:-3])
result.to_csv('bosFinal.csv', index = False)