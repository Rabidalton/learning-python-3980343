# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

# class vehicle:
#   def __init__(self, typeOfVehicle):
#     self.typeOfVehicle = typeOfVehicle

#   def drive(self, speed, distance):
#     self.mode = "Driving"
#     self.speed = speed
#     self.distance = distance

# class car(vehicle):
#   def __init__(self, engineType):
#     super().__init__("Car")
#     self.engine = engineType
#     self.wheels = 4
#     self.tyres = 4
#     self.door = 2
  
#   def drive(self, speed, distance):
#     super().drive(speed, distance)
#     print(self.mode, self.engine, " car at ", self.speed, " on a distance of ", self.distance)

# class motorcycle(vehicle):
#   def __init__(self, engineType, isatricycle):
#     super().__init__("motorbike")
#     if(isatricycle):
#       self.tyres = 3
#       self.carrier = 1
#     else:
#       self.tyres = 2
#       self.carrier = 0
#     self.engine = engineType

#   def drive(self, speed, distance):
#     super().drive(speed, distance)
#     print(self.mode, self.engine, " my motorcycle", "at", self.speed, " of a distance of ", self.distance)

# car1 = car("gas")
# car2 = car("electric")
# mc1 = motorcycle("gas", True)

# print(mc1.engine)
# print(car1.engine)
# print(mc1.tyres)
# print(car2.door)
# print(mc1.carrier)

# car1.drive("30km/h", "100 miles")
# car2.drive("50km/h", "150 miles")
# mc1.drive("40km/h", "120 miles")


#Creating my own class from scratch

class realestate:
  def __init__(self, realestatetype):
    self.estatetype = realestatetype

  def searchestate(self, type, location, amount):
    self.action = "I am searching for a"
    self.type = type
    self.location = location
    self.amount = amount

class house(realestate):
  def __init__(self, floorType):
    super().__init__("house")
    self.rooms = 6
    self.livingroom = 1
    self.kitchen = 1
    self.bathroom = 4
    self.floortype = floorType

  def searchestate(self, type, location, amount):
    super().searchestate(type, location, amount)
    print(self.action, self.floortype, self.type, "located at", self.location, "that costs", self.amount)

class hotel(realestate):
  def __init__(self, floorType):
    super().__init__("hotel")
    self.rooms = 20
    self.livingroom = 0
    self.kitchen = 0
    self.bathroom = 20
    self.floortype = floorType

  def searchestate(self, type, location, amount):
    super().searchestate(type, location, amount)
    print(self.action, self.floortype, self.type, "located at", self.location, "that costs", self.amount)

class appartment(realestate):
  def __init__(self, floorType):
    super().__init__("house")
    self.rooms = 2
    self.livingroom = 1
    self.kitchen = 1
    self.bathroom = 2
    self.floortype = floorType

  def searchestate(self, type, location, amount):
    super().searchestate(type, location, amount)
    print(self.action, self.floortype, self.type, "located at", self.location, "that costs", self.amount)

house1 = house("upstairs")
house2 = house("single-floor")
hotel1 = hotel("upstairs")
hotel2 = hotel("single-floor")
appartment1 = appartment("upstairs")
appartment2 = appartment("single-floor")

# print("rooms:",house1.rooms, "kitchen:",house1.kitchen, "bathroom:",house1.bathroom, house1.livingroom, house1.floortype)
# print("rooms:",house2.rooms, "kitchen:",house2.kitchen, "bathroom:",house2.bathroom, house2.livingroom, house2.floortype)
# print("rooms:",appartment1.rooms, "kitchen:",appartment1.kitchen, "bathroom:",appartment1.bathroom, appartment1.livingroom, appartment1.floortype)
# print("rooms:",appartment2.rooms, "kitchen:",appartment2.kitchen, "bathroom:",appartment2.bathroom, appartment2.livingroom, appartment2.floortype)
# print("rooms:",hotel1.rooms, "kitchen:",hotel1.kitchen, "bathroom:",hotel1.bathroom, hotel1.livingroom, hotel1.floortype)
# print("rooms:",hotel2.rooms, "kitchen:",hotel2.kitchen, "bathroom:",hotel2.bathroom, hotel2.livingroom, hotel2.floortype)

hotel2.searchestate("hotel", "16th Street", "$75")
house1.searchestate("house", "Caldwell", "$500")
appartment1.searchestate("appartment", "Rehab", "$150")

