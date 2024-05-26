from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.

s_dates, s_highs, s_lows = [], [], []

for row in reader:

    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[4])
        low = int(row[5])

    except:
        print(f"Missing data for {date}")

    else:
        s_dates.append(date)
        s_highs.append(high)
        s_lows.append(low)
