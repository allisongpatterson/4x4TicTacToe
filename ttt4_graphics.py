from graphics import *

win = GraphWin("4x4 Tic-Tac-Toe", 600, 600) # names & sizes window (pixels)
win.setCoords( 0, 4, 4, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)

def create_grid():
    
    for i in range(0,4):
        ln = Line(Point(i,0),Point(i,4))
        ln.setWidth(4)
        ln.draw(win)

    for j in range(1,4):
        ln = Line(Point(0,j),Point(4,j))
        ln.setWidth(4)
        ln.draw(win)

def display_mark(x,y,player):

    if player == 'X':
        ln1 = Line(Point(x-0.95,y-0.95),Point(x-0.05,y-0.05))
        ln2 = Line(Point(x-0.95,y-0.05),Point(x-0.05,y-0.95))        
        ln1.setOutline('red')
        ln2.setOutline('red')
        ln1.setWidth(10)
        ln2.setWidth(10)
        ln1.draw(win)
        ln2.draw(win)

    if player == 'O':
        circ = Circle(Point(x-0.5,y-0.5), 0.45)
        circ.setOutline('blue')
        circ.setWidth(10)
        circ.draw(win)

def get_click():

    while True:
        p = win.getMouse()
        for i in range(0,4):
            if i < p.getX() < i+1:
                x = i+1
                for j in range(0,4):
                    if j < p.getY() < j+1:
                        y = j+1
                        return x,y