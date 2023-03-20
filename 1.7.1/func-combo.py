import os
import sys

def current_path(): 
    print("Current working directory: " + os.getcwd()) 

#current_path()
os.chdir("1.6.1/")
#current_path()
sys.path.append(os.getcwd())

from loop import areWeThereYet
from i\f\-el\se import areWeThereYet

areWeThereYet()