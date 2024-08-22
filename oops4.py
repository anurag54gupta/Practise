class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
        return 6
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")  
print(car1.start())
car2.start()
print(car1.color)