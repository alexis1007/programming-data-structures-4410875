from collections import deque

def pop(pila):
  if len(pila)==0:
      pila.append(1)
  else:
    t = pila.pop()
    if t == 1:
      pop(pila)
      pila.append(0)
    if t == 0:
      pila.append(1)

def conver(deque):
  ret=[None] * len(deque)
  i = 0
  while len(deque) > 0:
    ret[i] = deque.pop()
    i += 1
  return ret

def obtener(task2):
  while len(task2) >0:
    print(task2.popleft())

def Binare(numero):
  task = deque()
  c = deque()
  tem = deque()
  n = 0
  while n < numero:
    n += 1
    pop(c)
    tem = c.copy()
    task.append(conver(tem))
  obtener(task)


          
Binare(5)


    

