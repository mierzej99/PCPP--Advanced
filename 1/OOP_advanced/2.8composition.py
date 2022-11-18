class Tires:
    def __init__(self, size):
        self.size = size
        self.__pressure = 0


    def get_presssure(self):
        print(self.__pressure)

    def pump(self):
        self.__pressure += 1


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.__running = 0

    def start(self):
        self.__running = 1

    def stop(self):
        self.__running = 0

    def get_state(self):
        if self.__running == 1:
            print('Engine working')
        else:
            print('Engine not working')


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


city_tires = Tires(15)
offroad_tires = Tires(18)

electric_engine = Engine('electric')
petrol_engine = Engine('petrol')

city_car = Vehicle(0, electric_engine, city_tires)
all_car = Vehicle(1, petrol_engine, offroad_tires)

city_car.engine.get_state()

all_car.tires.get_presssure()