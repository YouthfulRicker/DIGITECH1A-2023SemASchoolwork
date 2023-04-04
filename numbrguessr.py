# startDate: 2023.4.3

# import time, random, colors
import random
import time
from colorama import Fore, Back, Style

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
      print(Fore.GREEN + "\nWELL DONE! GUESSED CORRECTLY!")
      guessstat = True
    else:
      print(Fore.RED7 + "\nIncorrect, try again!!\n")

def numbPrint():
  for i in range(1, 101):
    if i <= 99:
      print(i, end=", ")
    elif i == 100:
      print("{}.\n".format(i))
  time.sleep(5)

# intro

# name + personalisation
name = input(Fore.YELLOW + "Well hello there! What is your name?\n")
time.sleep(3)
print(Fore.YELLOW + "\n{}. What a nice name! Glad to have you here".format(name.title()))
time.sleep(2)
print(Fore.YELLOW + "\nNow, {}, it's time to play a game, a number guessing game!!".format(
  name.title()))
time.sleep(8)
print(Fore.YELLOW + 
  "\nYou will recieve a list of numbers soon.\nThis list will contain numbers from 1-100, and one of them is stored in a variable here in my house, in the backend.\nYou will soon be required to guess that very number for an infinite number.\nNow to set your expectations, you only have a 1/100 chance of winning so good luuuck-!\n"
)
time.sleep(10)

# level start
numbPrint()
#print(numero)

# number-guessing
print(Fore.GREEN + "You can type your guesses now!\n")
while not guessstat:
  guessstat = False
#  guessr = input("What do you think is the number?\n")
  try:
    numbGuess(int(input(Fore.BLUE + "What do you think is the number?\n")))
  except:
    print(Fore.RED + "\nPlease enter an actual number.\n")

# end/victory
