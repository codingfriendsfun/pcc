from pathlib import Path
import csv

from datetime import datetime


path = Path('weather_data/san_fran_2021_simple.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.

sf_dates, sf_highs, sf_lows = [], [], []

for row in reader:

    date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[6])
        low = int(row[7])

    except:
        print(f"Missing data for {date}")

    else:
        sf_dates.append(date)
        sf_highs.append(high)
        sf_lows.append(low)
