import json

with open("on_street_parking_bays.json", "r") as read_file:
    data = json.load(read_file)
    data = data["features"]
    with open("data_file.json", "w") as write_file:
        for feature in data:
            json.dump(feature, write_file)
