import folium
from folium.plugins import HeatMap, MarkerCluster
import numpy as np

# Ustawienia poczÄtkowe mapy
location = [51.11008399314229, 17.066876386172535]  # Lokalizacja centrum - Warszawa
m = folium.Map(location=location, zoom_start=12, tiles='CartoDB positron')

# Dodawanie MarkerCluster - grupuje markery w klastry
marker_cluster = MarkerCluster().add_to(m)

# Dodawanie punktĂłw interaktywnych
for point in range(10):  # Generowanie 10 przykĹadowych punktĂłw
    folium.Marker(location=[52.2297 + np.random.uniform(-0.01, 0.01), 21.0122 + np.random.uniform(-0.01, 0.01)],
                  popup=f'Punkt {point+1}',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)

# Dodawanie warstwy cieplnej


# Dodawanie tras
folium.PolyLine(locations=[(51.11008399314229, 17.066876386172535), (50.816401595588566, 19.158270003862512), (50.263958418381364, 19.053349004969146), (50.06490277125615, 19.97391705840834), (52.22388704620884, 21.073377899135448), (53.1707500563181, 23.140114280601754), (54.34019017618809, 18.652913210216187), (53.422102713242516, 14.601054181510932), (52.73280139427859, 15.213284879329967), (52.42448624275443, 16.868490343314438), (53.149424330913675, 18.096602136448265), (51.79001232554983, 19.477413879700155), (50.665210569202216, 17.921335800547674), (50.07289591114158, 22.028815509321678), (51.28864794399777, 22.650296050789326), (50.884557107729194, 20.65211291932148), (53.7958063975562, 20.470206338170254)],
                color="blue", weight=5, opacity=0.7).add_to(m)

folium.Marker(location=[51.11008399314229, 17.066876386172535],
                  popup=f'Wroclaw',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)

folium.Circle(location=(51.11008399314229, 17.066876386172535), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)

folium.Marker(location=[50.816401595588566, 19.158270003862512],
                  popup=f'Czestochowa',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)

folium.Circle(location=(50.816401595588566, 19.158270003862512), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)

folium.Marker(location=[50.263958418381364, 19.053349004969146],
                  popup=f'Katowice',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(50.263958418381364, 19.053349004969146), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[50.06490277125615, 19.97391705840834],
                  popup=f'Kraków',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(50.06490277125615, 19.97391705840834), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[52.22388704620884, 21.073377899135448],
                  popup=f'Warszawa',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(52.22388704620884, 21.073377899135448), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[53.1707500563181, 23.140114280601754],
                  popup=f'Białystok',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(53.1707500563181, 23.140114280601754), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[54.34019017618809, 18.652913210216187],
                  popup=f'Gdansk',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(54.34019017618809, 18.652913210216187), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[53.422102713242516, 14.601054181510932],
                  popup=f'Szczecin',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(53.422102713242516, 14.601054181510932), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[52.73280139427859, 15.213284879329967],
                  popup=f'Gorzow',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(52.73280139427859, 15.213284879329967), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[52.42448624275443, 16.868490343314438],
                  popup=f'Poznań',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(52.42448624275443, 16.868490343314438), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[53.149424330913675, 18.096602136448265],
                  popup=f'Bydgoszcz',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(53.149424330913675, 18.096602136448265), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[50.665210569202216, 17.921335800547674],
                  popup=f'Opole',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(50.665210569202216, 17.921335800547674), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[51.28864794399777, 22.650296050789326],
                  popup=f'Lublin',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(51.28864794399777, 22.650296050789326), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[50.884557107729194, 20.65211291932148],
                  popup=f'Kielce',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(50.884557107729194, 20.65211291932148), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[53.7958063975562, 20.470206338170254],
                  popup=f'Olsztyn',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(53.7958063975562, 20.470206338170254), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[50.07289591114158, 22.028815509321678],
                  popup=f'Rzeszow',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(50.07289591114158, 22.028815509321678), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


folium.Marker(location=[51.79001232554983, 19.477413879700155],
                  popup=f'Lodz',
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)
folium.Circle(location=(51.79001232554983, 19.477413879700155), radius=10000,
              color='green', fill=True, fill_opacity=0.2,
              popup='PrzykĹadowy obszar').add_to(m)


# Dodawanie obszarĂłw
# folium.Circle(location=(51.11008399314229, 17.066876386172535), radius=300,
#              color='green', fill=True, fill_opacity=0.2,
 #             popup='PrzykĹadowy obszar').add_to(m)

# Zapisywanie mapy do pliku HTML
m.save('zaawansowana_mapa.html')