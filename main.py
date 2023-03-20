file = input("Which file would you like to run?\n1 - ifelse.py (clubbing)\n2 - loop.py (are we there yet)\n3 - func-combo.py (function combination)\n")
if file == "1":
  exec(open("1.6.1/ifelse.py").read())
elif file == "2":
  exec(open("1.6.1/loop.py").read())
elif file == "3":
  exec(open("1.7.1/func-combo.py").read())
else:
  print('bruh try again.')