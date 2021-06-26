import tubeio

TUBE_HEIGHT = 4
COLOUR_VOLUME = 4

# colour : int
# tube : [colour]
# tubes : [tube]
# chunk : (colour,int)
# move : (int,chunk,int)

# returns chunk of colour at top of tube
# top_chunk(tube) = (c,n) <-> n-many c's on top of tube
def top_chunk(tube):
  if len(tube) == 0:
    return (0,0)
  n = 1
  c = tube[-1]
  while n < len(tube) and tube[-(n+1)] == c:
    n += 1
  
  return (c,n)

# decide if this is a good tube to try to pour from
def good_source(st):
  c,n =  top_chunk(st)
  return n != 0

# true iff can pour entire non-zero top chunk from stube to ttube
def good_move(st, tt):
  c,n = top_chunk(st)

  # illegal move
  if n == 0 or (len(tt) !=0 and tt[-1] != c): return False

  # pointless move
  if len(tt) == 0 and len(st) == n: return False

  # can move entire chunk -> good move
  return n + len(tt) <= TUBE_HEIGHT



# generate all good moves on the state of tubes
# move: (int,chunk,int)
# (s,ch,t) ∈ good_moves -> can move ch from tubes[s] to tubes[t]
def good_moves(tubes):
  for s, st in enumerate(tubes):
    if not good_source(st): continue

    for t, tt in enumerate(tubes):
      if t == s: continue
      
      if good_move(st, tt):
        yield (s,top_chunk(st),t)

# change the tubes state
# move chunk from tubes[s] to tubes[t]
def make_move(tubes, s, chunk, t):
  c,out = chunk
  while out > 0:
    tubes[t].append(tubes[s].pop())
    out -= 1

# change the tubes state
# move chunk from tubes[t] to tubes[s]
def undo_move(tubes, s, ch, t):
  make_move(tubes, t, ch, s)

# tubes is in a valid solved state
def is_solved(tubes):
  for tube in tubes:
    if len(tube) > 0:
      if len(tube) < COLOUR_VOLUME:
        return False
      c = tube[0]
      for oc in tube:
        if oc != c:
          return False
  
  return True

# duplicate the tubes state
def copy_tubes(tubes):
    return [[x for x in tube] for tube in tubes]

# backtracking search to find puzzle solution
# maintains history by mutating list of moves
def help_solve(tubes, moves):
  for move in good_moves(tubes):
    make_move(tubes, *move)
    moves.append((move, copy_tubes(tubes)))
    if is_solved(tubes):
      return True
    elif help_solve(tubes, moves):
      return True
    else:
      moves.pop()
      undo_move(tubes, *move)
  return False

# solve the tubes puzzle
# returns solution moves and success flag
def solve(tubes):
  moves = []
  success = True
  if not is_solved(tubes):
    success = help_solve(copy_tubes(tubes),moves)
  
  return (moves, success)