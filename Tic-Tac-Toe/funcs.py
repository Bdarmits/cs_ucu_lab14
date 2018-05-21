'''
This module includes functions used in game.py
'''

def get_valid_input(input_str, valid_options):
    '''
    This func gets data from user
    :param input_str: msg that will be displayed to user when asking for data
    :param valid_options: all valid options of data
    :return: (str) - user's option
    '''
    input_str += " ({}) ".format(", ".join(valid_options))
    resp = input(input_str)
    while resp.lower() not in valid_options:
        resp = input(input_str)
    return resp


def userMakeMove(user_turn, board):
    '''
    This function handles user move
    :param user_turn: a str represents user figure(X or O)
    :param board: Board class inctance represents the Game Board
    :return: None
    '''
    print("\nIt's your turn to make a move!")
    coord = input("Please type the coord below - first row, then col: ")
    try:
        coord = tuple([int(i) for i in coord.split()])
    except:
        pass
    if coord in board.availible_cells:
        if board.put(user_turn, coord):
            pass
        else:
            print("Your move is not valid, try again.\n")
            userMakeMove(user_turn, board)
    else:
        print("Your move is not valid, try again.")
        userMakeMove(user_turn, board)
