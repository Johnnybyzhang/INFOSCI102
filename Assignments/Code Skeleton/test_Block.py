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
            self.assertEqual(board.isBlockValid(20, 0), False)
            self.assertEqual(board.isBlockValid(0, 10), True)
            self.assertEqual(board.isBlockValid(20, 10), False)
            
        def test_tryMoveDown(self):
            board = Board()
            self.assertEqual(board.curBlock.y, 0)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 1)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 2)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 3)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 4)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 5)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 6)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 7)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 8)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 9)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 10)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 11)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 12)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 13)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 14)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 15)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 16)
            board.tryMoveDown()
            self.assertEqual(board.curBlock.y, 17)
            board.tryMoveDown()
            self.assertLessEqual(board.curBlock.y, 18)
            board.tryMoveDown()
            self.assertLessEqual(board.curBlock.y, 18)
            board.dump()
            self.assertGreater(sum([sum(x) for x in board.board]),0)

if __name__ == '__main__':
    unittest.main()
