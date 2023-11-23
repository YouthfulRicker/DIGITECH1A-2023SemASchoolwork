# DIGITECH1A-2023SemASchoolwork

This is some work for my 2023 Digitech Class at [Wainuiomata High School](https://wainuiomatahigh.school.nz/).

Main Project Directory
---
My main project is [numbrguessr.py](NumberGuess/numbrguessr.py), a number guessing game.
The base instruction for this program is to run it, and follow it's instructions to attempt to guess a number, and have fun doing so.

In the [NumberGuess](NumberGuess/) folder, there are three things, two folders, and two files, one being the game, the other being what is essentially a basic information leaflet in a [markdown file](NumberGuess/README.md) such as this.

The two subfolders are named [Iterations](NumberGuess/Iterations) and [Pre-Planning](NumberGuess/Pre-Planning). Iterations contains each main iteration of the numbrguessr program and a [markdown file](NumberGuess/Iterations/README.md) containing a [changelog](NumberGuess/Iterations/README.md#Iterations), a [description of the features and functions](NumberGuess/Iterations/README.md#Stages/Features), and a [testlog](NumberGuess/Iterations/README.md#Testing) of things I tested on each iteration.

Everything mentioned is hyperlinked here, and can also easily be found if otherwise required.

---

main.py is a directory navigator that will play the file you want to play depending on your input variable.

init.sh is a general command sheet in which you input your git details (username and email). The script assumes your username is the same as the first part of your email. 

Example:
> Email: example@example2.com
>
> Username: example
>
> Script input: ./init.sh example @example2.com

---

- 1.6.1 is from 3.13 to 3.14
- 1.7.1 is from 3.20 to 3.26
- 1.8.1 is from 3.27 to 3.30

---

- Within NumberGuess is my final project, a number guessing game.

#### Relevant Implications
1. This program uses heavy error-catching in order to increase the usability and functionality of the program. This is necessary because, in order to create a smooth gameplay experience, it is a good idea to prevent as much user error from breaking the program as much as possible, so that the user experiences minimal frustration and minimal struggle in having fun with the program. I have implemented this, to give an example, in the `number_guess` function to prevent the user from entering words and letters, which would give a `ValueError` when trying to convert those to integers. And in the `replay` function, if the user gives an answer other than yes or no, it prompts the user again until they type yes or no, this ensures that the user invokes their right to choose whether or not to play again, rather than the app crashing or just shutting off with an ineligible answer.
2. This program uses color to increase usability and aesthetic value. This makes it so that at but a glance, the user can view the immediacy of the message and act accordingly, and/or just be happy at the looks of the program. Without this the program would just be plain and boring. It would also be less functional due to the user not being able to immediately discern between what they absolutely must read and what they can relax about. I have included this in many simple ways, such as using red for errors to invoke a sense of warning in the user, and to enhance the hot/cold indicator function, for example, displaying colder colors the colder the input, and hotter colors the hotter the input. I used an external library for displaying the colors, called `colorama`. That library allowed me to place the color specification along with the `print` function.
---

- All commit-by-commit progress is listed on [the GitHub commit page](https://github.com/YouthfulRicker/DIGITECH1A-2023SemASchoolwork/commits/main)
