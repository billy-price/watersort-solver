#!/usr/bin/env python3

import solver
import tubeio

# Enter a tubes state as a list of lists of prefixes of the following colours
# blue, brown, cyan, emerald, gray, mint
# orange, olive, pink, purple, red, yellow

TUBES_EASY = tubeio.read_tubes(
  [
    ['bl','bl','bl','re'],
    ['re','re','re','bl'],
    [],
    [],
  ]
)

TUBES_MED = tubeio.read_tubes(
  [
    ['bl','br','or','or'],
    ['bl','br','bl','br'],
    ['or','bl','br','or'],
    [],
    [],
  ]
)

TUBES_HARD = tubeio.read_tubes(
  [
    ['br','pi','ol','re'],
    ['re','mi','gr','ol'],
    ['or','em','br','re'],
    ['cy','gr','or','pi'],
    ['pu','br','pu','br'],
    ['gr','ye','ol','bl'],
    ['or','cy','pi','ye'],
    ['bl','mi','pu','mi'],
    ['mi','ol','em','em'],
    ['ye','re','bl','em'],
    ['pi','bl','cy','ye'],
    ['cy','pu','or','gr'],
    [],
    [],
  ]
)

TUBES_2000 = tubeio.read_tubes(
  [
    ['ol','mi','pi','gr'],
    ['mi','pu','ol','gr'],
    ['mi','gr','pi','cy'],
    ['bl','cy','re','pu'],
    ['or','ol','pu','bl'],
    ['cy','gr','bl','re'],
    ['pu','re','or','or'],
    ['cy','pi','mi','re'],
    ['or','pi','ol','bl'],
    [],
    [],
  ]
)

# print the solution to the terminal
# with move indicators
def show_solution(tubes, moves):
  prev_state = tubes
  for option, state in moves:
    s, _, t = option

    move_indicator = (
      min(s,t)*" " + ('↑' if s < t else '↓') +
      (max(s,t) - min(s,t) - 1)*" " + ('↓' if s < t else '↑') )
    print(" ".join(move_indicator))
    print(tubeio.show_tubes(prev_state, solver.TUBE_HEIGHT))
    print()
    prev_state = state

  print(tubeio.show_tubes(prev_state, solver.TUBE_HEIGHT))


def main():
  tubes = TUBES_MED
  print(tubeio.show_tubes(tubes, solver.TUBE_HEIGHT))
  moves, success = solver.solve(tubes)
  if success:
    print('gg ez win')
  else:
    print(':(')
  show_solution(tubes, moves)

if __name__ == '__main__':
  main()