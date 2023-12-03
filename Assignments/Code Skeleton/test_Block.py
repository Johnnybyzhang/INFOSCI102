import unittest
from Block import Block
from Board import Board

class TestBlock(unittest.TestCase):
    
    def test_moveDown(self):
        block = Block()
        self.assertEqual(block.x, 0)
        self.assertEqual(block.y, 0)
        block.moveDown()
        self.assertEqual(block.y, 1)
        self.assertEqual(block.x, 0)
        
        
class TestBoard(unittest.TestCase):
        
        def test_isBlockValid(self):
            board = Board()
            self.assertEqual(board.isBlockValid(0, 0), True)
            self.assertEqual(board.isBlockValid(20, 0), True)
            self.assertEqual(board.isBlockValid(0, 10), False)
            self.assertEqual(board.isBlockValid(20, 10), False)
            
        def test_tryMoveDown(self):
            board = Board()
            self.assertEqual(board.cur_block.y, 0)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 1)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 2)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 3)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 4)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 5)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 6)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 7)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 8)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 9)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 10)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 11)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 12)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 13)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 14)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 15)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 16)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 17)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 18)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 19)
            board.tryMoveDown()
            self.assertEqual(board.cur_block.y, 20)
            

if __name__ == '__main__':
    unittest.main()
