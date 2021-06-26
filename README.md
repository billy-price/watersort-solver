# Solver for Water Sort Puzzle

This game is stupid and wastes my time so I made a dead simple backtracking solver so that I have no reason to play it ever again.

- [iOS app](https://apps.apple.com/us/app/water-sort-puzzle/id1514542157)
- disable ads by removing the app's mobile data permission and then turning off wifi

## Rules
- There are `(n+2)`-`tubes`, each stacked with up to `m` (usually `4`) `cells` of liquid. Each `cell` of liquid is one of `n` colours (for the usual `n=12`, `blue, brown, cyan, emerald, gray, mint, orange, olive, pink, purple, red, yellow`)
- Adjacently stacked `cells` combine to form a `chunk`
- The `top chunk`of a tube is the largest `chunk` of the tube who's top `cell` is at the top of the tube
- There are `m` of each colour amongst all tubes
- The aim is to reach a `solved state` using only `valid move`'s.

### Solved State
Let `num_distinct(tube)` be the number of distinct colours amongst the cells in the tube if it's non-empty, and `1` if the tube is empty. The `tubes` are in a `solved state` iff every tube has `num_distinct(tube)=1`

### Valid Move
- A `move` is a selection of a `source tube` and `target tube`
- A `move` is a `valid move` iff the following conditions hold
  - The source `tube` is non-empty
  - The top cells of both tubes have the same colour OR the `target tube` is empty
- The `move chunk` associated to a `valid move` is a pair `(c,n)`, where `c` is the colour of the top cell of the `source tube`, and `n` is `min(num_cells(top_chunk(source_tube)), m - num_cells(target_tube))`. In simpler terms, it's the maximum amount of the top chunk of the `source tube` that can be poured into the `target tube`
- The `result` of a `valid move` is a modified state of the `tubes`, such that if the `move chunk` of the `valid move` is `(c,n)` the target tube has `n` more cells of colour `c` on top, and `source tube` has `n` less cells of `c` on top. The remaining tubes are fixed. In other words, pour as much of the `top chunk` of the `source tube` into the `target tube` up the to capacity of `m`, leaving the rest as is in the `source tube`.

## Solving Strategy

Only guiding strategy to the backtracking search is:
1. Never divide multi-cell chunks between tubes - i.e. every `move chunk` is the entire `top chunk` of the `source tube`
2. Don't empty an entire `source tube` (the `top chunk` is the entire `source tube`) into an empty `target tube`.

This strategy will always terminate, because every move 'makes progress' - i.e. always combining two of the same colour to form a larger chunk or separating two distinct colours. In fact the value of `sum(map(num_distinct, tubes))` is always non-negative integer and decreases on every move (remember `num_distinct` of an empty tube is `1`). Whether or not all solvable start state of tubes will be solved by this strategy, is unclear but seems plausible. This could be proven if every solvable start state of tubes has a solution satisfying point (1) of the strategy ((2) is trivially easy to obtain).

## Usage

Add a new puzzle state to solve in `main.py` (and edit the `main` method to point to your puzzle). A `tubes` state is a list of lists of colours cells, where each colour cell can be entered as any prefix of the colour set `blue, brown, cyan, emerald, gray, mint, orange, olive, pink, purple, red, yellow`. Each list is a bottom-to-top representation of a `tube`. For example, to entire the start state (`orange = 7, brown = 2, blue = 1`):
```
7 2 7    
7 1 2    
2 2 1    
1 1 7 _ _
```
do this:
```python
TUBES_MED = tubeio.read_tubes(
  [
    ['bl','br','or','or'],
    ['bl','br','bl','br'],
    ['or','bl','br','or'],
    [],
    [],
  ]
)
```
Then run `main.py`, and the solution is printed to the terminal as a sequence of states, with the corresponding move indicated with arrows. Each state is printed as a visual representation of the tubes (each tube is vertical), where each cell is colour highlighted using the [`sty`](https://sty.mewo.dev) text colouring package. Your terminal may not support colour highlighting so the text of each cell is the hexadecimal value of the internal `int` representation of each colour.

Tube height can be modified in `solver.py`.

## Example Solution
```
↑     ↓
7 2 7
7 1 2
2 2 1
1 1 7 _ _

↑       ↓
  2 7
  1 2
2 2 1 7
1 1 7 7 _

  ↑     ↓
  2 7
  1 2
  2 1 7
1 1 7 7 2

↑ ↓
    7
  1 2
  2 1 7 2
1 1 7 7 2

↓ ↑
  1 7
  1 2
  2 1 7 2
_ 1 7 7 2

  ↑     ↓
    7
    2
1 2 1 7 2
1 1 7 7 2

↑ ↓
    7
    2   2
1   1 7 2
1 1 7 7 2

↓   ↑
    7
  1 2   2
  1 1 7 2
_ 1 7 7 2

↑     ↓

  1 2   2
  1 1 7 2
7 1 7 7 2

↓   ↑

  1 2 7 2
  1 1 7 2
_ 1 7 7 2

↑       ↓

  1   7 2
  1 1 7 2
2 1 7 7 2

↓   ↑
        2
  1   7 2
  1 1 7 2
_ 1 7 7 2

↑ ↓
        2
  1   7 2
  1   7 2
1 1 7 7 2

    ↑ ↓
  1     2
  1   7 2
  1   7 2
_ 1 7 7 2

  1   7 2
  1   7 2
  1   7 2
_ 1 _ 7 2
```