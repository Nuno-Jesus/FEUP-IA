from State import State



current = State(4, 3, 0, 0, None)
queue = [current]
visited = []
current_depth = 0

while current != State(4, 3, 2, 0, None):
  current = queue.pop()
  
  #If the current node is in a higher depth of the maximum depth in this iteration
  if current.depth() > current_depth:
    #Reset the lists and initial state
    current = State(4, 3, 0, 0, None)
    queue = [current]
    visited = []
    
    #Increment the iteration depth
    current_depth = current_depth + 1
    
    #Skip the last node popped from the list(previous iteration)
    continue
  
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
    

print("Depth: " + str(current.depth()))

path = []
while current is not None:
  path.append(current)
  current = current.previous

while len(path) > 0:
  temp = path.pop()
  print("B1: " + str(temp.bucket1) + " B2: " + str(temp.bucket2))

print("\n")