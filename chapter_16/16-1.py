from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract PRCP values.

dates, prcps = [], []

for row in reader:

    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        prcp = float(row[5])

    except:
        print(f"Missing data for {date}")

    else:
        dates.append(date)
        prcps.append(prcp)


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, prcps)

# Format plot.
title = 'Daily Rainfall in Sitka'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()

ax.set_ylabel(f'Rainfall', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
