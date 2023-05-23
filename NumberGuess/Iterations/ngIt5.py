# startDate: 2023.5.17

# import time, random, colors
import random
import time
from colorama import Fore, Back, Style

# global vars
hundy = list(range(1, 101))
numero = random.randrange(1, 101)
hotcold_alerts = [
    "\nYOU ARE SO CLOOOOSEEEEEEEEEE, BOILING, ABSOLUTELY BOILING!",
    "\nYou are close my friend. Close but incorrect.\nHot, as people would say.",
    "\nYou are somewhat warm, somewhat.",
    "\nCold, slightly uncomfortably cold, but bearable.",
    "\nYou are absolutely freezing. I feel for you."
]


# funcs
def hot_cold(input):
    difference = abs(input - numero)
    if input < numero:
        if difference < 10:
            print(Fore.RED + Style.BRIGHT + hotcold_alerts[0])
        elif difference < 20:
            print(Fore.RED + Style.NORMAL + hotcold_alerts[1])
        elif difference < 30:
            print(Fore.YELLOW + Style.BRIGHT + hotcold_alerts[2])
        elif difference < 40:
            print(Fore.CYAN + Style.BRIGHT + hotcold_alerts[3])
        else:
            print(Fore.BLUE + Style.BRIGHT + hotcold_alerts[4])
    elif input > numero:
        if difference < 10:
            print(Fore.RED + Style.BRIGHT + hotcold_alerts[0])
        elif difference < 20:
            print(Fore.RED + Style.NORMAL + hotcold_alerts[1])
        elif difference < 30:
            print(Fore.YELLOW + Style.BRIGHT + hotcold_alerts[2])
        elif difference < 40:
            print(Fore.CYAN + Style.BRIGHT + hotcold_alerts[3])
        else:
            print(Fore.BLUE + Style.BRIGHT + hotcold_alerts[4])


def number_guess(guess):
    if guess in hundy:
        if guess == numero:
            print(Fore.GREEN + Style.BRIGHT + "\nWELL DONE! GUESSED CORRECTLY!")
            return True
        else:
            hot_cold(guess)
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + "Try again!")
            time.sleep(1)
    else:
        print(Fore.RED + Style.BRIGHT + "Please, within 1-100.\n")
    return False


def number_print():
    for i in range(1, 101):
        if i <= 99:
            print(Fore.BLUE + Style.BRIGHT + "{}".format(i), end=", ")
        elif i == 100:
            print(Fore.BLUE + Style.BRIGHT + "{}.\n".format(i))
    time.sleep(5)


def game_start():
    while True:
        try:
            guess = int(input(Fore.BLUE + Style.BRIGHT +"\nWhat do you think is the number?\n"))
            if number_guess(guess):
                break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nPlease enter an actual number.")


# name + personalisation
name = input(Fore.MAGENTA + Style.BRIGHT +
             "Well hello there! What is your name?\n")
if name == "5937":
    print("Hello Mr. Developer.\n")
    print(numero)
else:
    name = name.strip()
    time.sleep(3)
    print(Fore.MAGENTA + Style.BRIGHT +
          "\n{}. What a nice name! Glad to have you here".format(name.title()))
    time.sleep(2)
    print(Fore.WHITE + Style.BRIGHT +
          "\nNow, {}, it's time to play a game, a number guessing game!!".
          format(name.title()))
    time.sleep(4)
    print(
        Fore.WHITE + Style.BRIGHT +
        "\nYou will recieve a list of numbers soon.\nThis list will contain numbers from 1-100, and one of them is stored in a variable here in my house, in the backend.\nYou will soon be required to guess that very number for an infinite number.\nYou will also be alerted to how Hot or Cold you are to the answer!\nNow to set your expectations, you only have a 1/100 chance of winning so good luuuck-!\n"
    )
    time.sleep(10)
    # level start
    number_print()

# number-guessing
print(Fore.GREEN + Style.BRIGHT + "You can type your guesses now!\n")
game_start()

# end/victory
