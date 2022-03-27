# params
# NC - number of cannibals in the original shore
# NM - number of missionaries in the original shore
# NB - number of boats in the original shore
# M - total number of missionaries 
# C - total number of cannibals

class Boats:
  def __init__(this, NC, NM, NB, M, C, previous):
    this.NC = NC
    this.NM = NM
    this.NB = NB
    this.M = M
    this.C = C
    this.previous = previous
  
  # Move 1 missionary from the origin to destination
  def M1(this):
    return Boats(this.NC, this.NM - 1, 0, this.M, this.C, this)

  # Move 2 missionaries from the origin to destination
  def MM1(this):
    return Boats(this.NC, this.NM - 2, 0, this.M, this.C, this)

  # Move 1 cannibal from the origin to destination
  def C1(this):
    return Boats(this.NC - 1, this.NM, 0, this.M, this.C, this)
  
  # Move 2 cannibals from the origin to destination
  def CC1(this):
    return Boats(this.NC - 2, this.NM, 0, this.M, this.C, this)
  
  # Move 1 cannibal and 1 missionary from the origin to destination
  def MC1(this):
    return Boats(this.NC - 1, this.NM - 1, 0, this.M, this.C, this)
  
  # Move 1 missionary from the destination to origin
  def M2(this):
    return Boats(this.NC, this.NM - 1, 1, this.M, this.C, this)
  
  # Move 2 missionaries from the destination to origin
  def MM2(this):
    return Boats(this.NC, this.NM - 2, 1, this.M, this.C, this)
  
  # Move 1 cannibal from the destination to origin
  def C2(this):
    return Boats(this.NC - 1, this.NM, 1, this.M, this.C, this)
  
  # Move 2 cannibals from the destination to origin
  def CC2(this):
    return Boats(this.NC - 2, this.NM, 1, this.M, this.C, this)
  
  # Move 1 missionary and 1 cannibal from the destination to origin
  def MC2(this):
    return Boats(this.NC - 1, this.NM - 1, 1, this.M, this.C, this)

    
  