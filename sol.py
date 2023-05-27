from solara import *
import ipyleaflet
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="myapp")

@solara.component
def Page():
    findlocation = use_reactive("")

    url = ipyleaflet.basemaps.OpenStreetMap.Mapnik['url']

    # CREATE MARKER
    marker = ipyleaflet.Marker(
        element_name="marker",
        location=(52,10),
        # FOR DRAG MARKER USE THIS CODE
        draggable=True
        )
    def showlocation():
        # AND NOW CHANGE MARKER IF YOU FIND CITY
        locator = geolocator.geocode(findlocation.value)
        if locator is not None:
            lat = locator.latitude
            lon = locator.longitude
            print(lat,lon)
            # AND CHANGE MARKER HERE
            marker.location=(lat,lon)


    with Column(margin=10):
        with Row(justify="center"):
            InputText(label="find city here",
                value=findlocation
                )
            Button("search",
                on_click=showlocation,
                color="primary"
                )
        # CREATE MAPS HERE
        ipyleaflet.Map.element(
            zoom=5,
            center=marker.location,
            scroll_wheel_zoom=True,
            layers=[
            # FOR CREATE TILE THEME
            ipyleaflet.TileLayer.element(url=url),
            marker 
            ]
            )


