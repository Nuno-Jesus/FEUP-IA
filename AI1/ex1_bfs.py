from Buckets import Buckets

current = Buckets(4, 3, 0, 0, None)
queue = [current]
visited = []

while current != Buckets(4, 3, 2, 0, None):
  current = queue.pop()

  if current in visited: 
    continue

  visited.append(current)

  if(current.fill1_precond()):
    queue.append(current.fill1())

  if(current.fill2_precond()):
    queue.append(current.fill2())

  if(current.empty1_precond()):
    queue.append(current.empty1())

  if(current.empty2_precond()):
    queue.append(current.empty2())

  if(current.pour12_until_1_is_empty_precond()):
    queue.append(current.pour12_until_1_is_empty())

  if(current.pour12_until_2_is_full_precond()):
    queue.append(current.pour12_until_2_is_full())

  if(current.pour12_until_1_is_empty_precond()):
    queue.append(current.pour12_until_1_is_empty())
  
  if(current.pour21_until_1_is_full_precond()):
    queue.append(current.pour21_until_1_is_full())

path = []
while current is not None:
  path.append(current)
  current = current.previous


while len(path) > 0:
  temp = path.pop()
  print("B1: " + str(temp.bucket1) + " B2: " + str(temp.bucket2))