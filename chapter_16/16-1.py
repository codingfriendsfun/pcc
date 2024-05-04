from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('chapter_16/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and precipitation
dates, precip = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    days_precip = float(row[5])
    dates.append(current_date)
    precip.append(days_precip)

# Plot the precipitation
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, precip, color='cyan')

# Format plot
ax.set_title("Daily Precipitation in 2021\nSitka Alaska", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
