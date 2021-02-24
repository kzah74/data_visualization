import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='blue')

plt.title("Amount of rainfalls in Sitka for December 2020")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Amount of rainfalls.", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()