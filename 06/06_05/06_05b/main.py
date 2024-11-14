from collections import deque

def matching(strig):
  caract = list(strig)
  c1 = 0
  c2 = 0
  while len(caract) > 0:
    t = caract.pop()
    if t == "(" :
      c1 += 1
    if t == ")":
      c2 += 1
  print(c1 == c2)

matching("()()())))(())")
matching("(()()())")

matching("()")
matching("(hi there)")
matching("(hell)o")
matching("((linkedin)) learning")

matching("(hi(there")
matching("((increment)")
matching(")linkedin()")