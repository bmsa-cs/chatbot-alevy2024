"""
Chatbot
Author: Alex Levy
Period/Core: 3
"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)


name1 = input("What is your first name?\n")
name2 = input("What is your last name?\n")

print("It's nice to meet you " + name1 + " " + name2)
def week():
  global day1
  day =input("What is your favorite day of the week?\n")
  day1 = (day)
  day=day.lower()
  if day =="monday":
    mon = input("Ew. Why Monday?\n")
    if mon=="IDK":
      print("Ok nevermind then.")
    else:
      print("Strange.")
  elif day=="tuesday":
    tues = input("Oooo Taco Tuesday. Why is it your favorite?\n")
    if tues=="IDK":
      print("Ok Nevermind then.")
    else:
      print("That's a cool take on Tuesdays!")
  elif day=="wednesday":
    wed = input("Why Wednesday my dude?\n")
    if wed=="IDK":
      print("Ok nevermind then.")
    else:
      print("Wenesdays always seem to pass by so quickly.")
  elif day=="thursday":
    thurs = input("Friday Jr! Why is that one your favorite?\n")
    if thurs=="IDK":
      print("Ok Nevermind then.")
    else:
      print("Well then I hope you enjoy your next Friday Jr.")
  elif day =="friday":
    fri = input("Someone with good taste. Why is it your favorite day of the week?\n")
    if fri=="IDK":
      print("Ok nevermind then.")
    else:
      print("May I reccommend: Katy Perry's hit song \"Last Friday night?\"")
  elif day=="saturday":
    sat = input("Ahhh Saturday the day of rest. Why is it your favorite?\n")
    if sat =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you enjoy your next Saturday!")
  elif day=="sunday":
    sun = input("The sunniest of the days. Why is Sunday your favorite?\n")
    if sun =="IDK":
      print("Ok nevermind then.")
    else:
      print("Sunday Funday!")
  else:
    print("I wasn't expecting that.")
  print("I feel like you can learn a lot about a person based on their favorite day of the week.")
  quest = input("Do you agree?\n")
  quest = quest.lower()
  if quest=="yes":
    print("It's nice to know thaht we share the same opinion!")
  elif quest =="no":
    print("It's ok for people to have varrying opinions.")
  else:
    print("I wasn't expecting that.")
def holidays():
  global holiday
  print("Enough about days of the week. Let's move on to more special days.")
  holiday = input("What is your favorite holiday?\n")
  holiday = holiday.lower()
  if holiday == "christmas":
    chris = input("A very jolly choice indeed. Why is Christmas your favorite holiday?\n")
    if chris =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you feel the Christmas spirit all the time!")
  elif holiday == "easter":
    east = input("I've never met anyone who's favorite holiday is Easter. Why is it your favorite?\n")
    if east =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you have fun on your next bunny day!")
  elif holiday == "new year's":
    new = input("New Year's! Why is that your favorite?\n")
    if new =="IDK":
      print("Ok nevermind then.")
    else:
      print("Make sure that you keep up with any New Year's resolutions!")
  else:
    extra = input("I wasn't expecting that. Why is it your favorite?\n")
    print("Such an interesting perspective!")
def intro():
 emote = input("How are you feeling today?\n")
 emote = emote.lower()
 if emote=="good" or emote=="happy":
   y=random.randint(0,1)
   if y ==1:
     print("Well that is great to hear!")
   else:
     print("I'm so happy for you!")
 elif emote=="sad" or emote=="sad":
   x=random.randint(0,1)
   if x==1:
     print("Aww I'm so sorry just remember tomorrow is another day.")
   else:
     water=input("Did you drink water today?\n")
     water=water.lower()
     if water =="yes":
       print("Good job! That's progress!")
     elif water=="no":
       print("I know it seems like a small step but try to drink a cup it can really help!")
     else:
       print("I wasn't expecting that.")
 else:
    print("I wasn't expecting that.")
    input("Why do you feel this way?\n")
    print("Interesting.")   
def zodiac():
  global zod
  zod=input("What is your Zodiac sign?\n")
  zod =zod.capitalize()
  if zod == "Cancer" or zod=="Pisces" or zod=="Scorpio":
    print("You're a water sign!")
  elif zod == "Gemini" or zod=="Libra" or zod=="Aquarius":
    print("You're an air sign!")
  elif zod == "Taurus" or zod=="Virgo" or zod=="Capricorn":
    print("You're an earth sign!")
  elif zod == "Aries" or zod=="Leo" or zod=="Aquarius":
    print("You're a fire sign!")
  else:
    print("I wasn't expecting that.")
def conclusion():
  global day1
  global holiday
  print("Well look at what I've learned about you today "+ name1 + "!")
  print("Your zodiac sign is a/an ", end='')
  print(zod)
  print("Your favorite day of the week is ", end='')
  day1=day1.capitalize()
  print(day1)
  print("Your favorite holiday is ", end='')
  holiday=holiday.capitalize()
  print(holiday)
  print("It was great getting to know you!")
def main():
  """This function contains all code for the chatbot."""
  print("Hello! ",end='')
  intro()
  zodiac()
  week()
  holidays()
  conclusion()


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()

