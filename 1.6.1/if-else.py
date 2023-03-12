from time import sleep
def ageCheck():
  age=int(input("How old are you? "))
  name=input("What's your name? ")
  if age < 18 :
    print("{}, YOU CAN'T GO TO THE CLUB YOU GOTTA WAIT {} YEARS".format(name.upper(), 18-age))
    sleep(5)
    print("Let's just go to the ice cream bar {}".format(name.title()))
  elif age >= 18 :
    print("Aight {} let's go clubbing!".format(name.title()))
    sleep(3)
    drink=input("What drink would you like? ")
    sleep(2)
    print("aight, Waiter!!")
    sleep(1)
    print("Yes sir, what do you require?")
    sleep(1)
    print("Two {}s please.".format(drink.title()))
  else :
    print("E-?")

ageCheck()