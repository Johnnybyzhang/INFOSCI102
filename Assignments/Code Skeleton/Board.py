from Block import Block
import random
class Board:
    def __init__(self, width:int=10, hight:int=20):
        self.nextBlock = Block(type=random.randint(0,6),x=width//2+2)
        self.curBlock = Block(type=random.randint(0,6),x=width//2+2)
        self.width = width
        self.hight = hight
        self.stable = False
        self.score = 0
        self.board = [[0 for _ in range(width)] for _ in range(hight)] # board size: width by height (defaults to 10 * 20)
        
    
    # check if current block is valid
    def isBlockValid(self, x:int, y:int, rotate:bool=False)->bool:
        '''
        None -> bool
        
        Check if the current block is valid at position (x, y)
        '''
        def rotateHelper(x:int, y:int)->bool:
            '''
            None -> bool
            
            Check if the current block is valid at position (x, y) after rotation
            '''
            rotation = self.curBlock.current_direction
            self.curBlock.rotateLeft()
            isValid = self.isBlockValid(x, y)
            self.curBlock.current_direction = rotation
            return isValid
            
        if rotate:
            return rotateHelper(x, y)
        
        for i in range(4):
            for j in range(4):
                if (self.curBlock.getShape()[j][i]==0):
                    continue
                try:
                    if (self.curBlock.getShape()[j][i] and self.board[y + j][x + i]):
                        return False
                except IndexError:
                    return False
        return True
    
    def checkGameOver(self)->bool:
        '''
        None -> bool
        
        Check if the game is over
        '''
        for i in range(4):
            for j in range(4):
                if (self.curBlock.getShape()[j][i]):
                    if self.board[self.curBlock.y+j][self.curBlock.x+i]:
                        return True
        return False
    
    # move the block downward by 1 positon if the move is valid, otherwise do nothing 
    def tryMoveDown(self)->None:
        '''
        None -> None
        
        check if the block can move down by 1 position, if yes, move down, otherwise do nothing (flag this case for processing in next game tick)
        '''
        if self.isBlockValid(self.curBlock.x, self.curBlock.y +1):
            self.curBlock.moveDown()
            self.score += 10
        else:
            self.stable = True
        return
    
    def tryMoveRight(self)->None:   
        '''
        None -> None
        
        check if the block can move right by 1 position, if yes, move right, otherwise do nothing
        '''
        if self.isBlockValid(self.curBlock.x + 1 , self.curBlock.y):
            self.curBlock.moveRight()
        return
    
    def tryMoveLeft(self)->None:
        '''
        None -> None
        
        check if the block can move left by 1 position, if yes, move left, otherwise do nothing
        '''
        if self.isBlockValid(self.curBlock.x - 1, self.curBlock.y):
            self.curBlock.moveLeft()
        return
    
    def tryRotate(self)->None:
        '''
        None -> None
        
        check if the block can rotate, if yes, rotate, otherwise do nothing
        '''
        if self.isBlockValid(self.curBlock.x, self.curBlock.y, rotate=True):
            self.curBlock.rotateLeft()
        return
    
    def tryHardDrop(self)->None:
        '''
        None -> None
        
        drop the block to the bottom of the board
        '''
        while self.isBlockValid(self.curBlock.x, self.curBlock.y + 1):
            self.curBlock.moveDown()
        return
    
    def clearLine(self)->None:
        '''
        None -> None
        
        clear all the full lines
        '''
        counter = 0
        for i in range(self.hight):
            if sum(self.board[i]) == self.width:
                self.board.pop(i)
                counter += 1
                self.board.insert(0, [0 for _ in range(self.width)])
        if counter == 1:
            self.score += 100
        elif counter == 2:
            self.score += 300
        elif counter == 3:
            self.score += 500
        elif counter == 4:
            self.score += 800
        return
    
    # write current shape to the board permanently
    def dump(self)->None:
        for i in range(4):
            for j in range(4):
                if (self.curBlock.getShape()[j][i]):
                    self.board[self.curBlock.y+j][self.curBlock.x+i] = 1
        return

    # put a new block on the top of the board
    def putNewBlock(self)->None:
        self.curBlock = self.nextBlock
        self.nextBlock = Block(type=random.randint(0,6),x=self.width//2+2)
        self.stable = False
        return
    
    # return the current board with block on it 
    def toString(self)->str:
        tmp = [self.board[i][:] for i in range(self.hight)] #updated for any*any board
        for i in range(4):
            for j in range(4):
                if self.curBlock.getShape()[j][i]:
                    tmp[self.curBlock.y+j][self.curBlock.x+i]=1
        
        screen = ""
        
        for line in tmp:
            for char in line:
                if char == 1:
                    screen += "X"
                else:
                    screen += "_"
            screen += "\n"
        
        return screen

    def gameOver(self)->bool:
        if self.board[0][4] == 1 or self.board[0][5] == 1:
            if self.blockStuck == True:
                return True
        return False
