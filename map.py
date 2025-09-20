import csv
import os
from flask import render_template
import folium
from folium import IFrame

def create_map_almacenes(almacenes):
    # Centro del mapa: promedio de almacenes o default Oaxaca
    if almacenes:
        avg_lat = sum(float(a['latitud']) for a in almacenes if a['latitud']) / len([a for a in almacenes if a['latitud']])
        avg_lon = sum(float(a['longitud']) for a in almacenes if a['longitud']) / len([a for a in almacenes if a['longitud']])
        map_center = [avg_lat, avg_lon]
    else:
        map_center = [17.0654, -96.7237]  # Oaxaca centro

    m = folium.Map(location=map_center, zoom_start=8, tiles='openstreetmap')
    m._name = 'mapa'
    m._id = 'almacenes'

    min_lat = 900
    max_lat = -900
    min_lon = 900
    max_lon = -900

    for a in almacenes:
        marker_data = {'almacen': a.get('almacen', ''),
                       'direccion': a.get('direccion', ''),
                       'latitud': a.get('latitud', ''),
                       'longitud': a.get('longitud', ''),
                       'nota': a.get('nota', '')}

        if float(a['latitud']) < min_lat:
            min_lat = float(a['latitud'])
        if float(a['latitud']) > max_lat:
            max_lat = float(a['latitud'])
        if float(a['longitud']) < min_lon:
            min_lon = float(a['longitud'])
        if float(a['longitud']) > max_lon:
            max_lon = float(a['longitud'])
        if a['latitud'] and a['longitud']:
            popup_html = render_template(
                'popup.html',
                **marker_data
            )
            folium.Marker(
                location=[float(a['latitud']), float(a['longitud'])],
                popup=folium.Popup(html=popup_html, max_width=320),
                icon=folium.Icon(color='darkred', icon='warehouse', prefix='fa'),
                tooltip=a.get('almacen', '')
            ).add_to(m)

    # Ajustar el zoom para que todos los marcadores sean visibles
    m.fit_bounds([
        [min_lat, min_lon],
        [max_lat, max_lon]
    ])

    # Título fijo como overlay usando plantilla
    titulo_html = render_template('titulo_mapa.html')
    m.get_root().html.add_child(folium.Element(titulo_html))

    # cargar script desde static
    js_code = open('static/main.js', 'r').read()
    m.get_root().script.add_child(folium.Element(js_code))

    return m

def obtener_almacenes(csv_path, q=None):
    almacenes = []
    with open(csv_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['direccion'] or (row['latitud'] and row['longitud']):
                if q:
                    if q in row['almacen'].lower() or q in row['direccion'].lower():
                        almacenes.append(row)
                else:
                    almacenes.append(row)
    return almacenes

def mapa_almacenes(q=None):
    base_path = os.path.dirname(os.path.abspath(__file__))
    almacenes = obtener_almacenes(os.path.join(base_path, 'data', 'almacenes.csv'), q)
    m = create_map_almacenes(almacenes)
    return m
