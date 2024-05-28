from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i in range(0, len(header_row)):
    if header_row[i] == 'latitude':
        lat_index = i
    elif header_row[i] == 'longitude':
        long_index = i
    elif header_row[i] == 'brightness':
        bright_index = i

latitudes, longitudes, brightness = [], [], []

for row in reader:

    try:
        lat = float(row[lat_index])
        long = float(row[long_index])
        bright = float(row[bright_index])

    except:
        continue

    else:
        latitudes.append(lat)
        longitudes.append(long)
        brightness.append(bright)

title = 'Global Fires'
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightness, title=title,
                     color = brightness,
                     color_continuous_scale='hot',
                     labels={'color': 'Brightness'},
                     projection='natural earth',
                     )

fig.show()
