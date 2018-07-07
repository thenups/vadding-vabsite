#################################################
# Dependencies
#################################################
from flask import Flask, render_template, jsonify, redirect
from flask_cors import CORS

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)


@app.route('/check/<pwd>')
def check(pwd):
    paneer = ['saag','tandoori','masala']

    # Wedding/Reception - Saag
    # Sangeet/Wedding/Reception - Tandoori
    # Sangeet/wedding/reception/friendception - Masala

    if pwd in paneer:
        return jsonify(True)
    else:
        return jsonify(False)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
