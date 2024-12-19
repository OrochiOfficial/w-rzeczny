import plotly.graph_objects as go
cities = {
    'New York': [40.7128, -74.0060],
    'London': [51.5074, -0.1278],
    'Paris': [48.8567, 2.3522],
    'Tokyo': [35.6895, 139.6917],
    'Dublin': [53.3498, -6.2603],
    'Moscow': [55.7558, 37.6176],
    'Berlin': [52.5200, 13.4050],
    'Rome': [41.9028, 12.4964],
}
trace = go.Scatter3d(
    x = [coord[1] for coord in cities.values()], 
    y = [coord[0] for coord in cities.values()],
    z = [0] * len(cities),
    mode = 'markers + text',
    marker = dict(
        size = 10,
        color = 'red',
        text = list(cities.keys()),
    )   
)
layout = go.Layout(
    scene = dict(
        xaxis = dict(title = 'dlugosc geo'),
        yaxis = dict(title = 'szerokosc geo'),
        zaxis = dict(title = 'wysokosc'),
        aspectmode = 'manual',
        aspectratio = dict(x = 2, y = 2, z = 1),
)
)

fig = go.Figure(data = [trace], layout = layout)
fig.show()