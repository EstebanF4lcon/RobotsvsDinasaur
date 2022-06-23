from robot import robot



class Dinosaur :
    def __init__(self,attack_power): 
        self. name ="Triceratops"
        self.attack_power = attack_power 
        self.health = 125
    

    

    def attack(self,robot ):
      robot.health -= self.attack_power
      print(f"{self.name} attacks {robot.name} for {self.attack_power} damage. Their new health is {robot.health}.")
   