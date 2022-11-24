import os
from unittest import TestCase

import numpy

from main import sudoku_solver
from data.sudoku_loader import SudokuLoader


class TestVeryEasy(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_very_easy_0(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[0]
        solution = self.sudoku_loader.load_solved_sudoku(0)[0]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_1(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[1]
        solution = self.sudoku_loader.load_solved_sudoku(0)[1]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_2(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[2]
        solution = self.sudoku_loader.load_solved_sudoku(0)[2]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_3(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[3]
        solution = self.sudoku_loader.load_solved_sudoku(0)[3]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_4(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[4]
        solution = self.sudoku_loader.load_solved_sudoku(0)[4]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_5(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[5]
        solution = self.sudoku_loader.load_solved_sudoku(0)[5]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_6(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[6]
        solution = self.sudoku_loader.load_solved_sudoku(0)[6]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_7(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[7]
        solution = self.sudoku_loader.load_solved_sudoku(0)[7]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_8(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[8]
        solution = self.sudoku_loader.load_solved_sudoku(0)[8]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_9(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[9]
        solution = self.sudoku_loader.load_solved_sudoku(0)[9]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_10(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[10]
        solution = self.sudoku_loader.load_solved_sudoku(0)[10]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_11(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[11]
        solution = self.sudoku_loader.load_solved_sudoku(0)[11]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_12(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[12]
        solution = self.sudoku_loader.load_solved_sudoku(0)[12]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_13(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[13]
        solution = self.sudoku_loader.load_solved_sudoku(0)[13]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_very_easy_14(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(0)[14]
        solution = self.sudoku_loader.load_solved_sudoku(0)[14]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))
