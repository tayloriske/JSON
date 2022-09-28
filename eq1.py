import json

infile = open("eq_data_1_day_m1.json", "r")
jsonfile = open("readable_eq_data.json", "w")

eqdata = json.load(infile)

json.dump(eqdata, jsonfile, indent=4)

alist = eqdata["features"]
mags, lons, lats = [], [], []

for eq in alist:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

mylayout = Layout(title="Global Earthquakes (1 day)")

fig = {"data": data, "layout": mylayout}

offline.plot(fig, filename="global_eqs_1_day.html")

