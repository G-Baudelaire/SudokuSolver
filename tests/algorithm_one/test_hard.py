import os
from unittest import TestCase

import numpy

from main import sudoku_solver
from data.sudoku_loader import SudokuLoader


class TestHard(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_hard_0(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[0]
        solution = self.sudoku_loader.load_solved_sudoku(3)[0]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_1(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[1]
        solution = self.sudoku_loader.load_solved_sudoku(3)[1]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_2(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[2]
        solution = self.sudoku_loader.load_solved_sudoku(3)[2]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_3(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[3]
        solution = self.sudoku_loader.load_solved_sudoku(3)[3]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_4(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[4]
        solution = self.sudoku_loader.load_solved_sudoku(3)[4]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_5(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[5]
        solution = self.sudoku_loader.load_solved_sudoku(3)[5]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_6(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[6]
        solution = self.sudoku_loader.load_solved_sudoku(3)[6]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_7(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[7]
        solution = self.sudoku_loader.load_solved_sudoku(3)[7]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_8(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[8]
        solution = self.sudoku_loader.load_solved_sudoku(3)[8]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_9(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[9]
        solution = self.sudoku_loader.load_solved_sudoku(3)[9]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_10(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[10]
        solution = self.sudoku_loader.load_solved_sudoku(3)[10]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_11(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[11]
        solution = self.sudoku_loader.load_solved_sudoku(3)[11]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_12(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[12]
        solution = self.sudoku_loader.load_solved_sudoku(3)[12]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_13(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[13]
        solution = self.sudoku_loader.load_solved_sudoku(3)[13]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_hard_14(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(3)[14]
        solution = self.sudoku_loader.load_solved_sudoku(3)[14]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))
