# Sudoku Solver

## How to use

Pass a 9 by 9 Numpy Array representing the sudoku board to

```Python
sudoku_solver(sudoku)
```

## Design Process

There were two implementations of the program with each utilising a backtracking depth first search and constraint
propagation

## Initial Attempt

Initially I chose a fairly naive process by reading the sudoku board from left to right, top to bottom. Each time a 0
(zero) was found, convert the row, column and sector of position into sets and find their intersect excluding 0 (zero)
to find the potential values of the unknown position. One each subsequent branch the value of the unknown would be
replaced with one of the potential values. This process continued until an unsolved position had no potential at which
point the program would backtrack and try the next potential value of the parent branch.

Although this method was viable it was extremely slow taking up to 150 seconds to solve some provided hard puzzles.

To combat this I implemented two kinds of optimisations. Algorithmic optimisations and implementation optimisations, the
difference being one improves the algorithms as a whole, the other is purely an improvement how it is articulated in the
code of the program. e.g. Utilising

```Python
foo.insert(len(foo), bar)
```

as opposed to

```Python
foo.append(bar)
```

as I found in testing that it was faster. These kinds of optimisations were imperative to utilise in my second
implementation to reach my goal speed. I will only go over the algorithmic improvements as they were repurposed in my
later implementation.

Firstly, at each branch I chose to find the unsolved position with the least potential values in order to reduce the
branching factor of the program and implicitly tells the program to focus on the positions more likely to be the
limiting factor in a given permutation of potential solutions. This alone brought the running time for each test to be
less than ten (10) seconds however this was still an order of magnitude above the goal of one (1) second.

The slowness of this program comes from multiple inefficiencies. Firstly, finding the potential values of every single
unsolved position results in performing a computationally expensive action every branch by converting each row, column
and sector to sets and finding their intersection. Secondly, each branch has a new copy of the board so the action of
creating a deepcopy both wastes time and increases space complexity - although in the specification space complexity did
not seem to be an evaluated aspect so through my implementation runtime was prioritised over memory usage.

## The Chad Algorithm (Chalgorithm)

To reduce the number of checks one can find the unused values in each row, column and sector. With this information we
solve two issues of the previous implementation. It is no longer necessary to find what the potential values are from
scratch each branch as we are continually tracking the potential values of each row, column and sector as we go along.
This means a single intersection of sets is all that is necessary to find the potential values of an unsolved position
and on each branch the value we used can be removed from the sets, then added back after exploring the branch. A side
effect of this is that since we no longer need to query the board we can simply stop using it, saving space and time as
a deepcopy is no longer needed.

#### Example

```Python
[[1, 0, 3, 4, 5, 8, 9, 0, 7],
 [4, 5, 8, 9, 6, 7, 1, 2, 3],
 [9, 6, 7, 1, 2, 3, 8, 4, 5],
 [2, 3, 1, 6, 4, 9, 7, 5, 8],
 [6, 4, 5, 7, 8, 1, 3, 9, 2],
 [8, 7, 9, 5, 3, 2, 6, 1, 4],
 [3, 1, 2, 8, 9, 4, 5, 7, 6],
 [5, 9, 4, 3, 7, 6, 2, 8, 1],
 [7, 8, 6, 2, 1, 5, 4, 3, 9]]
```

- `rows = [{2, 6}, {}, {}, {}, {}, {}, {}, {}, {}]`
- `columns = [{2}, {}, {}, {}, {}, {}, {}, {6}, {}]`
- `sectors = [{2}, {}, {6}, {}, {}, {}, {}, {}, {}]`

```Python
# A method in Class SampleSpace
def find_intersection(self, position: np.ndarray) -> Set[int]:
    i, j = position
    k, m = position // 3
    return self._rows[i].intersection(self._columns[j], self._sectors[(k * 3) + m])
```

Using `find_intersection([0, 1])` will return the set `{2}`. It's much

## Optimisations

### Backtracking

Core of the back tracking process.

```Python
    def _process(self) -> Iterator["Branch"]:


if len(self._unsolved_positions) == 0:
    yield self._get_branch(self._branched_values, True)

for i in self._branch():
    yield i

if self._root:
    raise NoSolutionError

yield self._parent


def _branch(self) -> Iterator["Branch"]:
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
```

When there are no unsolved positions left, yield a branch which will terminate the searching progress as goal has been
found.

```Python
if len(self._unsolved_positions) == 0:
    yield self._get_branch(self._branched_values, True)
```

Otherwise, find the unsolved position with the least potential values. For each potential value, yield a Branch where
the potential value was chosen. The value is removed from the sample space and added to branched values while the Branch
is being explored. This process is undone for each Branch.

```Python
for i in self._branch():
    yield i


def _branch(self) -> Iterator["Branch"]:
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
```

Should all potential values be explored then we must backtrack to the parent Branch. The root Branch will not have a
parent Branch, so instead it will raise a NoSolutionError as all branches of the tree have been explored.

```Python
if self._root:
    raise NoSolutionError

yield self._parent
```

### Constraint Propagation

Utilising a sample space means the potential values of a position can be evaluated without querying the sudoku board.
Saving time as the board does not require a deepcopy every branch, nor does it have to be read.

### Reducing Branching Factor

By choosing the unsolved position with the least potential values means we can reduce the average branching factor of
the algorithm.

```Python
unsolved_position = self._find_unsolved_position_with_least_branches()
```

### Eliminating Usage of copy() and append()

Mutating the sample space and branched values as opposed to copying them reduced the run time significantly. Copying the
values in the sample space and branched values have complexity, O(n<sup>2</sup>) and O(n) respectively. Therefore,
removing and adding values on each branch is more efficient as they are both O(1) processes. A positive side effect is
that the space complexity is reduced.

Insert is used rather than append as I found there was a time save likely coming from checks used in the implementation
of append.

```Python
for i in potential_values:
    self._manager.remove(unsolved_position, i)
    self._branched_values.insert(len(self._branched_values), i)
    yield self._get_branch(self._branched_values, False)
    self._manager.add(unsolved_position, i)
    self._branched_values.pop()

self._order.pop()
self._unsolved_positions.insert(0, unsolved_position)
```

### Custom Min Function

Utilising the `enumerate(self._unsolved_positions)` loop rather than
using `min(self._unsolved_positions, key=lambda x:)` is because searching a list for a numpy array would be more
computationally expensive as I would have to convert each array to a
list. `self._unsolved_positions.sort(key=lambda x:)` was originally used but as only the first element was needed
sorting the entire list was a redundant calculation.

```Python
    def _find_unsolved_position_with_least_branches(self) -> np.ndarray:


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
```

## Edge Cases

### Full Grid

If completed grid is invalid a board filled with -1s: `UNSOLVABLE_SUDOKU = np.full((9, 9), -1, dtype=int)` is returned.
Otherwise, the completed grid is just returned.

### Empty Grid

Generates a solved sudoku but due to the use of the set object, the output is not standardised and could vary from
system to system.

## References

Alex Dawkins, 2021, _sudoku_solver_ [Online]. Available
from: https://github.com/ouked/sudoku_solver/blob/master/README.md [Accessed 5 December 2021]