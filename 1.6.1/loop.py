awtystat = False


def areWeThereYet():
  global awtystat
  while not awtystat:
    answer = input("Are we there yet?\n").lower()
    if answer in ["yes", "y", "ye", "yep"]:
      print("WHOHOOOOO, YIPPEE, A TRIP YEEHEEEEEEE")
      awtystat = True
    elif answer in ["no", "n", "nu", "nope"]:
      print("THEN WHEN?!?!?!?!")
      awtystat = False
    else:
      print("That's not an answer goddamnit.")


areWeThereYet()
