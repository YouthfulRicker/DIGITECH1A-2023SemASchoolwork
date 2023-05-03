# startDate: 2023.4.10

# import time, random, colors
import random
import time

# vars 
guessstat = False
hundy = list(range(1, 101))
numero = random.randrange(1, 101)

# funcs
def numbGuess(guess):
  global guessstat
  if guess in hundy:
    if guess == numero:
      print("\nWELL DONE! GUESSED CORRECTLY!")
      guessstat = True
    else:
      print("Incorrect, try again!!\n")
  else:
    print("Please, within 1-100.\n")

def numbPrint():
  for i in range(1, 101):
    if i <= 99:
      print("{}".format(i), end=", ")
  time.sleep(5)

# name + personalisation
name = input("Well hello there! What is your name?\n")
name = name.strip()
time.sleep(3)
print("\n{}. What a nice name! Glad to have you here".format(name.title()))
time.sleep(2)
print("\nNow, {}, it's time to play a game, a number guessing game!!".format(name.title()))
time.sleep(8)
print(
  "\nYou will recieve a list of numbers soon.\nThis list will contain numbers from 1-100, and one of them is stored in a variable here in my house, in the backend.\nYou will soon be required to guess that very number for an infinite number.\nNow to set your expectations, you only have a 1/100 chance of winning so good luuuck-!\n"
)
time.sleep(10)

# level start
numbPrint()

# number-guessing
print("You can type your guesses now!\n")
while not guessstat:
  guessstat = False
#  guessr = input("What do you think is the number?\n")
  try:
    numbGuess(int(input("What do you think is the number?\n")))
  except:
    print("Please enter an actual number.\n")

# end/victory