import os

def checkVisibleRight(forest, x, y):
  check = forest[x][y]
  for i in range(x + 1, len(forest[x])):
    if(forest[i][y] >= check):
      return False
  return True

def checkVisibleLeft(forest, x, y):
  check = forest[x][y]
  for i in reversed(range(x)):
    if(forest[i][y] >= check):
      return False
  return True

def checkVisibleDown(forest, x, y):
  check = forest[x][y]
  for i in range(y + 1, len(forest[y])):
    if(forest[x][i] >= check):
      return False
  return True

def checkVisibleUp(forest, x, y):
  check = forest[x][y]
  for i in reversed(range(y)):
    if(forest[x][i] >= check):
      return False
  return True

def isVisible(forest, x, y):
  if(checkVisibleUp(forest,x,y)):
    return True
  elif(checkVisibleLeft(forest,x,y)):
    return True
  elif(checkVisibleDown(forest,x,y)):
    return True
  elif(checkVisibleRight(forest,x,y)):
    return True
  else:
    return False
  

forest = []

with open("input.txt") as f:
  lines = [line.rstrip() for line in f]

for line in lines:
  row = []
  for elem in line:
    row.append(elem)

  forest.append(row)

total = 0
for x, _ in enumerate(forest):
  for y, _ in enumerate(forest[x]):
    if(isVisible(forest, x, y)):
      total += 1

print(total)

