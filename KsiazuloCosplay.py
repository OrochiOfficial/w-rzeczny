import folium

location_Mac = [50.9081719138793, 15.73685337396408]
location_KANS = [50.914402651583536, 15.730024250869935]
m = folium.Map(location=location_Mac, zoom_start=12)

folium.TileLayer('Stamen Terrain', attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.').add_to(m)

# m = folium.Map(location=location_Mac, zoom_start=12, tiles='StamenToner', attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.')

folium.LayerControl().add_to(m)

icon_image = "path856.png"
folium.Marker(location=location_Mac, icon=folium.Icon(icon="fa-solid fa-utensils", prefix='fa')).add_to(m)
folium.Marker(location=location_KANS, icon=folium.Icon(icon="fa-solid fa-thumbs-up", prefix='fa')).add_to(m)

m.save('zaawansowana_mapa.html')

# Map data @ OpenStreetmap contributions