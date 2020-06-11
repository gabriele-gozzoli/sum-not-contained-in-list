"""
Given a list of integers, check if the sum of any two integers in the list is not contained in the list.
For example with the list [4, 5, 15, 2, 8], there is no pair of integers where their sum is in the list.
The list [8, 7, 5, 3] does not satisfy the criteria since the sum of 5 and 3 is in the list.
Write a function which takes a list of integers and returns True if the list satisfies the criteria above,
or False otherwise.
"""

from typing import List
from unittest import TestCase


def sum_not_contained_in_list(integers: List[int]) -> bool:
    pass


class Test(TestCase):

    def test_satisfy_1(self):
        integers = [4, 5, 15, 2, 8]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(True, result)

    def test_satisfy_2(self):
        integers = [14, 2, -4, 7, 8, -3]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(True, result)

    def test_satisfy_3(self):
        integers = [1, 5, 3, 7, 13, -11, 19]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(True, result)

    def test_not_satisfy_1(self):
        integers = [8, 7, 5, 3]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(False, result)

    def test_not_satisfy_2(self):
        integers = [7, 5, 3, 0]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(False, result)

    def test_not_satisfy_3(self):
        integers = [7, 1, 2, -1]
        result = sum_not_contained_in_list(integers=integers)
        self.assertEqual(False, result)
