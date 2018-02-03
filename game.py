#!/usr/bin/python

import character as char

def run_game():
    """
    Main entry point:
    Loop here, and parse user input until quit condition
    """
    game_done = False
    print("Type a command below..")
    while (not game_done):
        resp = raw_input() 
        game_done = parse_response(resp)
    print("..exiting") 
    exit() 

    
def parse_response(resp):
    """
    First stab at response parsing:
    Collect a user response and check if a pre-defined
    method should be called (is it a valid response)..If not it returns
    False .. this signifies that a game is not finished.
    """
    cases = {
        "Quit" : exit_game,
        "quit" : exit_game,
        "exit" : exit_game,
        "Exit" : exit_game,
        "start": start_character,
        "help" : help_menu,
    }
    func = cases.get(resp, lambda : False)
    return func() 


def help_menu():    
    print('..list of recognized commands')
    print('  help: prints this menu')
    print('  quit/Quit/Exit/exit: exits the game.')
    print('  start: picks a character for you, and starts')    
    return False


def start_character():
    """
    Dbg method to select a new character and start a game
    We can make it fancier later, for now, we default to Marine
    for the character selection
    """
    p = char.CharacterProps("Arnold",height=2,weight=120)
    M = char.Marine(props=p)
    M.desc() # test printout
    return False


def exit_game():
    """ exits game
    """
    return True # our exit condition in the while loop (game_done = true) ok



if __name__ == "__main__":
    run_game()
