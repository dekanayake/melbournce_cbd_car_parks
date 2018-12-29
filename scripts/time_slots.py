#time_slots.py
from datetime import time

appointments = [(time(7,30), time(11,00)),
                (time(12,00), time(14,00)),
                (time(15,00), time(16,00))]

hours = (time(0, 00), time(23,00))

def get_slots(hours, appointments):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    freeSlots = []
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
        print "{:%H:%M} - {:%H:%M}".format(start, end)

if __name__ == "__main__":
    get_slots(hours, appointments)
