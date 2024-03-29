"""Basic number guessing game."""
# startDate: 2023.5.29

# import time, random, colors
import random
import time
from colorama import Fore, Style

# vars
hundy = list(range(1, 101))
numero = random.randrange(1, 101)
hotcold_alerts = [
    "\nYOU ARE SO CLOOOOSEEEEEEEEEE, BOILING, ABSOLUTELY BOILING!",
    "\nYou are close, close but incorrect.\nHot, as people would say.",
    "\nYou are somewhat warm, somewhat.",
    "\nCold, slightly uncomfortably cold, but bearable.",
    "\nYou are absolutely freezing. I feel for you."
]


# funcs
def hot_cold(input):
    """Return hot/cold info."""
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


def replay(replay_stat):
    """Replay the game."""
    replay_boolean = False
    if replay_stat.lower() == "yes":
        replay_boolean = True
    elif replay_stat.lower() == "no":
        replay_boolean = False
    else:
        print("I will take your incompliance as a no, bye!")
    while replay_boolean:
        game_start(6)


def number_guess(guess):
    """Process the user's number guess."""
    if guess in hundy:
        if guess == numero:
            print(Fore.GREEN + Style.BRIGHT + "Correct!! Farewell Friend!")
            return True
        else:
            hot_cold(guess)
            time.sleep(1)
    else:
        print(Fore.RED + Style.BRIGHT + "Please, within 1-100.\n")
    return False


def number_print():
    """Return the numbers 1-100 in a list."""
    for i in range(1, 101):
        if i <= 99:
            print(Fore.BLUE + Style.BRIGHT + "{}".format(i), end=", ")
        elif i == 100:
            print(Fore.BLUE + Style.BRIGHT + "{}.\n".format(i))
    time.sleep(5)


def game_start(attempt_count):
    """Do number_guess in loops."""
    correct = False
    while attempt_count != 0 and not correct:
        try:
            guess = int(
                input(Fore.BLUE + Style.BRIGHT + "\nGuess the Number!\n"))
            if number_guess(guess):
                correct = True
                break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nPlease enter an actual number.")
        attempt_count -= 1
        if attempt_count == 1:
            print(Fore.RED + Style.BRIGHT + "Make it good, 1 attempt left!")
        elif attempt_count == 0:
            print(Fore.RED + Style.BRIGHT + "Sorry, out of attempts!")
            print(Fore.RED + Style.BRIGHT + "The answer was {}".format(numero))
        else:
            print("Try again, {} attempts left.".format(attempt_count))
    replay(
        input(Fore.MAGENTA + Style.BRIGHT +
              "Would you like to play again? (yes or no)\n"))


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
    print(Fore.WHITE + Style.BRIGHT +
          "\nYou will recieve a list of numbers soon.")
    print(Fore.WHITE + Style.BRIGHT +
          "You will be shown some numbers, one is the key.")
    print(Fore.WHITE + Style.BRIGHT +
          "You will soon be required to guess that very number.")
    print(Fore.WHITE + Style.BRIGHT +
          "You will also be alerted to how Hot or Cold you are to the answer!")
    print(Fore.WHITE + Style.BRIGHT +
          "You only have a 1/100 chance of winning so good luuuck-!\n")
    time.sleep(10)
    # level start
    number_print()

# number-guessing
print(Fore.GREEN + Style.BRIGHT + "You can type your guesses now!\n")
game_start(6)

# replay

# end/victory
