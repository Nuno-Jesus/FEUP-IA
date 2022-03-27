from Boats import Boats

current = Boats(3, 3, 1, 3, 3, None)
# Will work as a queue (pop the head and push the tail)
queue = [current]
visited = []

while current != Boats(0, 0, 0, 3, 3, None):  
  current = queue.pop(0)

  if current in visited:
    continue

  