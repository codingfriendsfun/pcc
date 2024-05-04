from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('chapter_16/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

location_index = header_row.index("NAME")
date_index = header_row.index("DATE")
high_temp_index = header_row.index("TMAX")
low_temp_index = header_row.index("TMIN")

# Extract dates, high and low temps
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_temp_index])
        low = int(row[low_temp_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot high and low temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Format plot
place = row[location_index]
title = f"Daily High and Low Temperatures\n{place} 2021"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
