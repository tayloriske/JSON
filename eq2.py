import json

infile = open("eq_data_30_day_m1.json", "r")
jsonfile = open("readable_eq_data.json", "w")

eqdata = json.load(infile)

json.dump(eqdata, jsonfile, indent=4)

alist = eqdata["features"]
mags, lons, lats, hover_text = [], [], [], []

for eq in alist:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    place = eq["properties"]["place"]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(place)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = {"type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_text,
        "marker": {
            "size": [5*m for m in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"}
        }}

mylayout = Layout(title="Global Earthquakes (30 days)")

fig = {"data": data, "layout": mylayout}

offline.plot(fig, filename="global_eqs_30_days.html")

