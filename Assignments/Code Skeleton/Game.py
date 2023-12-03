from Board import Board
from KBHit import KBHit
from time import time
class Game:
    def __init__(self):
        self.board = Board ()
        self.kb = KBHit() # a class that read input from the keyboard
        self.tickrate = 10
        self.gameOver = False

    # start the game
    def run(self)->None:
        print("Welcome to Tetris!")
        tick = time()
        while (not self.gameOver):
            if (time() - tick >= 1/self.tickrate):
                tick = time()
                self.tick()
        return
    
    # print board on the command line
    def display(self)->None:
        print(self.board.toString())
        return

    def tick(self)->None:
        if self.board.dumpNeeded: # Dump the block from previous tick as needed
            self.board.dump()
            self.board.dumpNeeded(False)
        
        if self.board.dumped(): # If the block is dumped, put a new block on the board
            self.board.putNewBlock()
        
        if (self.board.isStuck()): # If the block is stuck, check if the game is over, else flag the block to dump in next game tick
            if self.board.gameOver():
                self.gameOver = True
            self.board.dumpNeeded(True)
            
        self.board.tryMoveDown() # Try to move the block down by 1 position
        self.display() # Display the board
        return