from sty import fg, bg, ef, rs, Style, RgbFg, RgbBg

bg.my_blue = Style(RgbBg(60, 52, 192))
bg.brown = Style(RgbBg(126, 72, 18))
bg.my_cyan = Style(RgbBg(87, 163, 228))
bg.mint = Style(RgbBg(102, 213, 128))
bg.orange = Style(RgbBg(230, 138, 74))
bg.olive = Style(RgbBg(122, 147, 23))
bg.pink = Style(RgbBg(231, 95, 121))
bg.purple = Style(RgbBg(110, 47, 146))
bg.my_red = Style(RgbBg(195, 45, 42))
bg.my_yellow = Style(RgbBg(240, 216, 96))

colours_dict = {
  1  : ("blue", bg.my_blue),
  2  : ("brown", bg.brown),
  3  : ("cyan", bg.my_cyan),
  4  : ("emerald", bg.da_green),
  5  : ("gray", bg.da_grey),
  6  : ("mint", bg.mint),
  7  : ("orange", bg.orange),
  8  : ("olive", bg.olive),
  9  : ("pink", bg.pink),
  10 : ("purple", bg.purple),
  11 : ("red", bg.my_red),
  12 : ("yellow", bg.my_yellow),
}

def read(pref):
  for c,(name, bg_col) in colours_dict.items():
    if name.startswith(pref):
      return c
  print('failed read:', pref)


def read_tube(tube):
  return list(map(read,tube))

def read_tubes(tubes):
  return list(map(read_tube,tubes))

def show_tube(tube):
  return list(map(show,tube))

def show(i):
  return colours_dict[i][1] + str(hex(i))[-1] + rs.bg

def show_tubes(tubes, tube_height):
  def colour_row(row):
    return " ".join((show(tube[row]) if row < len(tube) else ('_' if row == 0 else ' ')) for tube in tubes)

  return "\n".join(colour_row(row) for row in range(tube_height-1,-1,-1))
