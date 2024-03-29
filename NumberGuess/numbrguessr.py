"""Basic number guessing game."""
# startDate: 2023.4.3

# import time, random, colors
import random
import time

from colorama import Fore, Style

# vars
hundy = list(range(1, 101))
numero = random.randrange(1, 101)
guesses = []
hotcold_alerts = [
    "\nYOU ARE SO CLOOOOSEEEEEEEEEE, BOILING, ABSOLUTELY BOILING!",
    "\nYou are close, close but incorrect.\nHot, as people would say.",
    "\nYou are somewhat warm, somewhat.",
    "\nCold, slightly uncomfortably cold, but bearable.",
    "\nYou are absolutely freezing. I feel for you."
]
max_attempts = 6


# funcs
def number_check(text):
    """Return true if any character in string is a digit."""
    return any(char.isdigit() for char in text)


def hot_cold(guess, numero):
    """Return hot/cold info."""
    difference = abs(guess - numero)
    if difference < 5:
        print(Fore.RED + Style.BRIGHT + hotcold_alerts[0])
    elif difference < 10:
        print(Fore.RED + Style.BRIGHT + hotcold_alerts[1])
    elif difference < 20:
        print(Fore.YELLOW + Style.BRIGHT + hotcold_alerts[2])
    elif difference < 30:
        print(Fore.CYAN + Style.BRIGHT + hotcold_alerts[3])
    else:
        print(Fore.BLUE + Style.BRIGHT + hotcold_alerts[4])


def replay(replay_stat, guesses):
    """Replay the game."""
    replay_boolean = False
    if replay_stat.lower() == "yes":
        replay_boolean = True
    elif replay_stat.lower() == "no":
        replay_boolean = False
    while replay_boolean:
        numero = random.randrange(1, 101)
        game_start(6, guesses, numero)
        replay_stat = input(Fore.MAGENTA + Style.BRIGHT +
                            "Would you like to play again? (yes or no)\n")
        while replay_stat.lower() not in ["yes", "no"]:
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + "\nPlease enter yes or no")
            time.sleep(1)
            replay_stat = input(Fore.MAGENTA + Style.BRIGHT +
                                "Would you like to play again? (yes or no)\n")
        if replay_stat.lower() == "yes":
            replay_boolean = True
        elif replay_stat.lower() == "no":
            replay_boolean = False
    return replay_stat


def number_guess(guess, attempt_count, numero, guesses):
    """Process the user's number guess."""
    if guess in hundy:
        guesses.append(guess)
        if guess == numero:
            print(Fore.GREEN + Style.BRIGHT + "Correct!!")
            print(Fore.BLUE + Style.BRIGHT + "You Guessed:", guesses, "\n")
            return True, attempt_count, guesses
        else:
            hot_cold(guess, numero)
            time.sleep(1)
    else:
        print(Fore.RED + Style.BRIGHT + "Please, within 1-100.\n")
        attempt_count += 1
    return False, attempt_count, guesses


def number_print():
    """Return the numbers 1-100 in a list."""
    for i in range(1, 101):
        if i <= 99:
            print(Fore.BLUE + Style.BRIGHT + "{}".format(i), end=", ")
        elif i == 100:
            print(Fore.BLUE + Style.BRIGHT + "{}.\n".format(i))
    time.sleep(5)


def game_start(attempt_count, guesses, numero):
    """Do number_guess in loops."""
    guesses = []
    correct = False
    numero = random.randrange(1, 101)
    while attempt_count != 0 and not correct:
        try:
            guess = int(
                input(Fore.BLUE + Style.BRIGHT + "\nGuess the Number!\n"))
            correct, attempt_count, guesses = number_guess(
                guess, attempt_count, numero, guesses)
            if correct:
                break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nPlease enter an actual number.")
            attempt_count += 1
        attempt_count -= 1
        if attempt_count == 1:
            print(Fore.RED + Style.BRIGHT + "Make it good, 1 attempt left!")
        elif attempt_count == 0:
            print(Fore.RED + Style.BRIGHT + "Sorry, out of attempts!\n")
            print(Fore.RED + Style.BRIGHT +
                  "The answer was {}\n".format(numero))
            print(Fore.BLUE + Style.BRIGHT + "You Guessed:", guesses, "\n")

            guesses = []
        else:
            print("Try again, {} attempts left.".format(attempt_count))


#    return attempt_count

# name + personalisation
name = input(Fore.MAGENTA + Style.BRIGHT +
             "Well hello there! What is your name?\n")
if name == "5937":
    print("Hello Mr. Developer.\n")
    print(numero)
else:
    while number_check(name):
        print(Fore.RED + Style.BRIGHT + "\nNo numbers in your name please.\n")
        name = input(Fore.MAGENTA + Style.BRIGHT + "Please enter your name\n")
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
attempt_count_remaining = game_start(max_attempts, guesses, numero)

replay_stat = input(Fore.MAGENTA + Style.BRIGHT +
                    "Would you like to play again? (yes or no)\n")

while replay_stat.lower() not in ["yes", "no"]:
    time.sleep(1)
    print(Fore.RED + Style.BRIGHT + "\nPlease enter yes or no")
    time.sleep(1)
    replay_stat = input(Fore.MAGENTA + Style.BRIGHT +
                        "Would you like to play again? (yes or no)\n")

while replay_stat.lower() == "yes":
    numero = random.randrange(1, 101)
    replay_stat = replay(replay_stat, guesses)

time.sleep(2)
print(Fore.GREEN + Style.BRIGHT + "Thanks for playing!")
