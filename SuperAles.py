class SuperAles: 
    def __init__(self, name: str, abv: float, volume_in_oz: int):
        self.name = name 
        self.abv = abv 
        self.volume_in_oz = volume_in_oz
    
    def alcohol_content(self): 
        return (self.abv * self.volume_in_oz)
    
    def description(self): 
        return f"{self.name}: {self.abv*100:.1f}% ABV"

PaleAle = SuperAles("Pale Ale", 0.055, 12)

IPA = SuperAles("IPA", 0.065, 12)

Stout = SuperAles("Stout", 0.07, 12)

Porter = SuperAles("Porter", 0.06, 12)




















#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 