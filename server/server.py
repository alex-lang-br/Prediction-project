from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Welcome to this app for price prediction !"


@app.route('/get_location_names')
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    location = request.form['location']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    car = int(request.form['car'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, bed, bath, car)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Flask server for Sydney price prediction")
    util.load_saved_artefacts()
    app.run()
