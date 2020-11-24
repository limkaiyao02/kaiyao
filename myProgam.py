#3
class Vehicle:
    engine_capacity = "1,6 Turbo"

#4
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

#5
vios = Vehicle ('4','petrol',5,180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

#6
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")

#7
class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

#8
blueSG = ElectricCar ('4', 5, 150)
blueSG.drive()

#10
class Computer:
    def __init__(self, type_of_computer, color_of_pc, price_of_pc, brand_of_pc):
        self.type_of_computer = type_of_computer
        self.color_of_pc = color_of_pc
        self.price_of_pc = price_of_pc
        self.brand_of_pc = brand_of_pc

    def playGame(self,game):
        print("The name of the game is",game)

laptop = Computer('laptop','Rose Gold',1300,'Asus')
print(laptop.type_of_computer)
print(laptop.color_of_pc)
print(laptop.price_of_pc)
print(laptop.brand_of_pc)

laptop.playGame("Valorant")

class laptop1(Computer):
    def __init__(self,color_of_pc, price_of_pc, brand_of_pc):
        Computer.__init__(self,'laptop',color_of_pc,price_of_pc,brand_of_pc)

Mac = laptop1('Silver Grey', '1600', 'Mac')
print(Mac.type_of_computer)
print(Mac.color_of_pc)
print(Mac.price_of_pc)
print(Mac.brand_of_pc)
Mac.playGame("Mobile Leagues")

class desktop1(Computer):
    def __init__(self,color_of_pc, price_of_pc, brand_of_pc):
        Computer.__init__(self,'desktop',color_of_pc,price_of_pc,brand_of_pc)

Dell = desktop1('silver', 2400,'Dell')
print(Dell.type_of_computer)
print(Dell.color_of_pc)
print(Dell.price_of_pc)
print(Dell.brand_of_pc)
Dell.playGame("League of Legends")
