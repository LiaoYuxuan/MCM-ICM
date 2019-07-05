import unittest
# 导入文件最好这么写，直接import无法进行多个测试
from Binary_Search import *


class TestBinarySearch(unittest.TestCase):

    # 函数名必须以test开头，否则无法进行测试
    # 一个method中无论写多少，都显示Run 1 test
    # 有时候运行不会检查出错误是因为测试样本不够普遍
    def test_binary_search_iterative(self):
        data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
        self.assertEqual(binary_search_iterative(data, 28), 13)
        self.assertEqual(binary_search_iterative(data, 2), 0)
        self.assertEqual(binary_search_iterative(data, 98), 'not found')
        self.assertEqual(binary_search_iterative(data, 12), 6)

    def test_linear_search(self):
        data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
        self.assertEqual(linear_search(data, 28), 13)
        self.assertEqual(linear_search(data, 2), 0)
        self.assertEqual(linear_search(data, 98), 'not found')
        self.assertEqual(linear_search(data, 12), 6)


# 在终端运行python test_binarysearch.py即可或者在编译器中运行
if __name__ == '__main__':
    unittest.main()
