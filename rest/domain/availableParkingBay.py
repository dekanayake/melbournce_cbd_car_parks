class AvailableParkingBay:
    
  def __init__(self, bayId, longitude, lattitude, parkingBayRestrictionDescription, parkingBayDescription):
    self.bayId = bayId
    self.longitude = longitude
    self.lattitude = lattitude
    self.parkingRestrictionDescription = parkingBayRestrictionDescription
    self.parkingBayDescription = parkingBayDescription

  def serialize(self):
    return {
      'bayId': self.bayId,
      'longitude': self.longitude,
      'lattitude': self.lattitude,
      'parkingRestrictionDescription': self.parkingRestrictionDescription,
      'parkingBayDescription': self.parkingBayDescription,
    }
