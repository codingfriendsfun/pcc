from pathlib import Path
import json

import plotly.express as px


# Read data as string; convert to Python object
path = Path('chapter_16/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all quakes
all_eq_dicts = all_eq_data['features']

mags, longs, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    longs.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title = (all_eq_data['metadata']['title'])
fig = px.scatter_geo(lat=lats, lon=longs, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Turbo',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
