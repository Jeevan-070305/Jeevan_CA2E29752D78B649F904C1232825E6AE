'''Implement a class called a player that represents a cricket player. The player class should have a method called play() which brings"The player is playing."derived two classes,batsmen and bowler,from the player class. Override the play()method in each derived class to print"The batsmen is batting" and "the bowler is bowling",respectively. Write a program to create an objects of both the batsmen and bowler classes and call the play() method for each object.'''

#define the base class player
class Player:
 def play(self):
  print("The player is playing cricket.")

#define the derived class batsmen
class Batsmen(Player):
 def play(self):
  print("the batsmen is batting.")

#define the derived class bowler
class Bowler(Player):
  def play(self):
   print("The bowler is bowling.")

#Create object of batsmen and bowler classes
batsmen=Batsmen()
bowler=Bowler()

#call the play(method for each object)
batsmen.play()
bowler.play()
