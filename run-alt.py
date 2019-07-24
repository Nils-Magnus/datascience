import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime

def mstime_to_hour(stamp):
    dt = datetime.datetime.fromtimestamp(stamp/1000)
    return int(10*float(float(dt.hour) + dt.minute / 60.0)) / 10.0

df = pd.read_csv("data/10.csv", sep=",", index_col="timestamp_utc")
df["hour"] = df["timestamp"].apply(mstime_to_hour)

plt.hist(df["hour"], bins=24*6, density=True)
plt.title("WLAN-Events über den Tag verteilt")
plt.xlabel("Stunde")
plt.ylabel("Anteil pro Stunde")
plt.show()

exit(0)

data = df[["location_x", "location_y"]]

dat_x = df.location_x
dat_y = df.location_y
dat_t = df.timestamp

dat_t.timestamp.apply(mstime_to_hour)
print(dat_t)
exit(0)

plt.hist(dat_t, bins=200)
plt.title("Histogram")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.show()

exit(0)



print("index: ", data.index)
print("columns: ", data.columns)
print(data.head())
print(data.mean())
print("min:", data.min(), "max:", data.max())
x = data.location_x
x.plot()
plt.show()




#data = (df.location_x, df.location_y)

#print(type(data))
#print(data.head())

#plt.plot([-1, -4.5, 16, 23, 15, 59])
#plt.show()
