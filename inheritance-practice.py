# When you override the constructor, the constructor from the parent class (from which we inherited) is not called at all. If you still want that functionality, you have to call it yourself. This is done with super(): it returns a reference to the parent class, so we can call the constructor of the parent class.

# In this case, we added functionality for the center stand but removed the option to set the speed and started state in the constructor. If you want, you can add options for speed and started state too and pass those on to the Vehicle constructor.

class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")


class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        trunk_open = True

    def close_trunk(self):
        trunk_open = False


class Motorcycle(Vehicle):
    def __init__(self, center_stand_out=False):
        self.center_stand_out = center_stand_out

        super().__init__(True, 10)


car = Car()

moto = Motorcycle()

print(moto.started)
