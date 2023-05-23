class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine started.")
    
    def stop(self):
        print("Engine stopped.")
    
    def get_horsepower(self):
        return self.horsepower

class Wheel:
    def __init__(self, size):
        self.size = size
    
    def roll(self):
        print("Wheel rolling.")
    
    def get_size(self):
        return self.size

class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels
    
    def start(self):
        print("Starting car...")
        self.engine.start()
        for wheel in self.wheels:
            wheel.roll()
        print("Car started.")
    
    def stop(self):
        print("Stopping car...")
        self.engine.stop()
        print("Car stopped.")
    
    def get_horsepower(self):
        return self.engine.get_horsepower()
    
    def get_wheel_sizes(self):
        return [wheel.get_size() for wheel in self.wheels]

# Example usage
engine = Engine(200)
wheels = [Wheel(18) for i in range(4)]
car = Car(engine, wheels)
car.start()
print("Horsepower:", car.get_horsepower())
print("Wheel sizes:", car.get_wheel_sizes())
car.stop()
