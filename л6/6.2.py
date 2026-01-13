class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Транспортное средство: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f"Автомобиль: {self.make} {self.model}, Тип топлива: {self.fuel_type}"


# Пример использования
vehicle = Vehicle("Yamaha", "MT-07")
car1 = Car("Toyota", "Camry", "Бензин")
car2 = Car("Tesla", "Model 3", "Электричество")

print(vehicle.get_info())
print(car1.get_info())
print(car2.get_info())