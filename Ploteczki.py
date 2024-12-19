import plotly.graph_objs as go
import numpy as np

# WspĂłĹrzÄdne lotnisk (Warszawa i Nowy Jork)
lotniska = {
    'Warszawa': (52.2297, 21.0122, 0),
    'Nowy Jork': (40.7128, -74.0060, 0)
}

# WspĂłĹrzÄdne lotu (linia ĹÄczÄca WarszawÄ i Nowy Jork)
trasa_lotu = [(52.2297, 21.0122, 0), (40.7128, -74.0060, 0)]

# Wygenerowanie 10 punktĂłw poĹrednich na trasie lotu (zmiana wysokoĹci)
zmiana_wysokosci = np.linspace(0, 10000, num=10)
punkty_posrednie = [(trasa_lotu[0][0], trasa_lotu[0][1], h) for h in zmiana_wysokosci]
punkty_posrednie.append(trasa_lotu[1])  # Dodanie ostatniego punktu koĹcowego

# Przygotowanie gradientu kolorĂłw
gradient_kolorow = np.linspace(0, 1, len(punkty_posrednie))

# Tworzenie polilinii reprezentujÄcej trasÄ lotu
polilinia_trasy = go.Scatter3d(x=[coord[1] for coord in punkty_posrednie],  # WspĂłĹrzÄdna x (dĹugoĹÄ geograficzna)
                               y=[coord[0] for coord in punkty_posrednie],  # WspĂłĹrzÄdna y (szerokoĹÄ geograficzna)
                               z=[coord[2] for coord in punkty_posrednie],  # WspĂłĹrzÄdna z (wysokoĹÄ)
                               mode='lines',
                               line=dict(color=gradient_kolorow, width=5, colorscale='Viridis'),
                               name='Trasa lotu')

# Tworzenie punktĂłw reprezentujÄcych lotniska
trace_lotniska = go.Scatter3d(x=[coord[1] for coord in lotniska.values()],  # WspĂłĹrzÄdna x (dĹugoĹÄ geograficzna)
                              y=[coord[0] for coord in lotniska.values()],  # WspĂłĹrzÄdna y (szerokoĹÄ geograficzna)
                              z=[coord[2] for coord in lotniska.values()],  # WspĂłĹrzÄdna z (wysokoĹÄ)
                              mode='markers',
                              marker=dict(color='blue', size=10),
                              name='Lotniska')

# WspĂłĹrzÄdne granic Polski do narysowania na osi x
granice_polski = {
    'PĂłĹnoc': (54.9, 14.1),  # Granica pĂłĹnocna
    'PoĹudnie': (49.0, 14.1),  # Granica poĹudniowa
    'WschĂłd': (54.9, 24.2),  # Granica wschodnia
    'ZachĂłd': (54.9, 14.1)  # Granica zachodnia
}

# Tworzenie polilinii reprezentujÄcej granice Polski
polilinia_polski = go.Scatter3d(x=[granica[1] for granica in granice_polski.values()],  # WspĂłĹrzÄdna x (dĹugoĹÄ geograficzna)
                                y=[granica[0] for granica in granice_polski.values()],  # WspĂłĹrzÄdna y (szerokoĹÄ geograficzna)
                                z=[0] * len(granice_polski),  # WspĂłĹrzÄdna z (wysokoĹÄ)
                                mode='lines',
                                line=dict(color='black', width=2),
                                name='Granice Polski')

# Tworzenie layoutu
layout = go.Layout(scene=dict(xaxis=dict(title='Mapa', showgrid=False),  # OĹ x (mapa)
                               yaxis=dict(title='SzerokoĹÄ geograficzna'),  # OĹ y (szerokoĹÄ geograficzna)
                               zaxis=dict(title='WysokoĹÄ geograficzna')),  # OĹ z (wysokoĹÄ geograficzna)
                   title='Trasa lotu miÄdzy WarszawÄ a Nowym Jorkiem')

# Tworzenie figury
fig = go.Figure(data=[polilinia_trasy, trace_lotniska, polilinia_polski], layout=layout)

# WyĹwietlanie wizualizacji
fig.show()