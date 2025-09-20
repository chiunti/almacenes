import os
from flask import Flask, render_template, send_from_directory, request
from map import mapa_almacenes
import sys

app = Flask(__name__)


# Ruta para el favicon.ico principal (el más común que buscan los navegadores)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Rutas para los otros archivos de favicon
@app.route('/android-chrome-192x192.png')
def android_chrome_192():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'android-chrome-192x192.png', mimetype='image/png')


@app.route('/android-chrome-512x512.png')
def android_chrome_512():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'android-chrome-512x512.png', mimetype='image/png')


@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'apple-touch-icon.png', mimetype='image/png')


@app.route('/favicon-16x16.png')
def favicon_16x16():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'favicon-16x16.png', mimetype='image/png')


@app.route('/favicon-32x32.png')
def favicon_32x32():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'favicon-32x32.png', mimetype='image/png')


@app.route('/site.webmanifest')
def webmanifest():
    return send_from_directory(os.path.join(app.root_path, 'static', 'favicon'),
                               'site.webmanifest', mimetype='application/manifest+json')


@app.route('/')
def index():
    q = request.args.get('q', '').strip().lower()
    visitas_path = os.path.join(app.root_path, 'data', 'visits.txt')
    if not os.path.exists(visitas_path):
        with open(visitas_path, 'w') as f:
            f.write('0')
    with open(visitas_path, 'r+') as f:
        visitas = int(f.read() or 0) + 1
        f.seek(0)
        f.write(str(visitas))
        f.truncate()

    m = mapa_almacenes(q)
    mapa_html = m.get_root().render()
    mapa_html = m.get_root().html.render()
    header_html = m.get_root().header.render()
    script_html = m.get_root().script.render()
    return render_template('index.html',
                           header_html=header_html,
                           mapa_html=mapa_html,
                           script_html=script_html,
                           visitas=visitas,
                           busqueda=q)


@app.route('/visitas')
def visitas():
    visitas_path = os.path.join(app.root_path, 'data', 'visits.txt')
    if not os.path.exists(visitas_path):
        return {'visitas': 0}
    with open(visitas_path) as f:
        return {'visitas': int(f.read() or 0)}


if __name__ == '__main__':
    if '--debug' in sys.argv:
        app.run(host='0.0.0.0', port=8000, debug=True)
    else:
        app.run(host='0.0.0.0', port=8000)