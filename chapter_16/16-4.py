from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Get indexes

for i in range(0, len(header_row)):
    if header_row[i] == 'TMAX':
        tmax = i
    elif header_row[i] == 'TMIN':
        tmin = i
    elif header_row[i] == 'NAME':
        name_index = i

# Extract PRCP values.

dates, highs, lows = [], [], []

for row in reader:
    
    name = row[name_index]
    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[tmax])
        low = int(row[tmin])

    except:
        pass

    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs)
ax.plot(dates, lows)

# Format plot.
title = f'{name} Temperature Data'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()

ax.set_ylabel(f'Rainfall', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
