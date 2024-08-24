
# Problem 1 : Create a Car class with attributes like brand and model. Then Create an instance of this class.
# Problem 2 : Add a method to the Car class that displays the full name of the car (brand and model).
# Problem 3 : Inheritance - Create an ElectricCar class that inherits from the Car class and has an additional sttribute battery_size.
# Problem 4 : Encapsulation - Modify the Car class to encapsulate the brand attribute, make it private, provide a getter method for it.
# Problem 5 : Polymorphism - Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behavious.
# Problem 6 : Class Variable - Add a class variable to Car that keeps track of the number of cars created.
# Problem 7 : Static Method - Add a Static Method to the Car class that returns a general description of a car.
# Problem 8 : Property Decorators - Use a property decorator in the Car class to make the model attribute read-only.
# Problem 9 : Class Inheritance and isinstance() function - Demonstrate the use of isinstance() to check if my_electric1 is and instance of Car and ElectricCar.
# Problem 10 : Multiple Inheritance - Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance. 

class CarTest:
    brand = None
    model = None

my_car_test = CarTest()                  # Class storing as Object
print(my_car_test)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("MG", "Hector")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
        
my_car_old = Car("Maruti", "Ritz")
print(my_car_old.brand)
print(my_car_old.model)
print(my_car_old.full_name())

print("==============Inheritance===============")

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric1 = ElectricCar("Tesla", "Model S", "85kWH")
print(my_electric1.brand)
print(my_electric1.model)
print(my_electric1.battery_size)
print(my_electric1.full_name())

print("==============Encapsulation===============")

# Encapsulation
class CarEncap:
    def __init__(self, brand, model):
        self.__brand = brand                # Two Underscore to make it Private
        self.model = model
    
    # Getter
    def get_brand(self):
        return self.__brand + "!"
    
    # Setter - brand attribute is private. So, to modify the value you'll need set method otherwise you can't change attribute value.
    def set_brand(self, brand):
        # You can add validation logic here if needed
        if isinstance(brand, str) and brand:
            self.__brand = brand
        else:
            raise ValueError("Invalid brand name")

    def full_name(self):
        return f"{self.__brand} {self.model}"
    

my_hyundai = CarEncap("Hyundai", "IONIQ5")
#print(my_hyundai.__brand)                  # Private attribute - Not accessible
print(my_hyundai.get_brand())
print(my_hyundai.model)
print(my_hyundai.full_name())
my_hyundai.set_brand("Kia")                 # using setter to modify private attribute
print(my_hyundai.full_name())


print("==============Polymorphism===============")

# Polymorphism - Overriding / Overloading
class CarPoly:
    def __init__(self, brand, model):
        self.__brand = brand                # Two Underscore to make it Private
        self.model = model
    
    # Getter
    def get_brand(self):
        return self.__brand + "!"
    
    # Setter - brand attribute is private. So, to modify the value you'll need set method otherwise you can't change attribute value.
    def set_brand(self, brand):
        # You can add validation logic here if needed
        if isinstance(brand, str) and brand:
            self.__brand = brand
        else:
            raise ValueError("Invalid brand name")

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCarPoly(CarPoly):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"

my_porsche = CarPoly("Porsche", "911 Turbos S")
print(my_porsche.fuel_type())

my_porsche_elec = ElectricCarPoly("Porsche", "911 Taycan Turbo S", "100kWH")
print(my_porsche_elec.fuel_type())


print("==============Class Variable===============")

# Class Variable
class CarTotal:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand                # Two Underscore to make it Private
        self.model = model
        CarTotal.total_car = CarTotal.total_car + 1     # Every Object created will increase the total car value.
    
    # Getter
    def get_brand(self):
        return self.__brand + "!"
    
    # Setter - brand attribute is private. So, to modify the value you'll need set method otherwise you can't change attribute value.
    def set_brand(self, brand):
        # You can add validation logic here if needed
        if isinstance(brand, str) and brand:
            self.__brand = brand
        else:
            raise ValueError("Invalid brand name")

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


print(CarTotal.total_car)               # Accessing total_car without creating Object otherwise if you make an Object to just access the total_car then value will be 1 and not 0.


print("==============Static Method===============")

# Static Method
class CarStatic:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand                # Two Underscore to make it Private
        self.model = model
        CarTotal.total_car = CarTotal.total_car + 1     # Every Object created will increase the total car value.
    
    # Getter
    def get_brand(self):
        return self.__brand + "!"
    
    # Setter - brand attribute is private. So, to modify the value you'll need set method otherwise you can't change attribute value.
    def set_brand(self, brand):
        # You can add validation logic here if needed
        if isinstance(brand, str) and brand:
            self.__brand = brand
        else:
            raise ValueError("Invalid brand name")

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of Transport"
    
print(CarStatic.general_description())              # Accessing Static Method without creating Object


print("==============Property Decorators===============")

# Property Decorators
class CarDeco:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand                # Two Underscore to make it Private
        self.__model = model
        CarTotal.total_car = CarTotal.total_car + 1     # Every Object created will increase the total car value.
    
    # Getter
    def get_brand(self):
        return self.__brand + "!"
    
    # Setter - brand attribute is private. So, to modify the value you'll need set method otherwise you can't change attribute value.
    def set_brand(self, brand):
        # You can add validation logic here if needed
        if isinstance(brand, str) and brand:
            self.__brand = brand
        else:
            raise ValueError("Invalid brand name")

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model


my_bmw = CarDeco("BMW", "M3 Competition")
#my_bmw.model = "M4 Competition"            # You can't modify the value make it read-only
print(my_bmw.model)                         # model method - both name are same for attribute and method but now you are calling Property decorator model.

print("==============Class Inheritance and isinstance() Function===============")

# Class Inheritance and isinstance() Function
print(isinstance(my_electric1, Car))
print(isinstance(my_electric1, ElectricCar))

print("==============Multiple Inheritance===============")

# Multiple Inheritance
class Battery:
    def battery_info(self):
        return "This is Battery"


class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarMulti(Car, Battery, Engine):
    pass

my_cybertruck = ElectricCarMulti("Tesla", "Cybertruck")
print(my_cybertruck.battery_info())
print(my_cybertruck.engine_info())