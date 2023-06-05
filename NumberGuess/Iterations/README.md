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
  - Attempt Countdown
- ngIt6.py
  - Game Engine 
  - Game Base 
  - Introduction with Name Use
  - Colour
  - HotCold func
  - Cheat Code 
  - Attempt Countdown
  - Replay Function

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
- Attempt Countdown
    - The attempt countdown gives a limited quantity of guesses, allowing for a greater sense of engagement and urgency for the player.
    - In essence, it counts down the quantity of guesses the user takes, using a function argument in the Game Base
- Replay Function
    - The replay function allows for the player to replay the game multiple times, with different numbers but everything else the same.
    - This works by one function that takes a string 'yes or no' input through an argument, and, using an if statement, converts it into a boolean, and gives it to a while loop that runs the game base.
    - Hilariously the game base is actually what calls the replay function, looping until the player decides not to play.

-------

# Testing

|**Test ID**|**Test Scenario**|**Test Description**|**Test Steps**|**Expected Results**|
|---|---|---|---|---|
|1|Enter text string as guess|This is to test whether the program will just spit out an error and end or notify the user as to the error and continue when given a string when expecting an integer.|Enter "portland" when asked for a guess.|I expect that my try/except should catch the issue and notify the user without stopping the program.|
|2|Boundary test number input range|This will check whether when you guess, if you enter a number outside of 1-100, that it'll tell you and allow you to guess again rather than immediately turn off.|Try guessing 0, 1, 100, 101, 150, and 200.|I expect that it will tell me to guess within the boundaries. By this definition, 0, 101, and 150 should all fail and trip the error warning.|
|3|Name usage|This tests whether names are handled correctly in the script. Removing unnecessary spaces, correcting capitalisation, etc.|Enter "  FoRResTer GUmP  "|This, through the variable modifications and scripting, should output "Forrester Gump".|
|4|HotCold testing|This will test whether my HotCold function will output the correct message depending on how close you are to the number.|Go into dev mode (enter '5937' when asked for a name), look at the provided number, and formulate your guesses from that. Deoending on the provided number, guess 9 numbers behind/forward 5 times. e.g, if the provided number was 24, you can't go back far, so go forward. You would type 32, 41, 50, 59, and 68 to test the messages. for a higher number, you would do similar but backwards.|Each integer should return a different message corresponding to roughly how close it is to the source number.|
|5|Attempt Countdown testing|This will test whether the code correctly limits your attempt count depending on the quantity specified in the code.|Just guess repeatedly, you should be told how many attempts you have left as well as when you have none left.
|6|Replay loop testing|This will test whether the code can correctly replay the code after an expiry of attempt quantity.|Just play until you get the 'do you want to play again' message, and try to say yes after two playthroughs, and then say no on the third.|Depending on your 

### Test Results
|**Test ID**|**ngIt1**|**ngIt2**|**ngIt3**|**ngIt4**|**ngIt5**|**ngIt6**|
|---|---|---|---|---|---|---|
|1|Success|Success|N/A|N/A|N/A|N/A|
|2|Success|Success|N/A|N/A|N/A|N/A|
|3|Success|Success|Success|N/A|N/A|N/A|
|4|Success|Success|Success|Success|N/A|N/A|
|5|Success|Success|Success|Success|Success|N/A|
|6|Success|Success|Success|Success|Success|Success|