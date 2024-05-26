from pathlib import Path
import csv

from datetime import datetime


path = Path('weather_data/death_valley_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.

dv_dates, dv_highs, dv_lows = [], [], []

for row in reader:

    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[3])
        low = int(row[4])

    except:
        print(f"Missing data for {date}")

    else:
        dv_dates.append(date)
        dv_highs.append(high)
        dv_lows.append(low)
