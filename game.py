#!/usr/bin/python

def run_game():
    """
    Main entry point:
    Loop here, and parse user input until quit condition
    """
    game_done = False
    while (not game_done):
        resp = raw_input("Type something here:") 
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
    }
    func = cases.get(resp, lambda : False)
    return func() 


def exit_game():
    """ exits game
    """
    return True # our exit condition in the while loop (game_done = true) ok


if __name__ == "__main__":
    run_game()
