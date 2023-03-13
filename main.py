file = input("Which file would you like to run?\n1 - if-else.py (clubbing)\n2 - loop.py (are we there yet)\n")
if file == "1":
  exec(open("1.6.1/if-else.py").read())
elif file == "2":
  exec(open("1.6.1/loop.py").read())