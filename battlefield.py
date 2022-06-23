from dinosaur import Dinosaur
from robot import robot


class Battlefield:
   def __init__ (self):
      self.robot = robot()
      self.dinosaur = Dinosaur(30) 
        
   def run_game (self):
      self.display_welcome()
      self.battle_phase()
      self.display_winner() 
   def display_welcome(self):
      print('Welcome to the battlefield Good Luck there is only one way out!')

   def battle_phase (self):
      while self.robot.health> 0 and self.dinosaur.health> 0:
         self.dinosaur.attack(self.robot)
         if self.robot.health > 0:
            self.robot.attack(self.dinosaur)
   def display_winner(self):
      if self.robot.health > 0 :
         print("Robots win!")
      elif self.dinosaur.health > 0 :
         print("Dinosaurs win!")
      else:
         print("")