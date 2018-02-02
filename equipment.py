#!/usr/bin/python

import sys

class Background:
    def __init__(self, background, description):
        self.b = background
        self.d = description
print('which background would you like to learn more about? Soldier? Scholar? Engineer?')
x = Background("Soldier:","You are a millitary trained badass!")
y= Background('Engineer:', 'You have spent years studying. Your mind is strong, but your body is weak.')


def parse_response(resp):
    """Python does not contain a standard switch statement
       This function is a standard remedy, it will parse the
       user input during a game, and call the appropriate function"""
    cases = {
        "quit" : exit_game,
        "Quit" : exit_game,
        "exit" : exit_game,
        "Exit" : exit_game,
    }
    func = cases.get(resp, lambda : True)
    return func()



def exit_game():
    """Function to exit the game (with save?)"""
    return False


def run_game():
    """Main game loop/io for text entry/response parsing."""
    not_finished = True
    while(not_finished):
        # do some game stuff
        resp = raw_input('Please enter some text:')
        not_finished = parse_response(resp)
    print('Exiting..')
    exit()

#z=input()
#if z == 'Soldier':
#    print(x.b, x.d)
#if z == 'Scholar':
#    print(y.b, y.d)


if __name__ == "__main__":
    run_game()
