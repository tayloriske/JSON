import json

infile = open("US_fires_9_14-1.json", "r")

fdata = json.load(infile)

alist = [f for f in fdata if f["brightness"] >450]
brightness, lons, lats, = [], [], []

for f in alist:
    bright = f["brightness"]
    lon = f["longitude"]
    lat = f["latitude"]

    brightness.append(bright)
    lons.append(lon)
    lats.append(lat)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = {"type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": 25,
            "color": brightness,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"}
        }}

mylayout = Layout(title="US Fires 9/14/2020 through 9/13/2020")

fig = {"data": data, "layout": mylayout}

offline.plot(fig, filename="9_14.html")

