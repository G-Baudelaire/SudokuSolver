import collections
import itertools
from typing import *

import numpy as np

UNSOLVABLE_SUDOKU = np.full((9, 9), -1, dtype=int)


def sudoku_solver(sudoku: np.ndarray) -> np.ndarray:
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    if Reader.is_invalid(sudoku):
        return UNSOLVABLE_SUDOKU.copy()

    rows = Reader.find_potential_values_rows(sudoku)
    columns = Reader.find_potential_values_columns(sudoku)
    sectors = Reader.find_potential_values_sectors(sudoku)

    sample_space = SampleSpace(rows, columns, sectors)
    unsolved_positions = Reader.find_all_unsolved_positions(sudoku)
    branch = Branch(None, True, unsolved_positions, sample_space, list(), list(), False)

    try:
        while not branch.is_completed():
            branch = branch.run()
    except NoSolutionError:
        return UNSOLVABLE_SUDOKU.copy()

    for value, position in zip(branch.get_branched_values(), branch.get_order()):
        i, j = position
        sudoku[i][j] = value
    return sudoku


class Reader:
    _POTENTIAL_OPTIONS = {i for i in range(1, 10)}

    @staticmethod
    def get_sector(board: np.ndarray, sector: np.ndarray) -> np.ndarray:
        """
        Return a 3 x 3 numpy array of the 3 x 3 sectors on a sudoku board.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :param sector: Numpy array (2) with the position of the sector to be retrieved.
            Note: largest value should be [2, 2]
        :return: Numpy array (3 x 3) containing the values of the given sector.
        """
        i, j = sector * 3
        return board[i: i + 3, j: j + 3]

    @staticmethod
    def is_invalid(board: np.ndarray) -> bool:
        """
        Check sudoku board has no repeats in any rows, columns or sectors. Zero (0) is not included when looking for
        these repeats. Usage of 'or' is lazy reducing redundancy.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: Boolean stating whether the board has any invalid subsets (rows, columns and sectors).
        """
        return Reader._are_rows_invalid(board) or \
               Reader._are_columns_invalid(board) or \
               Reader._are_sectors_invalid(board)

    @staticmethod
    def _is_subset_invalid(subset: np.ndarray) -> bool:
        """
        Check subset of the sudoku board has no repeats.
        :param subset: Numpy array (9) representing a row, column or sector of the board.
        :return: Boolean stating whether there are repeats in the subset.
        """
        for key, value in collections.Counter(subset).items():
            if (1 < value) and (key != 0):
                return True
        return False

    @staticmethod
    def _are_rows_invalid(board: np.ndarray) -> bool:
        """
        Check if any rows are invalid. 'any()' is a lazy function, useful as no row is allowed to be invalid.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: Boolean stating whether any rows are invalid.
        """
        return any((Reader._is_subset_invalid(i) for i in board))

    @staticmethod
    def _are_columns_invalid(board: np.ndarray) -> bool:
        """
        Check if any columns are invalid. 'any()' is a lazy function, useful as no column is allowed to be invalid.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: Boolean stating whether any columns are invalid.
        """
        return any((Reader._is_subset_invalid(j) for j in board.transpose()))

    @staticmethod
    def _are_sectors_invalid(board: np.ndarray) -> bool:
        """
        Check if any sectors are invalid. 'any()' is a lazy function, useful as no sector is allowed to be invalid.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: Boolean stating whether any sectors are invalid.
        """
        return any((Reader._is_subset_invalid(Reader.get_sector(board, np.array(k)).flatten()) for k in
                    itertools.product(range(3), repeat=2)))

    @staticmethod
    def find_potential_values_rows(board: np.ndarray) -> List[Set]:
        """
        Check each row to find potential values the unsolved positions can take in each row.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: List of sets, each set containing the unassigned values for each row.
        """
        return [Reader._POTENTIAL_OPTIONS.difference(set(row)) for row in board]

    @staticmethod
    def find_potential_values_columns(board: np.ndarray) -> List[Set]:
        """
        Check each column to find potential values the unsolved positions can take in each column.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: List of sets, each set containing the unassigned values for each column.
        """
        return [Reader._POTENTIAL_OPTIONS.difference(set(column)) for column in board.transpose()]

    @staticmethod
    def find_potential_values_sectors(board: np.ndarray) -> List[Set]:
        """
        Check each sector to find potential values the unsolved positions can take in each sector.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: List of sets, each set containing the unassigned values for each sector.
        """
        return [
            Reader._POTENTIAL_OPTIONS.difference(set(Reader.get_sector(board, np.array(i)).flatten())) for i in
            itertools.product(range(3), repeat=2)
        ]

    @staticmethod
    def find_all_unsolved_positions(board: np.ndarray) -> List[np.ndarray]:
        """
        Search the board from left to right, top to bottom for positions missing values.
        :param board: Numpy array (9 x 9) of the sudoku board.
        :return: List of numpy arrays (2) with the positions that are missing values.
        """
        return [np.array([i, j]) for i, j in itertools.product(range(9), repeat=2) if board[i][j] == 0]


class SampleSpace:
    """
    Hold the potential values for each row, column and sector on the board. Has helper functions associated with such
    manipulations.
    """

    def __init__(self, rows: List[Set], columns: List[Set], sectors: List[Set]) -> NoReturn:
        """
        Initialize the sample_space object.
        :param rows: List of sets, each set containing the unassigned values for each row.
        :param columns: List of sets, each set containing the unassigned values for each column.
        :param sectors: List of sets, each set containing the unassigned values for each sector.
        """
        self._rows = rows
        self._columns = columns
        self._sectors = sectors

    def remove(self, position: np.ndarray, integer: int) -> NoReturn:
        """
        Remove integer from the sets that represent the potential values for the given position.
        :param position: Numpy array (2) of the position that being filled by the given integer.
        :param integer: Value to remove from the potential value sets.
        """
        i, j = position
        k, m = position // 3

        self._rows[i].remove(integer)
        self._columns[j].remove(integer)
        self._sectors[(k * 3) + m].remove(integer)

    def add(self, position: np.ndarray, integer: int) -> NoReturn:
        """
        Add integer from the sets that represent the potential values for the given position.
        :param position: Numpy array (2) of the position that being filled by the given integer.
        :param integer: Value to add to the potential value sets.
        """
        i, j = position
        k, m = position // 3

        self._rows[i].add(integer)
        self._columns[j].add(integer)
        self._sectors[(k * 3) + m].add(integer)

    def find_intersection(self, position: np.ndarray) -> Set[int]:
        """
        Find set of potential values a position can have. With those potential values being the intersection of the
        potential values for it's row, column and sector.
        :param position: Numpy array (2) of the position to find potential values for.
        :return: Set of integers with the potential values of the position.
        """
        i, j = position
        k, m = position // 3
        return self._rows[i].intersection(self._columns[j], self._sectors[(k * 3) + m])


class Branch:
    """
    Thing on a tree.
    """
    _reader = Reader

    def __init__(self,
                 parent: Union["Branch", None],
                 root: bool,
                 unsolved_positions: np.ndarray,
                 sample_space: SampleSpace,
                 branched_values: List[int],
                 order: List[np.ndarray],
                 completed: bool) -> NoReturn:
        self._parent = parent
        self._root = root
        self._unsolved_positions = unsolved_positions
        self._sample_space = sample_space
        self._branched_values = branched_values
        self._order = order
        self._completed = completed
        self._run = self._process()

    def is_completed(self) -> bool:
        """
        Getter for self._completed.
        :return: Boolean stating whether the search can be terminated.
        """
        return self._completed

    def get_branched_values(self) -> List[int]:
        """
        Getter for self._branched_values.
        :return: List of integers containing the values found in order of being found for a solution. Positions of
        integers correspond with self._order positions.
        """
        return self._branched_values

    def get_order(self) -> List[int]:
        """
        Getter for self._order.
        :return: Order the unsolved positions where evaluated in to find a solution.
        """
        return self._order

    def run(self) -> "Branch":
        """
        Find the next branch to evaluate in the process. This branch can be a child branch or a parent.
        :return: Child or parent branch object.
        """
        return next(self._run)

    def _process(self) -> Iterator["Branch"]:
        """
        Determine which Branch object to yield.
        When there are no unsolved positions the puzzle is solved.
        If all potential values have been explored than the we can backtrack to a parent branch. Should it be the root
        branch than we can raise a NoSolutionError.
        :return: Branch below or above the current branch.
        """
        if len(self._unsolved_positions) == 0:
            yield self._get_branch(self._branched_values, True)

        for i in self._branch():
            yield i

        if self._root:
            raise NoSolutionError

        yield self._parent

    def _branch(self) -> Iterator["Branch"]:
        # Honestly, pretty poorly worded but I'm extremely tired at this point :/
        """
        Find the unsolved position with the least number of potential options, subsequently choosing a position with the
        minimum possible branches. Then iterate through the positions potential values yielding a Branch object each
        time. Each iteration will remove the potential value from the sample space containing the potentials values and adds
        it to the branched values. It undoes those changes with each iteration.

        Note: .insert() is used as it seems to run faster than append.
        :return: Branch object.
        """
        unsolved_position = self._find_unsolved_position_with_least_branches()

        self._order.insert(len(self._order), unsolved_position)
        potential_values = self._sample_space.find_intersection(unsolved_position)

        for i in potential_values:
            self._sample_space.remove(unsolved_position, i)
            self._branched_values.insert(len(self._branched_values), i)
            yield self._get_branch(self._branched_values, False)
            self._sample_space.add(unsolved_position, i)
            self._branched_values.pop()

        self._order.pop()
        self._unsolved_positions.insert(0, unsolved_position)

    def _find_unsolved_position_with_least_branches(self) -> np.ndarray:
        """
        Find the unsolved position with the least potential values. Remove that unsolved position from the list of
        unsolved positions. This more bloated version is used as opposed to a min() due to the fact that finding the
        position of a numpy array in a list would probably more computationally expensive.
        :return: Numpy array (2) of an unsolved position with the least possible values.
        """
        unsolved_position = None
        pointer = None
        least_number_of_branches = float("inf")

        for index, position in enumerate(self._unsolved_positions):
            number_of_branches = len(self._sample_space.find_intersection(position))
            if number_of_branches < least_number_of_branches:
                unsolved_position = position
                pointer = index
                least_number_of_branches = number_of_branches

        self._unsolved_positions.pop(pointer)
        return unsolved_position

    def _get_branch(self, branched_values: List[int], completed: bool):
        """
        Wrapper function for initialising a Branch object.
        :param branched_values: Values chosen in order of when they were branched to.
        :param completed: Whether search can be terminated on this Branch.
        :return: Branch object.
        """
        return Branch(
            parent=self,
            root=False,
            unsolved_positions=self._unsolved_positions,
            sample_space=self._sample_space,
            branched_values=branched_values,
            order=self._order,
            completed=completed
        )


class NoSolutionError(Exception):
    pass
