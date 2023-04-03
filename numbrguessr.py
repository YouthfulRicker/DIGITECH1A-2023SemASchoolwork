# startDate: 2023.4.3

# import time, random
import random
import time

# intro

# name + personalisation
name = input("Well hello there! What is your name?\n")
time.sleep(3)
print("{}. What a nice name! Glad to have you here".format(name.title()))
time.sleep(2)
print("Now, {}, it's time to play a game, a number guessing game!!".format(
  name.title()))
time.sleep(1)
print(
  "You will recieve a list of numbers soon.\nThis list will contain numbers from 1-100, and one of them is stored in a variable here in my house, in the backend.\nYou will soon be required to guess that very number for an infinite number.\nNow to set your expectations, you only have a 1/100 chance of winning so good luuuck-!"
)
print("Now, {}, it's time to play a game, a number guessing game!!".format(name.title()))
time.sleep(1)
print("You will recieve a list of numbers soon.\nThis list will contain numbers from 1-100, and one of them is stored in a variable here in my house, in the backend.\nYou will soon be required to guess that very number for an infinite number.\nNow to set your expectations, you only have a 1/100 chance of winning so good luuuck-!")
time.sleep(15)

# level start
guessstat = True
hundy = list(range(1, 100))
numero = random.randrange(1, 100)
#print(numero)
for i in range(1, 101):
  if i <= 99:
    print(i, end=", ")
  elif i == 100:
    print(i)
time.sleep(5)

# number-guessing
print("\nYou can type your guesses now!")
while guessstat == True:
  guess = str(input("What do you think is the number?\n"))
  if guess in hundy:
    print("WORKING WOOOO")
    if guess == numero:
      print("WELL DONE! GUESSED CORRECTLY!")
      guessstat = True
    else:
      guesstat = False
      print("Incorrect, try again!!")

# end/victory
