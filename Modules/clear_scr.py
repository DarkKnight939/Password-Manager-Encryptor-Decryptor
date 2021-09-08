import os
# Function to clear the screen


def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')
