from State import State

max_depth = int(input("Enter a depth: "))

for i in range(max_depth):
  current = State(4, 3, 0, 0, None)
  queue = [current]
  visited = []

  while current != State(4, 3, 2, 0, None) and current.depth() < i:
    current = queue.pop()

    if current in visited: 
      continue

    visited.append(current)
    
    if(current.fill1_precond()):
      queue.insert(0, current.fill1())

    if(current.fill2_precond()):
      queue.insert(0, current.fill2())

    if(current.empty1_precond()):
      queue.insert(0, current.empty1())

    if(current.empty2_precond()):
      queue.insert(0, current.empty2())

    if(current.pour12_until_1_is_empty_precond()):
      queue.insert(0, current.pour12_until_1_is_empty())

    if(current.pour12_until_2_is_full_precond()):
      queue.insert(0, current.pour12_until_2_is_full())

    if(current.pour12_until_1_is_empty_precond()):
      queue.insert(0, current.pour12_until_1_is_empty())
    
    if(current.pour21_until_1_is_full_precond()):
      queue.insert(0, current.pour21_until_1_is_full())

  path = []
  while current is not None:
    path.append(current)
    current = current.previous

  print("Depth: " + str(i))
  while len(path) > 0:
    temp = path.pop()
    print("B1: " + str(temp.bucket1) + " B2: " + str(temp.bucket2))

  print("\n")