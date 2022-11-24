import os
from unittest import TestCase

import numpy

from main import sudoku_solver
from data.sudoku_loader import SudokuLoader


class TestMedium(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_medium_0(self):
        os.getcwd()
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[0]
        solution = self.sudoku_loader.load_solved_sudoku(2)[0]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_1(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[1]
        solution = self.sudoku_loader.load_solved_sudoku(2)[1]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_2(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[2]
        solution = self.sudoku_loader.load_solved_sudoku(2)[2]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_3(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[3]
        solution = self.sudoku_loader.load_solved_sudoku(2)[3]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_4(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[4]
        solution = self.sudoku_loader.load_solved_sudoku(2)[4]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_5(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[5]
        solution = self.sudoku_loader.load_solved_sudoku(2)[5]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_6(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[6]
        solution = self.sudoku_loader.load_solved_sudoku(2)[6]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_7(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[7]
        solution = self.sudoku_loader.load_solved_sudoku(2)[7]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_8(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[8]
        solution = self.sudoku_loader.load_solved_sudoku(2)[8]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_9(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[9]
        solution = self.sudoku_loader.load_solved_sudoku(2)[9]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_10(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[10]
        solution = self.sudoku_loader.load_solved_sudoku(2)[10]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_11(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[11]
        solution = self.sudoku_loader.load_solved_sudoku(2)[11]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_12(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[12]
        solution = self.sudoku_loader.load_solved_sudoku(2)[12]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_13(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[13]
        solution = self.sudoku_loader.load_solved_sudoku(2)[13]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_medium_14(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(2)[14]
        solution = self.sudoku_loader.load_solved_sudoku(2)[14]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))
