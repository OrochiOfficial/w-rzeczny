import folium
from folium.plugins import HeatMap, MarkerCluster
import numpy as np

location = [52.26555163927304, 20.995670226479277]
m = folium.Map(location=location, zoom_start=12, tiles='CartoDB positron')

marker_cluster = MarkerCluster().add_to(m)

#folium.PolyLine(locations=[(52.26555163927304, 20.995670226479277),         #1
#                           (-34.65046071794412, -58.43950114758784),        #2
#                           (-33.923198173886746, 18.417391440082874),       #3
#                           (55.76248837742747, 37.64094589325472),          #4
#                           (40.71252422659164, -73.99487095157382),         #5
#                           (52.26555163927304, 20.995670226479277)],        
#                color="blue", weight=5, opacity=0.7).add_to(m)

folium.PolyLine(locations=[(52.26555163927304, 20.995670226479277),         
                           (-34.65046071794412, -58.43950114758784)],
                color="red", weight=5, opacity=0.7).add_to(m)

folium.PolyLine(locations=[(52.26555163927304, 20.995670226479277),
                           (55.76248837742747, 37.64094589325472)],
                color="red", weight=5, opacity=0.7).add_to(m)

folium.PolyLine(locations=[(55.76248837742747, 37.64094589325472),
                           (40.71252422659164, -73.99487095157382)],
                color="red", weight=5, opacity=0.7).add_to(m)

folium.PolyLine(locations=[(40.71252422659164, -73.99487095157382),
                           (-33.923198173886746, 18.417391440082874)],
                color="red", weight=5, opacity=0.7).add_to(m)


folium.Marker(location=[52.26555163927304, 20.995670226479277],
                  popup=f'Wielopierścieniowe Węglowodory Aromatyczne',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(52.26555163927304, 20.995670226479277), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='Wielopierścieniowe Węglowodory Aromatyczne').add_to(m)

folium.Marker(location=[-34.65046071794412, -58.43950114758784],
                  popup=f'Kinder Bueno',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(-34.65046071794412, -58.43950114758784), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='Kinder Bueno').add_to(m)

folium.Marker(location=[-33.923198173886746, 18.417391440082874],
                  popup=f'Cape Village',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(-33.923198173886746, 18.417391440082874), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='Cape Village').add_to(m)

folium.Marker(location=[55.76248837742747, 37.64094589325472],
                  popup=f'Stolica ZSRR',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(55.76248837742747, 37.64094589325472), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='Stolica ZSRR').add_to(m)

folium.Marker(location=[40.71252422659164, -73.99487095157382],
                  popup=f'Stary Husky',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(40.71252422659164, -73.99487095157382), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='Stary Husky').add_to(m)

m.save('zaawansowana_mapa.html')