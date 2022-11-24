import sys

import numpy as np
import os

print()


class SudokuLoader:
    def __init__(self):
        self._directory = os.path.dirname(os.path.realpath(__file__))

    def load_unsolved_sudoku(self, difficulty):
        sudoku_board_paths = {
            0: "very_easy_puzzle.npy",
            1: "easy_puzzle.npy",
            2: "medium_puzzle.npy",
            3: "hard_puzzle.npy"
        }
        return np.load(os.path.join(self._directory, sudoku_board_paths[difficulty]))

    def load_solved_sudoku(self, difficulty):
        sudoku_board_paths = {
            0: "very_easy_solution.npy",
            1: "easy_solution.npy",
            2: "medium_solution.npy",
            3: "hard_solution.npy"
        }
        return np.load(os.path.join(self._directory, sudoku_board_paths[difficulty]))
