#
class Vehicle():
    def __init__(self,wheels,weigt,doors):
        self.wheels = wheels
        self.weigt = weigt
        self.doors = doors
    def show_vehicle(self):
        print("Type: {}, Wheels: {},Weigt: {}, Doors : {}".format(type(self).__name__,self.wheels,self.weigt,self.doors))
class Car(Vehicle):
    def __init__(self, wheels, weigt,doors):
        self.weigt = weigt
        self.wheels = wheels
        self.doors = doors
class Motorbike(Vehicle):
    def __init__(self, wheels, weigt):
        self.wheels = wheels
        self.weigt = weigt
    def show_vehicle(self):
        print("Type: {0}, Wheels: {1},Weigt: {2}, {0} - dont have a doors".format(type(self).__name__,self.wheels,self.weigt))
    

class Bus(Vehicle):
    def __init__(self, wheels, weigt,doors):
        self.wheels = wheels
        self.weigt = weigt
        self.doors = doors
        

def main():
    veh = Vehicle(4,2000,8)
    veh.show_vehicle()
    print()

    car = Car(4,1500,5)
    car.show_vehicle()
    print()

    motorcircle = Motorbike(3,900)
    motorcircle.show_vehicle()
    print()

    bus = Bus(8,2500,3)
    bus.show_vehicle()




if __name__ == '__main__':
    main()