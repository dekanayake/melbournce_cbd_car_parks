from flask import Flask, url_for
from rest.service.parkingBayService import ParkingBayService

app = Flask(__name__)


def __init__(self):
    self.parking_bay_service = ParkingBayService()

@app.route('/available/<longitude>/<lattitude>')
def getAvailableParkingSlots():
    return self.parking_bay_service

