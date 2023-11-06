def combinationsWithoutCurrent(current):
  num = 1
  for child in current:
    num *= stableSet(child)
  return num

def combinationsWithCurrent(current):
  num = 1
  for child in current:
    num *= combinationsWithoutCurrent(child)
  return num

def stableSet(current):
  return (combinationsWithCurrent(current) +
          combinationsWithoutCurrent(current))

