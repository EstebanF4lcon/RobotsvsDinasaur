
from weapon import Weapon


class robot:
    def __init__(self):
        self. name ="Frankitty 100"
        self.health = 150
        self. weapon = Weapon("Sniper", 30)


    def attack (self, dinosaur ):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage. New health is {dinosaur.health}.")