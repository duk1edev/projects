class Car:

    def __init__(self,model,price):
        self.model = model
        self.price = price

class Store(object):

    

    def __init__(self, cars_list=[]):
        self.cars = cars_list
    

    def show_cars(self):
        """Show all cars in the store
        """
        for i in self.cars: 
            print("{0} = {1}".format((i),(self.cars)))
    #def sell_car(self):
    def __str__(self):
        
        return ("Model : {0} , Price: {}".format(self.) 

         
   
        
def main():
    car1 = Car("AudiQ6)",45000)
    car2 = Car("MercedesBenz E350",250000)

    store = Store()
    store.cars = [car1,car2]
    store.show_cars()

if __name__ == '__main__':
    main()


