import csv
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather(path, high_row, low_row, location):
    """Obtain weather data from specified path"""
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates, high and low temps
    for row in reader: 
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[high_row])
            low = int(row[low_row])
        except ValueError:
            print(f"Missing data for {current_date} at {location}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

# Set up graph
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Plot for Sitka, AK
path = Path('chapter_16/sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather(path, 4, 5, "Sitka")
ax.plot(dates, highs, color='red', alpha=1)
ax.plot(dates, lows, color='blue', alpha=1)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.25)

# Plot for Death Valley, CA
path = Path('chapter_16/death_valley_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather(path, 3, 4, "Death Valley")
ax.plot(dates, highs, color='red', alpha=.5)
ax.plot(dates, lows, color='blue', alpha=.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "High and Low Temperatures In Sitka, AK, and Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
