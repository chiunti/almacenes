import os
from flask import Flask, render_template, send_from_directory

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
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
