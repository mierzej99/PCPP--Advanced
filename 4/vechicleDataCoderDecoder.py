import json


class Vehicle:

    def __init__(self, reg, year, passenger, mass):
        passenger = True if passenger == 'y' or passenger is True else False
        self.json = json.dumps(
            {"registration_number": reg, "year_of_production": year, "passenger": passenger, "mass": mass})

    def get_json(self):
        return self.json

    @staticmethod
    def get_from_json(msg):
        data = json.loads(msg)
        return Vehicle(data["registration_number"], data["year_of_production"], data["passenger"], data["mass"])


print("What can I do for you?")
msg = "1 - produce a JSON string describing a vehicle \n2 - decode a JSON string into vehicle data \nYour choice: "

step = input(msg)

if int(step) == 1:
    reg = input("Registration number: ")
    year = int(input("Year of production: "))
    passenger = input("Passenger [y/n]: ")
    mass = float(input("Vehicle mass: "))
    print(Vehicle(reg, year, passenger, mass).get_json())
else:
    msg = input("Enter Vehicle JSON string: ")
    print(Vehicle.get_from_json(msg).get_json())
