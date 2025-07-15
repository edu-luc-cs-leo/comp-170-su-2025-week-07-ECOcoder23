class SuperAles: 
    def __init__(self, name: str, abv: float):
        self.name = name 
        self.abv = abv 
    
    def alcohol_content(self, volume_in_oz): 
        return (self.abv * volume_in_oz)
    
    def description(self): 
        return f"{self.name}: {self.abv*100:.1f}% ABV"

PaleAle = SuperAles("Pale Ale", 0.055)

IPA = SuperAles("IPA", 0.065)

Stout = SuperAles("Stout", 0.07)

Porter = SuperAles("Porter", 0.06)




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 