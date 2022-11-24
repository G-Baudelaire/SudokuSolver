from unittest import TestCase

import numpy as np

from data.sudoku_loader import SudokuLoader
from main import UNSOLVABLE_SUDOKU, sudoku_solver


class TestCompletedInvalid(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_completed_invalid_0(self):
        puzzle = np.arange(81).reshape(9, 9)
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(np.array_equal(UNSOLVABLE_SUDOKU, my_solution))
