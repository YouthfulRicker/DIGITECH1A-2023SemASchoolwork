# Iterations

- ngIt1.py
  - Game Engine
  - Game Base
- ngIt2.py
  - Game Engine
  - Game Base
  - Introduction with Name Use
- ngIt3.py
  - Game Engine
  - Game Base
  - Introduction with Name Use
  - Colour
- ngIt4.py
  - Game Engine
  - Game Base
  - Introduction with Name Use
  - Colour
  - HotCold func
  - Cheat Code
- ngIt5.py
  - Game Engine (removed boolean variable, made engine definition return true/false)
  - Game Base (moved to function 'game_start')
  - Introduction with Name Use
  - Colour
  - HotCold func
  - Cheat Code (changed to '5937')

---

# Stages/Features

- Game Engine
  - The game engine uses two functions. One for handling the guess, and one for printing the numbers in a organised fashion. The function for handling the guess also contains a variable within it's brackets for use within the function.
  - These functions also use three global variables for their actions. One list, one random-randrange, and one boolean.
    - The list is a simple directory of the numbers 1-101, as it is a converted range.
    - The random-randrange variable is to select the number that needs to be guessed.
    - And finally, the boolean is simply to store whether the number has been successfully guessed or not.
  - Within the engine is also a catch-all for entered numbers over 100, giving a warning to stay within 1-100.
- Game Base
  - This is the part of the code that activates the functions and has extra checks and inputs. It's a simple loop that just constantly cycles while the guess boolean is false, and has a try & except to catch non-integer user input.
- Introduction with Name Use
  - This is basically just a 'hello' using a user input variable (name) that is stripped of spaces, and is used in a print function where it is titled and formatted correctly according to the needs of the phrase.
- Colour
  - Colour uses an external dependency called Colorama. This allows for simple addition of print colour for added cosmetic satisfaction.
- HotCold func
    - This is the function to tell the user whether they're hot or cold, in the sense of how close they are to the answer. This allows for a greater sense of anticipation for the user.
    - Originally I had used a basic system of if this is less than that then calculate this minus this and if it's less than 10 or such. But then I learnt of a python function that gives you the absolute difference between two integers called abs(), so I then simplified the code using that.
- Cheat Code
  - I added a singular cheat code, for the original reason cheat codes were invented. To get around the preview quicker as a developer!
  - It's based in the name variable, where when you type your name, you should actually type 'testcode', and it will bypass the introduction and give you the answer. This was designed so I could bypass the introduction and test the HotCold function with the answer given to me.