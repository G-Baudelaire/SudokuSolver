from unittest import TestCase

import numpy

from main import sudoku_solver
from data.sudoku_loader import SudokuLoader


class TestCompleted(TestCase):
    def setUp(self) -> None:
        self.sudoku_loader = SudokuLoader()

    def test_completed_0(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[0]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_1(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[1]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_2(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[2]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_3(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[3]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_4(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[4]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_5(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[5]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_6(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[6]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_7(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[7]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_8(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[8]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_9(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[9]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_10(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[10]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_11(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[11]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_12(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[12]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_13(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[13]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))

    def test_completed_14(self):
        solution = self.sudoku_loader.load_solved_sudoku(3)[14]
        my_solution = sudoku_solver(solution)
        self.assertTrue(numpy.array_equal(solution, my_solution))
