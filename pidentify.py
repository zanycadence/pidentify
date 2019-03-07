from clarifai.rest import ClarifaiApp
from flask import Flask, request, jsonify

flask_app = Flask(__name__)


app = ClarifaiApp()
model = app.models.get('PiDentify')


@flask_app.route('/')
def index():
    return 'Index Page'


@flask_app.route('/hello')
def hello():
    return 'Hello, World!'


@flask_app.route('/identify_pie')
def identify_pie():
    response = model.predict_by_url(
        'https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/white-chocolate-cardamom-tart-with-raspberry-dust.jpg?itok=s_QUobYD')
    return jsonify(list(response.values()))


@flask_app.route('/identify_raspi')
def identify_raspi():
    response = model.predict_by_url(
        'https://cdn.shopify.com/s/files/1/0174/1800/products/Raspberry_Pi_Zero_W_1_of_6_large.JPG?v=1539263625'
    )
    return jsonify(list(response.values()))


@flask_app.route('/identify_pi')
def identify_pi():
    response = model.predict_by_url(
        'http://www.lightboxreg.com/eventdata/3875/5aa2d19e353a0.1520619934.1119696475_bigstock--D-Pi-Symbol-10433186.jpg'
    )
    return jsonify(list(response.values()))
