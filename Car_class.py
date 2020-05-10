class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.__make = make 
        self.__model = model
        self.__year = year
        self.__odometer = odometer
        self.__fuel = fuel

    def drive(self, distance):
        if distance <= self.__fuel * 10:
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
            return 'Let \'s drive'
        else:
            return 'Need more fuel, please, fill more!'

    def __add_distance(self, distance):
        self.__odometer += distance
        return self.__odometer

    def __subtract_fuel(self, distance):
        self.__fuel -= distance/10 
        return self.__fuel

car1 = Car('BMW', 'X6', 2019)
print(car1.drive(1000))







