awtystat = False
def areWeThereYet():
  areWeThereYet = input("Are we there yet?")
  if areWeThereYet == "yes" or areWeThereYet == "y" or areWeThereYet == "ye" or areWeThereYet == "yep" or areWeThereYet == "Yes" or areWeThereYet == "Y" or areWeThereYet == "Ye" or areWeThereYet == "Yep" :
    print("WHOHOOOOO, YIPPEE, A TRIP YEEHEEEEEEE")
    awtystat = True
    quit()
  elif areWeThereYet == "no" or areWeThereYet == "n" or areWeThereYet == "nu" or areWeThereYet == "nope" or areWeThereYet == "No" or areWeThereYet == "N" or areWeThereYet == "Nu" or areWeThereYet == "Nope" :
    print("THEN WHEN?!?!?!?!")
    awtystat = False
  else:
    print("That's not an answer goddamnit.")
#def checkAwtystat():
#  if awtystat == False:
#    areWeThereYet()

#checkAwtystat()
while awtystat == False:
  areWeThereYet()