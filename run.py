import pandas as pd
# import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

def epochms_to_hour(stamp):
    time = dt.datetime.fromtimestamp(stamp / 1000)
    return time.hour

df = pd.read_csv("data/10.csv", sep=",", index_col="timestamp_utc")
df["hour"] = df["timestamp"].apply(epochms_to_hour)

plt.hist(df["hour"], bins=24, density=True)
plt.title("Die WLAN-Events über den Tag verteilt")
plt.xlabel("Stunde")
plt.ylabel("Anteil pro Stunde")
plt.show()
