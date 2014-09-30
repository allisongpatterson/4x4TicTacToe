#!/usr/bin/env python
# 

#
# Game Programming, Level 2 Project
#
# TIC-TAC-TOE 4
#
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe
#

import sys
testString = '.....XO..OX.....'
size = 4
WIN_SEQUENCES = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [4,8,12,16],
    [1,6,11,16],
    [4,7,10,13]
]

MARK_VALUE = {
    'O': 1,
    '.': 0,
    'X': 10
}

class board(object):
    def __init__(self, boardString):
        self.boardList = boardString

    def valueOfCoordinate(self,x,y):
        value = self.boardList[(x-1) + size*(y-1)]
        return value

    def indexOfCoordinate(self,x,y):
        index = (x-1)+size*(y-1)
        return index

# def fail (msg):
#     raise StandardError(msg)


def create_board (boardString):
    # FIX ME
    #
    # Take a description of the board as input and create the board
    #  in your representation
    #
    # The string description is a sequence of 16 characters,
    #   each either X or O, or . to represent a free space
    # It is allowed to pass in a string describing a board
    #   that would never arise in legal play starting from an empty
    #   board
    # return None

    board = board(testString)
    return board

def has_mark (board,x,y):
    # FIX ME
    #
    # Take a board representation and checks if there's a mark at
    #    position x, y (each between 1 and 4)
    # Return 'X' or 'O' if there is a mark
    # Return False if there is not
    # return None

    if board.valueOfCoordinate(x,y) == '.':
        return False
    elif board.valueOfCoordinate(x,y) != '.':
        return board.valueOfCoordinate(x,y)

def has_win (board):
    # FIX ME
    # 
    # Check if a board is a win for X or for O.
    # Return 'X' if it is a win for X, 'O' if it is a win for O,
    # and False otherwise
    # return None

    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 4:
            return 'O'
        if s == 40:
            return 'X'
    return False

def done (board):
    # FIX ME
    #
    # Check if the board is done, either because it is a win or a draw
    # return True

    if has_win(board) != False:
        return True
    elif has_win(board) == False:
        for i in range(0,len(board.boardList)):
            if board.boardList[i] == '.':
                return False
        return True

def print_board (board):
    # FIX ME
    #
    # Display a board on the console
    # return None

    for i in range(0,4):
        print ' ',board.boardList[i*4],board.boardList[i*4+1],board.boardList[i*4+2],board.boardList[i*4+3]
    print

def read_player_input (board, player):
    # FIX ME
    #
    # Read player input when playing as 'player' (either 'X' or 'O')
    # Return a move (a tuple (x,y) with each position between 1 and 4)
    # return None

    while True:
        move = raw_input#('Enter row,column (ex: 2,3) to make move.')
        if move == 'q':
            exit(0)
        if has_mark(board,move[0],move[1]) == False:
            print int(move[0]),int(move[1])

def make_move (board,move,player):
    # FIX ME
    #
    # Returns a board where 'move' has been performed on 'board' by 
    #    'player'
    # Change can be done in place in 'board' or a new copy created
    # return None

    moveSpace = board.indexOfCoordinate(move[0],move[1])
    newBoard = board.boardList[:]
    board.boardList[moveSpace] = player
    return board.boardList

    # new_board = board.boardList[:]
    # new_board[move] = player
    # return new_board

def computer_move (board,player):
    # FIX ME
    #
    # Select a move for the computer, when playing as 'player' (either 
    #   'X' or 'O')
    # Return the selected move (a tuple (x,y) with each position between 
    #   1 and 4)
    return None


def other (player):
    if player == 'X':
        return 'O'
    return 'X'


def run (str,player,playX,playO): 

    board = create_board(str)

    print_board(board)

    while not done(board):
        if player == 'X':
            move = playX(board,player)
        elif player == 'O':
            move = playO(board,player)
        else:
            fail('Unrecognized player '+player)
        board = make_move(board,move,player)
        print_board(board)
        player = other(player)

    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'
        
def main ():
    run('.' * 16, 'X', read_player_input, computer_move)


PLAYER_MAP = {
    'human': read_player_input,
    'computer': computer_move
}

# if __name__ == '__main__':

#   try:
#       #str = sys.argv[1] if len(sys.argv)>1 else '.' * 16
#       player = sys.argv[2] if len(sys.argv)>3 else 'X'
#       playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else read_player_input
#       playO = PLAYER_MAP[sys.argv[4]] if len(sys.argv)>4 else computer_move
#   except:
#     print 'Usage: %s [starting board] [X|O] [human|computer] [human|computer]' % (sys.argv[0])
#     exit(1)
#   run(testString,player,playX,playO)

board = board(testString)
print board.valueOfCoordinate(2,3)
print has_mark(board,2,3)
print_board(board)
a = 1,1
print make_move(board,a,'X')