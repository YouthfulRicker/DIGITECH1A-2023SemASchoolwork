# startDate: 2023.4.3

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
#    print("WORKING WOOOO")
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