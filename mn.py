import folium
from folium.plugins import HeatMap, MarkerCluster
import numpy as np

location = [50.914, 15.727]
m = folium.Map(location=location, zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)
for point in range(10):
        folium.Marker(location=[50.914 + np.random.uniform(-0.01, 0.01), 15.727 + 
        np.random.uniform(-0.01, 0.01)],
                        popup=f'Punkt {point + 1}', 
                        icon=folium.Icon(color='red', icon='info-sign')).add_to(marker_cluster)

data = (np.random.normal(size=(1000, 2)) * 0.01 + np.array(location)).tolist()
HeatMap(data).add_to(m)

folium.PolyLine(locations=[(50.914, 15.727), (50.924, 15.749), (50.934, 15.771), (50.944, 15.793), (50.954, 15.815), (50.964, 15.837), (50.974, 15.859), (50.984, 15.881), (50.994, 15.903), (51.004, 15.925), (51.014, 15.947), (51.024, 15.969), (51.034, 15.991), (51.044, 16.013), (51.054, 16.035), (51.064, 16.057), (51.074, 16.079), (51.084, 16.101), (51.094, 16.123), (51.104, 16.145)], color = 'red', weight = 5, opacity=0.6).add_to(m)

folium.Circle(locations= [50.914, 15.727], radius=300,
              color = 'green', fill=True, fill_opacity=0.5, popup='KANS').add_to(m)

m.save('mapazobrazami.html')