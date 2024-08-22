import unittest
from logics_2048 import get_number_from_index, get_empty_list, get_index_from_number, \
                   is_zero_in_mas, move_left, move_right, move_up, move_down, can_move


class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1,2), 7)

    def test_2(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas  = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_3(self):
        a = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas  = [
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_3(self):
        a = []
        mas  = [
            [1,1,1,1],
            [1,1,4,1],
            [1,1,2,1],
            [3,4,1,1],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        self.assertEqual(get_index_from_number(1), (0,0))

    def test_5(self):
        self.assertEqual(get_index_from_number(15), (3,2))                 
  
    def test_6(self):
        mas  = [
            [1,1,1,1],
            [1,1,4,1],
            [1,1,2,1],
            [3,4,1,1],
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_7(self):
        mas  = [
            [0,1,1,1],
            [1,1,0,1],
            [1,1,2,1],
            [3,0,1,1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)
    
    def test_8(self):
        mas  = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)
        
    def test_9(self):
        mas  = [
            [2,4,4,2],
            [4,0,0,2],
            [0,0,0,0],
            [8,8,4,4],
        ]
        res  = [
            [2,8,2,0],
            [4,2,0,0],
            [0,0,0,0],
            [16,8,0,0],
        ]
        self.assertEqual(move_left(mas), (res, 32, True))

    def test_10(self):
        mas  = [
            [0,0,2,0],
            [4,0,0,2],
            [0,0,0,0],
            [8,8,4,4],
        ]
        res  = [
            [2,0,0,0],
            [4,2,0,0],
            [0,0,0,0],
            [16,8,0,0],
        ]    
        self.assertEqual(move_left(mas), (res, 24, True))
    
    def test_11(self):
        mas  = [
            [2,4,0,2],
            [2,0,2,0],
            [4,2,2,4],
            [4,4,0,0],
        ]
        res  = [
            [4,4,4,2],
            [8,2,0,4],
            [0,4,0,0],
            [0,0,0,0],
        ]    
        self.assertEqual(move_up(mas), (res, 16, True))

    def test_12(self):
        mas  = [
            [0,0,2,0],
            [4,0,0,2],
            [0,0,0,0],
            [8,8,4,2],
        ]
        res  = [
            [4,8,2,4],
            [8,0,4,0],
            [0,0,0,0],
            [0,0,0,0],
        ]    
        self.assertEqual(move_up(mas), (res, 4, True))
    
    def test_13(self):
        mas  = [
            [0,0,2,0],
            [4,0,0,2],
            [0,0,0,0],
            [8,8,4,2],
        ]
        res  = [
            [0,0,0,0],
            [0,0,0,0],
            [4,0,2,0],
            [8,8,4,4],
        ]    
        self.assertEqual(move_down(mas), (res, 4, True))

    def test_14(self):
        mas  = [
            [0,0,2,0],
            [4,0,0,2],
            [0,0,0,0],
            [8,8,4,2],
        ]
        res  = [
            [0,0,0,0],
            [0,0,0,0],
            [4,0,2,0],
            [8,8,4,4],
        ]    
        self.assertEqual(can_move(mas), True)

    def test_15(self):
        mas  = [
            [1,2,23,4],
            [5,4,1,5],
            [55,3,2,5],
            [8,8,4,2],
        ]
        res  = [
            [0,0,0,0],
            [0,0,0,0],
            [4,0,2,0],
            [8,8,4,4],
        ]    
        self.assertEqual(can_move(mas), False)

    def test_16(self):
        mas  = [
            [2,2,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        res  = [
            [0,0,0,4],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]    
        self.assertEqual(move_right(mas), (res, 4, True))
    
    def test_16(self):
        mas  = [
            [2,2,0,0],
            [0,0,0,0],
            [0,16,16,0],
            [2,0,0,2],
        ]
        res  = [
            [0,0,0,4],
            [0,0,0,0],
            [0,0,0,32],
            [0,0,0,4],
        ]    
        self.assertEqual(move_right(mas), (res, 40, True))         

if __name__ == '__main__':
    unittest.main()