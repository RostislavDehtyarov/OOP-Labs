from enum import Enum
from datetime import date

class CarType(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    COUPE = "Coupe"

class Person:
    def __init__(self, name: str, surname: str, birthdate: date):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.name} {self.surname}, {self.birthdate}"

class Service:
    def __init__(self, serviceName: str, price: float, serviceDate: date):
        self.serviceName = serviceName
        self.price = price
        self.serviceDate = serviceDate

    def __str__(self):
        return f"{self.serviceName} - {self.price} USD on {self.serviceDate}"

class Car:
    def __init__(self, model: str, carType: CarType, owner: Person):
        self.model = model
        self.carType = carType
        self.owner = owner
        self.services = []

    def add_service(self, service: Service):
        self.services.append(service)

    def get_total_service_cost(self):
        return sum(service.price for service in self.services)

    def full_info(self):
        services_info = "\n".join(str(service) for service in self.services)
        return (f"Model: {self.model}\nType: {self.carType.value}\nOwner: {self.owner}\n"
                f"Services:\n{services_info}\nTotal Cost: {self.get_total_service_cost()} USD")

    def short_info(self):
        return f"Model: {self.model}, Owner: {self.owner.name} {self.owner.surname}, Total Cost: {self.get_total_service_cost()} USD"

if __name__ == "__main__":
    owner = Person("John", "Doe", date(1985, 7, 15))
    car = Car("Toyota Camry", CarType.SEDAN, owner)
    service1 = Service("Oil Change", 50.0, date(2023, 6, 10))
    service2 = Service("Tire Replacement", 300.0, date(2024, 1, 20))
    car.add_service(service1)
    car.add_service(service2)
    print("Full Information:")
    print(car.full_info())
    print("\nShort Information:")
    print(car.short_info())
