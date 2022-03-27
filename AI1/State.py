class State:
  def __init__ (this, capacity1, capacity2, bucket1, bucket2, previous):
    this.capacity1 = capacity1
    this.capacity2 = capacity2
    this.bucket1 = bucket1
    this.bucket2 = bucket2
    this.previous = previous

  #Empty bucket 1
  def empty1(this):
    return State(this.capacity1, this.capacity2, 0, this.bucket2, this)

  #Empty bucket 2
  def empty2(this):
    return State(this.capacity1, this.capacity2, this.bucket1, 0, this)

  #Fill bucket 1
  def fill1(this):
    return State(this.capacity1, this.capacity2, this.capacity1, this.bucket2, this)

  #Fill bucket 2
  def fill2(this):
    return State(this.capacity1, this.capacity2, this.bucket1, this.capacity2, this)

  #Pour from 1 to 2 until 2 is full
  def pour12_until_2_is_full(this):
    c1 = this.bucket1 - (this.capacity2 - this.bucket2)
    c2 = this.capacity2
    return State(this.capacity1, this.capacity2, c1, c2, this)

  #Pour from 1 to 2 until 1 is empty
  def pour12_until_1_is_empty(this):
    c1 = 0
    c2 = this.bucket2 + this.bucket1
    return State(this.capacity1, this.capacity2, c1, c2, this)

  #Pour from 2 to 1 until 1 is full
  def pour21_until_1_is_full(this):
    c1 = this.capacity1
    c2 = this.bucket2 - (this.capacity1 - this.bucket1)
    return State(this.capacity1, this.capacity2, c1, c2, this)

  #Pour from 2 to 1 until 2 is empty
  def pour21_until_2_is_empty(this):
    c1 = this.bucket1 + this.bucket2
    c2 = 0
    return State(this.capacity1, this.capacity2, c1, c2, this)

  def fill1_precond(this):
    return this.bucket1 < this.capacity1
  
  def fill2_precond(this):
    return this.bucket2 < this.capacity2

  def empty1_precond(this):
    return this.bucket1 > 0

  def empty2_precond(this):
    return this.bucket2 > 0

  def pour12_until_2_is_full_precond(this):
    return this.bucket1 > 0 and this.bucket2 < this.capacity2 and this.bucket1 >= this.capacity2 - this.bucket2
  
  def pour21_until_1_is_full_precond(this):
    return this.bucket2 > 0 and this.bucket1 < this.capacity1 and this.bucket2 >= this.capacity1 - this.bucket1

  def pour12_until_1_is_empty_precond(this):
    return this.bucket1 > 0 and this.bucket2 < this.capacity2 and this.bucket1 < this.capacity2 - this.bucket2
  
  def pour21_until_2_is_empty_precond(this):
    return this.bucket2 > 0 and this.bucket1 < this.capacity1 and this.bucket2 < this.capacity1 - this.bucket1
  
  #Override to compare objects
  def __eq__(this, other):
    return this.bucket1 == other.bucket1 and this.bucket2 == other.bucket2 and this.capacity1 == other.capacity1 and this.capacity2 == other.capacity2

  def depth(this):
    depth = 0
    
    state = this.previous
    while state is not None:
      state = state.previous
      depth = depth + 1

    return depth