class SuperVehicles: 
   def __init__(self, name: str, mpg: int): 
      self.name = name 
      self.mpg = mpg

   def fuel_needed(self, distance: float): 
      return (distance / self.mpg)
   
   def description(self): 
      return f"{self.name} gets {self.mpg} miles per gallon."

Car = SuperVehicles("Car", 30)

Truck = SuperVehicles("Truck", 15)

Motorcycle = SuperVehicles("Motorcycle", 50)

Bus = SuperVehicles("Bus", 8)




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 