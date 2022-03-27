from Boats import Boats

current = Boats(3, 3, 1, 3, 3, None)
# Will work as a queue (pop the head and push the tail)
queue = [current]
visited = []

while current != Boats(0, 0, 0, 3, 3, None):  
  current = queue.pop(0)

  if current in visited:
    continue

  print("M: " + str(current.NM) + " C: " + str(current.NC) + " B: " + str(current.NB))
  visited.append(current)

  if(current.C1_precond()):
    queue.append(current.C1())
  
  if(current.CC1_precond()):
    queue.append(current.CC1())
  
  if(current.M1_precond()):
    queue.append(current.M1())
    
  if(current.MM1_precond()):
    queue.append(current.MM1())
    
  if(current.MC1_precond()):
    queue.append(current.MC1())

  if(current.C2_precond()):
    queue.append(current.C2())
  
  if(current.CC2_precond()):
    queue.append(current.CC2())
  
  if(current.M2_precond()):
    queue.append(current.M2())
    
  if(current.MM2_precond()):
    queue.append(current.MM2())
    
  if(current.MC2_precond()):
    queue.append(current.MC2())

path = []
while current is not None:
  path.append(current)
  current = current.previous

while len(path) > 0:
  current = path.pop()
  print("M: " + str(current.NM) + " C: " + str(current.NC) + " B: " + str(current.NB))