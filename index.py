from flask import Flask, render_template_string,url_for,render_template
import folium
import json
import geopandas as gpd
import pandas as pd
from branca.colormap import linear
from branca.element import Template, MacroElement

# create a flask application
app = Flask(__name__)

f = open('shpasjson.geojson', encoding="utf8")
geo_json_data = json.load(f)
geo_data = pd.read_csv("countries.csv")

a,b,c = geo_data["points"].quantile([0.25,0.5,0.75])
geo_data = None

def mappy(feature):
    try:
        x = feature["properties"]["POINTS"]
        if x > c:
            return "#36FF00"
        elif x > b:
            return "#FFC500"
        elif x > a:
            return "#FF2D00"
        elif x < a:
            return "#00C9FF"
    except:
        return None

@app.route("/")
def home():
    """Create a map object"""
    mapObj = folium.Map(location=[33.979643, -117.332125],zoom_start=2,width=1000, height=500)

    popup = folium.GeoJsonPopup(fields=["ADMIN","POINTS"],aliases=["Name:","Points:"])

    folium.GeoJson(geo_json_data,name="Heatmap",style_function=lambda feature: {
            "fillColor": mappy(feature),
            "color": "black",
            "weight": 1,
            "dashArray": "5, 5",
            "fillOpacity": 0.2      
    },
    popup=popup
    ).add_to(mapObj)

    folium.LayerControl().add_to(mapObj)

    # render the map object
    mapObj.get_root().render()

    # derive the script and style tags to be rendered in HTML head
    header = mapObj.get_root().header.render()

    # derive the div container to be rendered in the HTML body
    body_html = mapObj.get_root().html.render()

    # derive the JavaScript to be rendered in the HTML body
    script = mapObj.get_root().script.render()

    return render_template(
        "index.html",
        header=header,
        body_html=body_html,
        script=script,
        a=a,
        b=b,
        c=c
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)