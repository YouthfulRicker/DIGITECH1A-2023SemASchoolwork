from colorama import Fore, Back
import os

file = input(
  Fore.LIGHTBLUE_EX +
  "Which file would you like to run?\n1 - ifelse.py (clubbing)\n2 - loop.py (are we there yet)\n3 - func-combo.py (function combination)\n4 - lists.py (experimenting with lists)\n5 - McGuireExample.py (Mr. McGuire's example of an if-else statement with lower class)\n6 - TryExceptExample.py (An example of the Try/Except function in python)\n7 - colortesting.py (Just an example of the colors I was contemplating putting into my other programs.)\n8 - numbrguessr.py (My Final Project, A Number Guessing Game)\n9 - numbrguessr.py's iterations\n")
if file == "1":
  os.system('clear')
  exec(open("1.6.1/ifelse.py").read())
elif file == "2":
  os.system('clear')
  exec(open("1.6.1/loop.py").read())
elif file == "3":
  os.system('clear')
  exec(open("1.7.1/func-combo.py").read())
elif file == "4":
  os.system('clear')
  exec(open("1.7.1/lists.py").read())
elif file == "5":
  os.system('clear')
  exec(open("1.8.1/McGuireExample.py").read())
elif file == "6":
  os.system('clear')
  exec(open("1.8.1/TryExceptExample.py").read())
elif file == "7":
  os.system('clear')
  exec(open("1.11.1/colortesting.py").read())
elif file == "8":
  os.system('clear')
  exec(open("NumberGuess/numbrguessr.py").read())
elif file == "9":
  try:
    itno = int(input("Which iteration do you want? (1-6)\n"))
  except:
    print("invalid, please try again")
  os.system('clear')
  exec(open("NumberGuess/Iterations/ngIt{}.py".format(itno)).read())
else:
  print('bruh try again.')
