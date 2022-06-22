from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

   def ___init___ (self):
     self.robot = Robot()
     self.dinosaur = Dinosaur() 
        
   def run_game (self):
    self.display_welcome()
    self.battle_phase()
    self.display_winner() 
   def display_welcome(self):
    print('Welcome to the battlefield Good Luck there is only one way out!')

   def battle_phase (self):
    while len(self.Robot) > 0 and len(self.Dinosaur) > 0:
         self.Dinosaur_turn()
      if len(self.Robots) > 0:
         self.Robot_turn()
   def display_winner(self):
        if len(self.Robots) > 0:
            print("Robots win!")
        if self.Robot_turn():
         print("Dinosaurs win!")
        else:
         print