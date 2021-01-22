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
  if day =="Monday":
    mon = input("Ew. Why Monday?\n")
    if mon=="IDK":
      print("Ok nevermind then.")
    else:
      print("Strange.")
  elif day=="Tuesday":
    tues = input("Oooo Taco Tuesday. Why is it your favorite?\n")
    if tues=="IDK":
      print("Ok Nevermind then.")
    else:
      print("That's a cool take on Tuesdays!")
  elif day=="Wednesday":
    wed = input("Why Wednesday my dude?\n")
    if wed=="IDK":
      print("Ok nevermind then.")
    else:
      print("Wenesdays always seem to pass by so quickly.")
  elif day=="Thursday":
    thurs = input("Friday Jr! Why is that one your favorite?\n")
    if thurs=="IDK":
      print("Ok Nevermind then.")
    else:
      print("Well then I hope you enjoy your next Friday Jr.")
  elif day =="Friday":
    fri = input("Someone with good taste. Why is it your favorite day of the week?\n")
    if fri=="IDK":
      print("Ok nevermind then.")
    else:
      print("May I reccommend: Katy Perry's hit song \"Last Friday night?\"")
  elif day=="Saturday":
    sat = input("Ahhh Saturday the day of rest. Why is it your favorite?\n")
    if sat =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you enjoy your next Saturday!")
  elif day=="Sunday":
    sun = input("The sunniest of the days. Why is Sunday your favorite?\n")
    if sun =="IDK":
      print("Ok nevermind then.")
    else:
      print("Sunday Funday!")
  else:
    print("I wasn't expecting that.")
  print("I feel like you can learn a lot about a person based on their favorite day of the week.")
  quest = input("Do you agree?\n")
  if quest=="Yes":
    print("It's nice to know thaht we share the same opinion!")
  elif quest =="No":
    print("It's ok for people to have varrying opinions.")
  else:
    print("I wasn't expecting that.")
def holidays():
  global holiday
  print("Enough about days of the week. Let's move on to more special days.")
  holiday = input("What is your favorite holiday?\n")
  if holiday == "Christmas":
    chris = input("A very jolly choice indeed. Why is Christmas your favorite holiday?\n")
    if chris =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you feel the Christmas spirit all the time!")
  elif holiday == "Easter":
    east = input("I've never met anyone who's favorite holiday is Easter. Why is it your favorite?\n")
    if east =="IDK":
      print("Ok nevermind then.")
    else:
      print("I hope that you have fun on your next bunny day!")
  elif holiday == "New Year's":
    new = input("New Years! Why is that your favorite?\n")
    if new =="IDK":
      print("Ok nevermind then.")
    else:
      print("Make sure that you keep up with any New Year's resolutions!")
  else:
    extra = input("I wasn't expecting that. Why is it your favorite?\n")
    print("Such an interesting perspective!")
def intro():
  emote = input("How are you feeling today?\n")
  if emote == "Sad":
    x = random.randint(0,1)
    if x==0:
      print("I'm so sorry to hear that. Just hang on and I'm sure today will get better!")
    elif x==1:
      water=input("Did you dirnk water today?\n")
      if water == "Yes":
        print("Good job! I'm proud of you just keep making progress!")
      elif water=="No":
        print("Try to drink a cup. It might not seem like it will help but I promise that it will!")
      else:
        print("I wasn't expecting that.")
  elif emote=="Happy":
    y = random.randint(0,1)
    if y==0:
      print("That's great to hear!")
    elif y==1:
      print("Keep up the positive attidude!")
  else:
     input("Well I wasn't expecting that. Why do you feel that way?\n")
     print("That's very interesting.")
def zodiac():
  global zod
  zod=input("What is your Zodiac sign?")
  if zod == "Cancer" or "Pisces" or "Scorpio":
    print("You're a water sign!")
  elif zod == "Gemini" or "Libra" or "Aquarius":
    print("You're an air sign!")
  elif zod == "Taurus" or "Virgo" or "Capricorn":
    print("You're an earth sign!")
  elif zod == "Aries" or "Leo" or "Aquarius":
    print("You're a fire sign!")
  else:
    print("I wasn't expecting that.")
def conclusion():
  print("Well look at what I've learned about you today!\n")
  print("Your zodiac sign is a/an ", end='')
  print(zod)
  print("Your favorite day of the week is ", end='')
  print(day1)
  print("Your favorite holiday is ", end='')
  print(holiday)
  print("It was great getting to know you!")

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
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

