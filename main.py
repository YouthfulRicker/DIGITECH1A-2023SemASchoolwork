file = input(
  "Which file would you like to run?\n1 - ifelse.py (clubbing)\n2 - loop.py (are we there yet)\n3 - func-combo.py (function combination)\n4 - lists.py (experimenting with lists)\n5 - McGuireExample.py (Mr. McGuire's example of an if-else statement with lower class)\n6 - TryExceptExample.py (An example of the Try/Except function in python)\n7 - numbrguessr.py (My Final Project, A Number Guessing Game)\n"
)
if file == "1":
  exec(open("1.6.1/ifelse.py").read())
elif file == "2":
  exec(open("1.6.1/loop.py").read())
elif file == "3":
  exec(open("1.7.1/func-combo.py").read())
elif file == "4":
  exec(open("1.7.1/lists.py").read())
elif file == "5":
  exec(open("1.8.1/McGuireExample.py").read())
elif file == "6":
  exec(open("1.8.1/TryExceptExample.py").read())
elif file == "7":
  exec(open("numbrguessr.py").read())
else:
  print('bruh try again.')
