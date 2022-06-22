
from weapon import Weapon


class Robot:
    def __init__(self,name):
        self. name ="Frankitty 100"
        self.health = [150]
        self. active_weapon = Weapon("Sniper", [30])


    def attack (self, dinosaur ):
      dinosaur.health -= self.weapon.attack_power
      print(f"{self.name} attacks {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage. New health is {dinosaur.health}.")