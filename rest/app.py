from flask import Flask, url_for
from service.parkingBayService import ParkingBayService
from flask.json import jsonify
import json

app = Flask(__name__)


def __init__(self):
    self.parking_bay_service = ParkingBayService()

@app.route('/available/<longitude>/<lattitude>')
def getAvailableParkingSlots(longitude, lattitude):
    parking_bay_service = ParkingBayService()
    parkingBays = parking_bay_service.getAvailableParkingBays(float(longitude), float(lattitude))
    return jsonify({'parkingBays': [parkingBay.serialize() for parkingBay in parkingBays]})

