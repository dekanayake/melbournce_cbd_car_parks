import requests
import json
from datetime import time,datetime
import itertools
from mongoengine import *
from functools import reduce

class ParkingRestriction(Document):
    bay_id = StringField()
    description = StringField()
    typedesc = StringField()
    day = IntField()
    startTime = DateTimeField()
    endTime = DateTimeField()
    duration = IntField()
    effectiveOnPH = BooleanField()
    disableOnly = BooleanField()
    ticket = BooleanField()
    metered = BooleanField()
    free = BooleanField()
    meta = {
        'indexes': [
            'bay_id',
            'day'
        ]
    }





def get_restricted_slots(parking_bay_restriction):
    restricted_slots = []
    for parking_restriction_number in range(1,6):
        if 'description' + str(parking_restriction_number) in parking_bay_restriction:
            restricted_slots.append((parking_bay_restriction['description' + str(parking_restriction_number)],
                                 parking_bay_restriction['fromday' + str(parking_restriction_number)],
                                 parking_bay_restriction['today' + str(parking_restriction_number)],
                                 parking_bay_restriction['starttime' + str(parking_restriction_number)],
                                 parking_bay_restriction['endtime' + str(parking_restriction_number)],
                                 parking_bay_restriction['duration' + str(parking_restriction_number)],
                                 parking_bay_restriction['typedesc' + str(parking_restriction_number)],
                                 parking_bay_restriction['effectiveonph' + str(parking_restriction_number)]))
    return restricted_slots

def parkingRestrictions_per_day(parking_bay_restriction, restricted_slot):
    fromDay =  int(restricted_slot[1])
    toDay = int(restricted_slot[2])
    if toDay == 0:
        toDay = 7
    parkingRestrictions = []
    for day in range(fromDay, toDay + 1):
        parking_restrcition = ParkingRestriction()
        parking_restrcition.bay_id = parking_bay_restriction["bayid"]
        parking_restrcition.description = restricted_slot[0]
        parking_restrcition.day =  day if day != 7  else 0
        parking_restrcition.startTime = datetime.strptime(restricted_slot[3], '%H:%M:%S')
        parking_restrcition.endTime = datetime.strptime(restricted_slot[4], '%H:%M:%S')
        parking_restrcition.duration = int(restricted_slot[5])
        parking_restrcition.typedesc = restricted_slot[6]
        parking_restrcition.effectiveOnPH = bool(restricted_slot[7])
        parking_restrcition.disableOnly = restricted_slot[6] == "Disabled Only"
        parking_restrcition.ticket =  "Ticket" in restricted_slot[6]
        parking_restrcition.metered =  "Meter" in restricted_slot[6]
        parkingRestrictions.append(parking_restrcition)
    return parkingRestrictions

def free_slots(parkingRestrictios):
    free_slots = []
    for key, group in itertools.groupby(parkingRestrictios, key=lambda parkingRestiction:(parkingRestiction.bay_id,parkingRestiction.day)):
        free_slots.append(create_free_slots(key[0],key[1],list(group)))
    return reduce(list.__add__,free_slots)


def create_free_slots(bayId, day, parkdingRestrictionsList):
    hours_in_day = (datetime(1900,1,1,0, 00,00), datetime(1900,1,1,23,59,00))
    reserved_slots = []
    free_slots = []
    for parkingRestiction in parkdingRestrictionsList:
        reserved_slots.append((parkingRestiction.startTime, parkingRestiction.endTime))
        slots = sorted([(hours_in_day[0], hours_in_day[0])] + reserved_slots + [(hours_in_day[1], hours_in_day[1])])
        for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
            parking_restrcition = ParkingRestriction()
            parking_restrcition.bay_id = bayId
            parking_restrcition.day =  day
            parking_restrcition.startTime = start
            parking_restrcition.endTime = end
            parking_restrcition.free =  True
            free_slots.append(parking_restrcition)
    return free_slots


def convert_to_parkingRestrictions(parking_bay_restriction, restrcted_slots):
    parking_restrcitions = []
    for restricted_slot in restrcted_slots:
        parking_restrcitions.append(parkingRestrictions_per_day(parking_bay_restriction, restricted_slot))
    return reduce(list.__add__, parking_restrcitions)



url = 'https://data.melbourne.vic.gov.au/resource/ntht-5rk7.json?$limit=50000'
headers = {'X-App-Token': '2rKRf7vDTZdViV0k15XJuBBTH'}

resp = requests.get(url, headers=headers)


for parking_bay_restriction in resp.json():
    restricted_slots = get_restricted_slots(parking_bay_restriction)
    parkingRestrictions = convert_to_parkingRestrictions(parking_bay_restriction, restricted_slots)
    free_slots_list = free_slots(parkingRestrictions)
    parkingRestrictions.extend(free_slots_list)

    connect('melbourneCarpark', host='localhost', port=27017)
    for parking_restiction in parkingRestrictions:
        parking_restiction.save()
