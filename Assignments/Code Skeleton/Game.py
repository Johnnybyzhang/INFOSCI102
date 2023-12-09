from Board import Board
from KBHit import KBHit
from time import time
from threading import Thread
import curses
class Game:
    def __init__(self):
        self.board = Board ()
        self.kb = KBHit() # a class that read input from the keyboard
        self.tickrate = 2
        self.go = -1
        self.gameOver = False
        self.control = []
        #gameState = enumerate() # reserved for future improvements
        # Initializing curses window
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    # start the game
    def run(self)->None:
        print("Welcome to Tetris!")
        tick = time()
        while (not self.gameOver):
            if self.kb.kbhit():
                self.control.append(self.kb.getch())
            if (time() - tick >= 1/self.tickrate):
                tick = time()
                self.tick()
        # Finalizing curses window before exiting
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        print("Game Over!")
        return
    
    
    
    # print board on the command line
    def display(self)->None:
        self.stdscr.clear()  # Clear the window to prevent scrolling
        lines = self.board.toString().split('\n')
        for i in range(len(lines)):
            self.stdscr.addstr(i+2, 2, lines[i])
        self.stdscr.refresh()  # Refresh the window to update the display
        return

    def tick(self)->None:
        if self.board.stable:
            self.board.dump()
            self.board.putNewBlock()
            self.go=sum(self.board.board[0])
        
        if self.board.checkGameOver():
            self.gameOver = True
        
        while self.control:
            c = self.control.pop()
            if c == 'a':
                self.board.tryMoveLeft()
            elif c == 'd':
                self.board.tryMoveRight()
            elif c == 's':
                self.board.tryMoveDown()
            elif c == 'w':
                self.board.tryRotate()
            elif c == 'q':
                self.gameOver = True
            elif c == ' ':
                self.board.tryHardDrop()
        
        self.board.clearLine()
        self.board.tryMoveDown() # Try to move the block down by 1 position
        self.display() # Display the board
        return