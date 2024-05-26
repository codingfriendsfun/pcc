from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

sitka_path = Path('weather_data/sitka_weather_2021_full.csv')

sitka_lines = sitka_path.read_text().splitlines()

sitka_reader = csv.reader(sitka_lines)
header_row = next(sitka_reader)

# Extract PRCP values.

sitka_dates, sitka_prcps = [], []

for row in sitka_reader:

    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        prcp = float(row[5])

    except:
        print(f"Missing data for {date}")

    else:
        sitka_dates.append(date)
        sitka_prcps.append(prcp)


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_prcps)

# Format plot.
title = 'Daily Rainfall in Sitka'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()

ax.set_ylabel(f'Rainfall', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
