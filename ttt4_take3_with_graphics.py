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
import copy
import ttt4_graphics

testString = 'XOXOXOXOX.X.O...'
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
        self.boardList = []
        for i in range(0,len(boardString)):
        #self.boardList = [boardString]
            self.boardList.append(boardString[i])
        print self.boardList

    def valueOfCoordinate(self,x,y):
        value = self.boardList[(x-1) + size*(y-1)]
        return value

    def indexOfCoordinate(self,x,y):
        index = (int(x)-1)+size*(int(y)-1)
        return int(index)

    def coordinateOfIndex(self,index):
        y = index/size
        x = index-(y*size)
        coord = str(x+1)+','+str(y+1)
        return coord
        # print coord[0]
        # print coord[1]
        # print str(coord[0])+','+str(coord[1])

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
    
    board1 = board(boardString)
    return board1


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
        s = sum(MARK_VALUE[board.boardList[pos-1]] for pos in positions)
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
    else:
        for i in range(0,len(board.boardList)):
            if board.boardList[i] == '.':
                return False
        return True

def print_board (board):
    # FIX ME
    #
    # Display a board on the console
    # return None
    boarda = ttt4_graphics.create_grid()
    for i in range(0,len(board.boardList)):
        coord = board.coordinateOfIndex(i)
        value = board.valueOfCoordinate(int(coord[0]),int(coord[2]))
        if value != '.':
            ttt4_graphics.display_mark(int(coord[0]),int(coord[2]),value)

    # for i in range(0,4):
    #     print ' ',board.boardList[i*4],board.boardList[i*4+1],board.boardList[i*4+2],board.boardList[i*4+3]
    # print


def read_player_input (board, player):
    # FIX ME
    #
    # Read player input when playing as 'player' (either 'X' or 'O')
    # Return a move (a tuple (x,y) with each position between 1 and 4)
    # return None
    while True:
        x,y = ttt4_graphics.get_click()
        if has_mark(board,x,y) == False:
            move = str(x)+','+str(y)
            #make_move(board,move,player)
            return move


    # while True:
    #     move = str(raw_input('Enter row,column (ex: 2,3) to make move.'))
    #     print move
    #     x = int(move[0])
    #     y = int(move[2])
    #     if move == 'q':
    #         exit(0)
    #     if has_mark(board,x,y) == False:
    #         return str(x) + "," + str(y) #int(move[0]),int(move[2])

def make_move (board,move,player):
    # FIX ME
    #
    # Returns a board where 'move' has been performed on 'board' by 
    #    'player'
    # Change can be done in place in 'board' or a new copy created
    # return None

    x = int(move[0])
    y = int(move[2])
    i = int(board.indexOfCoordinate(x,y))
    board.boardList[i] = player
    return board

def minimaxSearch (board,player):
    # FIX ME
    #
    # Select a move for the computer, when playing as 'player' (either 
    #   'X' or 'O')
    # Return the selected move (a tuple (x,y) with each position between 
    #   1 and 4)
    # return None

    win = has_win(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    elif done(board):
        return 0
    else:
        valueList = []
        for i in range(0,len(board.boardList)):
            if board.boardList[i] == '.':
                hypo = make_move(copy.deepcopy(board),board.coordinateOfIndex(i),player)
                valueList.append(minimaxSearch(hypo,other(player)))
        if player == 'X':
            return max(valueList)
        elif player == 'O':
            return min(valueList)

def computer_move (board,player):
    bestMove = (-1,None)
    for i in range(0,len(board.boardList)):
        if board.boardList[i] == '.':
            hypo = make_move(copy.deepcopy(board),board.coordinateOfIndex(i),player)
            value = minimaxSearch(hypo,other(player))
            if bestMove[1] == None:
                bestMove = (i,value)
            elif player == 'X' and value>bestMove[1]:
                bestMove = (i,value)
            elif player =='O' and value<bestMove[1]:
                bestMove = (i,value)
            print "move " + str(i) + " examined"
    print bestMove
    ttt4_graphics.display_mark(bestMove[0],bestMove[1],player)
    return board.coordinateOfIndex(bestMove[0])

def other (player):
    if player == 'X':
        return 'O'
    return 'X'


def run (boardString,player,playX,playO): 
    board1 = create_board(boardString)

    print_board(board1)

    while not done(board1):
        if player == 'X':
            move = playX(board1,player)
        elif player == 'O':
            move = playO(board1,player)
        else:
            fail('Unrecognized player '+player)
        board1 = make_move(board1,move,player)
        print_board(board1)
        player = other(player)

    winner = has_win(board1)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'
        
# def main ():

#     ttt4_graphics.create_grid()
#     brd = create_board(testString)
    
#     print_board(brd)

#     while not done(brd):
#         move = ttt4_graphics.get_click()
#         #print "Use the arrow keys to specify which direction the block should move"
        
#         # move = read_player_input(brd,location,player)
#         print move
#         if move != None:
#             brd = make_move(brd,move,player)
#             ttt4_graphics.display_mark(int(move[0]),int(move[2]),player)
#             print_board(brd)

#     print 'YOU WIN! (Yay...)\n'


PLAYER_MAP = {
    'human': read_player_input,
    'computer': computer_move
}

if __name__ == '__main__':
    # main()

    run('.OOXXXOOXXXO....', 'X', computer_move, read_player_input)