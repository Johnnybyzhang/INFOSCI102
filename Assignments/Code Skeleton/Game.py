from Board import Board
from KBHit import KBHit
from time import time
from threading import Thread
import curses
class Game:
    def __init__(self, tickrate=2, highscore = 0, gliched = False):
        self.board = Board ()
        self.kb = KBHit() # a class that read input from the keyboard
        self.tickrate = tickrate # number of ticks per second
        self.go = -1
        self.gameOver = False
        self.gameQuit = False
        self.control = []
        self.pause = False
        self.gliched = gliched
        self.highscore = highscore
        #gameState = enumerate() # reserved for future improvements
        # Initializing curses window
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    # start the game
    
    def doGameOver(self)->None:
        '''None -> None
        This function is called when the game is over, handles the highscore.'''
        if self.board.score > self.highscore:
            self.highscore = self.board.score
        return
    
    def run(self)->None:
        print(f"Starting game with tickrate: {self.tickrate}")
        tick = time()
        while (not self.gameQuit):
            while (not self.gameOver):
                if self.kb.kbhit():
                    c = self.kb.getch()
                    if c == 'p':
                        self.pause = not self.pause
                    if c == 'q':
                        self.gameOver = True
                    
                    if self.gliched:            # gliched mode, where the controls are reversed
                        if c == 'a':
                            self.control.append('d')
                        elif c == 'd':
                            self.control.append('a')
                        elif c == 's':
                            self.control.append('w')
                        elif c == 'w':
                            self.control.append('s')
                        else:
                            self.control.append(c)
                    else:
                        self.control.append(c)
                if (time() - tick >= 1/self.tickrate and not self.pause):
                    tick = time()
                    self.tick()
            self.doGameOver()
            while self.gameOver:
                if self.gameQuit:
                    break
                if self.kb.kbhit():
                    c = self.kb.getch()
                    if c == 'q':
                        self.gameQuit = True
                    if c == 'r':
                        self.gameOver = False
                        self.board = Board()
                        self.go = -1
                        self.control = []
                        self.pause = False
                        tick = time()
                if (time() - tick >= 1/self.tickrate and not self.pause):
                    tick = time()
                    self.tick()
        # Finalizing curses window before exiting
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        return
    
    
    
    # print board on the command line
    def display(self)->None:
        self.stdscr.clear()  # Clear the window to prevent scrolling
        if not self.gameOver:
            lines = self.board.toString().split('\n')
            for i in range(len(lines)):
                self.stdscr.addstr(i+2, 2, lines[i])
            nextBlock = self.board.nextBlock.getFormattedShape().split('\n')
            self.stdscr.addstr(1, 20, "Next Block:")
            for i in range(len(nextBlock)):
                self.stdscr.addstr(i+2, 20, nextBlock[i])
        else:
            self.stdscr.addstr(2, 2, "GAME OVER")
            self.stdscr.addstr(3, 2, f"Your score is {self.board.score}")
            self.stdscr.addstr(4, 2, f"Your highest score is {self.highscore}")
            self.stdscr.addstr(5, 2, "Press 'r' to restart or 'q' to quit")
        self.stdscr.addstr(0,2,f"Score: {self.board.score}")
        self.stdscr.addstr(0,20,f"Highscore: {self.highscore}")
        self.stdscr.refresh()  # Refresh the window to update the display
        return

    def tick(self)->None:
        if not self.gameOver:
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