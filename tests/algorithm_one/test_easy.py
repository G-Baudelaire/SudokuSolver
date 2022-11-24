from unittest import TestCase

import numpy

from data.sudoku_loader import SudokuLoader
from main import sudoku_solver


class TestEasy(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_easy_0(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[0]
        solution = self.sudoku_loader.load_solved_sudoku(1)[0]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_1(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[1]
        solution = self.sudoku_loader.load_solved_sudoku(1)[1]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_2(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[2]
        solution = self.sudoku_loader.load_solved_sudoku(1)[2]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_3(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[3]
        solution = self.sudoku_loader.load_solved_sudoku(1)[3]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_4(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[4]
        solution = self.sudoku_loader.load_solved_sudoku(1)[4]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_5(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[5]
        solution = self.sudoku_loader.load_solved_sudoku(1)[5]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_6(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[6]
        solution = self.sudoku_loader.load_solved_sudoku(1)[6]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_7(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[7]
        solution = self.sudoku_loader.load_solved_sudoku(1)[7]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_8(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[8]
        solution = self.sudoku_loader.load_solved_sudoku(1)[8]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_9(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[9]
        solution = self.sudoku_loader.load_solved_sudoku(1)[9]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_10(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[10]
        solution = self.sudoku_loader.load_solved_sudoku(1)[10]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_11(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[11]
        solution = self.sudoku_loader.load_solved_sudoku(1)[11]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_12(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[12]
        solution = self.sudoku_loader.load_solved_sudoku(1)[12]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_13(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[13]
        solution = self.sudoku_loader.load_solved_sudoku(1)[13]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_easy_14(self):
        puzzle = self.sudoku_loader.load_unsolved_sudoku(1)[14]
        solution = self.sudoku_loader.load_solved_sudoku(1)[14]
        my_solution = sudoku_solver(puzzle)
        self.assertTrue(numpy.array_equal(solution, my_solution))
