class Vehicle:
    def __init__(self):
        print("Its a parent class")

class bus(Vehicle):
    def __init__(self):
        Vehicle.__init('bus')

print(issubclass(bus,Vehicle))
print(issubclass(bus,bus))
print(issubclass(bus,list))