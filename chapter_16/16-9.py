import json
import csv
from pathlib import Path

import plotly.express as px


# Read data as string; convert to Python object
path = Path('chapter_16/world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract latitude, longitude, brightness
lats, longs, brightness = [], [], []
for row in reader:
    lats.append(float(row[0]))
    longs.append(float(row[1]))
    brightness.append(float(row[2]))

title = "World Fires"
fig = px.scatter_geo(lat=lats, lon=longs, size=brightness, title=title,
                     color=brightness,
                     color_continuous_scale='Reds',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     )
fig.show()