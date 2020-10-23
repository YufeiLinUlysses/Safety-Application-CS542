import pandas as pd
import datetime

boston = pd.read_csv("Boston.csv")
boston["converted"] = pd.to_datetime(
    boston['date_time'], format='%Y-%m-%d %H:%M:%S').apply(lambda x: x.date())
print(boston.groupby(["converted"]).max())
