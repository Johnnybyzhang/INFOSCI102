from Block import Block
import random
class Board:
    def __init__(self, width:int=10, hight:int=20):
        self.next_block = Block()
        self.cur_block = Block()
        self.width = width
        self.hight = hight
        self.board = [[0 for _ in range(width)] for _ in range(hight)] # 10 * 20 board
        
    
    # check if current block is valid
    def isBlockValid(self, x:int, y:int)->bool:
        '''
        None -> bool
        
        Check if the current block is valid at position (x, y)
        '''
        for i in range(4):
            for j in range(4):
                try:
                    if (self.cur_block.getShape()[i][j] and self.board[x + i][y + j]):
                        return False
                except:
                    return False
        return True
    
    
    
    # move the block downward by 1 positon if the move is valid, otherwise do nothing 
    def tryMoveDown(self)->None:
        '''
        None -> None
        
        check if the block can move down by 1 position, if yes, move down, otherwise do nothing (flag this case for processing in next game tick)
        '''
        if self.isBlockValid(self.cur_block.x, self.cur_block.y +1):
            self.cur_block.moveDown()
        else:
            self.blockStuck = True
        return
    
    def tryMoveRight(self)->None:   
        '''
        None -> None
        
        check if the block can move right by 1 position, if yes, move right, otherwise do nothing
        '''
        if self.isBlockValid(self.cur_block.x + 1 , self.cur_block.y):
            self.cur_block.moveRight()
        return
    
    def tryMoveLeft(self)->None:
        '''
        None -> None
        
        check if the block can move left by 1 position, if yes, move left, otherwise do nothing
        '''
        if self.isBlockValid(self.cur_block.x - 1, self.cur_block.y):
            self.cur_block.moveLeft()
        return
    
    # write current shape to the board permanently
    def dump(self)->None:
        for i in range(4):
            for j in range(4):
                if (self.cur_block.getShape()[i][j]):
                    self.board[self.cur_block.x + i][self.cur_block.y + j] = 1
        self.blockDumped = True
        self.blockStuck = False
        return

    # put a new block on the top of the board
    def putNewBlock(self)->None:
        if self.blockDumped == True:
            self.cur_block = self.next_block
            self.next_block = Block()
        return
    
    # return the current board with block on it 
    def toString(self)->str:
        tmp = [self.board[i][:] for i in range(20)] #updated for 10*24 board
        for i in range(4):
            for j in range(4):
                if (self.cur_block.y + i < 10 and self.cur_block.x + j < 24 and self.cur_block.x + j >= 0):
                    tmp[self.cur_block.y + i][self.cur_block.x + j] = self.cur_block.getShape()[i][j]
        
        screen = ""
        
        for line in tmp:
            for char in line:
                if char == 1:
                    screen += "X"
                else:
                    screen += " "
            screen += "\n"
        
        return screen

    def gameOver(self)->bool:
        if self.board[0][4] == 1 or self.board[0][5] == 1:
            if self.blockStuck == True:
                return True
        return False
