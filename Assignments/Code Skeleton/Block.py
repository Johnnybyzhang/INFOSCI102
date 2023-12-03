class Block:
    import random
    def __init__(self, x:int=0, y:int=0, type:int=random.randint(0, 2)):
        self.shapes = \
            [[[[1, 0, 0, 0],    # L shape
               [1, 0, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]],

              [[0, 0, 1, 0],
               [1, 1, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
             
              [[1, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],

              [[1, 1, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]],
             
             [[[1, 0, 0, 0],    # I shape
               [1, 0, 0, 0],
               [1, 0, 0, 0],
               [1, 0, 0, 0]],
              
              [[1, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
              
              [[0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0]],
              
              [[0, 0, 0, 0],
               [1, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]],
             
             [[[0, 0, 0, 0],    # Square shape
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],
              
              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],
              
              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],
              
              [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]]]]
             

        self.x = x
        self.y = y
        self.type = type
        self.current_direction = 0
        
    # rotate the current block counterclockwise by 90 degree
    def rotateLeft(self)->None:
        '''
        None -> None
        
        rotate the current block counterclockwise by 90 degree
        '''
        self.current_direction = (self.current_direction + 1) % 4
        return
    
    # move the current block downward by one
    def moveDown(self)->None:
        '''
        None -> None
        
        move the current block downward by one
        '''
        self.y += 1
        return
    
    # move the current block rightward by one
    def moveRight(self)->None:
        '''
        None -> None
        
        move the current block rightward by one
        '''
        self.x += 1
        return
    
    # move the current block leftward by one 
    def moveLeft(self)->None:
        '''
        None -> None
        
        move the current block leftward by one
        '''
        self.x -= 1
        return
    
    # return current shape of the block
    def getShape(self)->"list[list[int]]":
        return self.shapes[self.type][self.current_direction]
