from unittest import TestCase

import numpy
import numpy as np

from data.sudoku_loader import SudokuLoader
from main import sudoku_solver, UNSOLVABLE_SUDOKU


class TestEmpty(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_empty(self):
        puzzle = np.zeros(81).reshape(9, 9)
        incorrect_solution = UNSOLVABLE_SUDOKU
        my_solution = sudoku_solver(puzzle)
        print(my_solution)
        self.assertFalse(numpy.array_equal(incorrect_solution, my_solution))
