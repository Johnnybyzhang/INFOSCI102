class Block:
    def __init__(self, x:int=0, y:int=0, type:int=0):
        self.shapes = \
            [
                [                   # L shape
                    [[1, 0, 0, 0],    
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
                     [0, 0, 0, 0]]
                ],
             
                [                   # I shape
                    [[1, 0, 0, 0],    
                     [1, 0, 0, 0],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0]],
                    
                    [[1, 1, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 0, 0, 0],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0]],
                    
                    [[1, 1, 1, 1],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
                ],
             
                [                   # O shape
                    [[1, 1, 0, 0],    
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
                ],
             
                [                   # T shape
                    [[0, 1, 0, 0],   
                     [1, 1, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                        
                    [[0, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                ],
             
                [                   # S shape
                    [[0, 1, 1, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[0, 1, 1, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]
                ],
                
                [                   # Z shape
                    [[1, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 0]]
                ],
                
                [                   # J shape
                    [[0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 1, 0, 0],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 0]],
                    
                    [[1, 0, 0, 0],
                     [1, 1, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
                ]
            ] 

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
        if self.x <0 :
            self.x = 0
        return
    
    # return current shape of the block
    def getShape(self)->"list[list[int]]":
        '''
        None -> 2DList
        
        return the shape of the block
        '''
        return self.shapes[self.type][self.current_direction]

    def getFormattedShape(self)->"str":
        '''
        None -> str
        
        return the shape of the block in string format
        '''
        shape = self.getShape()
        result = ""
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j]:
                    result += "X"
                else:
                    result += " "
            result += "\n"
        return result