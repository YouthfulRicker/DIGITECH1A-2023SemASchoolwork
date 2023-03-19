awtystat = False
from time import sleep

def ageCheck():
  age=int(input("How old are you?\n"))
  name=input("What's your name?\n")
  if age < 18 :
    print("{}, YOU CAN'T GO TO THE CLUB YOU GOTTA WAIT {} YEARS".format(name.upper(), 18-age))
    sleep(5)
    print("Let's just go to the ice cream bar {}".format(name.title()))
  elif age >= 18 :
    print("Aight {} let's go clubbing!".format(name.title()))
    sleep(3)
    drink=input("What drink would you like?\n")
    sleep(2)
    print("aight, Waiter!!")
    sleep(1)
    print("Yes sir, what do you require?")
    sleep(1)
    print("Two {}s please.".format(drink.title()))
  else :
    print("E-?")
    
def areWeThereYet():
  areWeThereYet = input("Are we there yet?\n")
  if areWeThereYet == "yes" or areWeThereYet == "y" or areWeThereYet == "ye" or areWeThereYet == "yep" or areWeThereYet == "Yes" or areWeThereYet == "Y" or areWeThereYet == "Ye" or areWeThereYet == "Yep" :
    print("WHOHOOOOO, YIPPEE, A TRIP YEEHEEEEEEE")
    awtystat = True
    quit()
  elif areWeThereYet == "no" or areWeThereYet == "n" or areWeThereYet == "nu" or areWeThereYet == "nope" or areWeThereYet == "No" or areWeThereYet == "N" or areWeThereYet == "Nu" or areWeThereYet == "Nope" :
    print("THEN WHEN?!?!?!?!")
    awtystat = False
  else:
    print("That's not an answer goddamnit.")