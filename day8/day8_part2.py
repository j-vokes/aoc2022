import os

def countTreesRight(forest, x, y):
  total = 0
  check = forest[x][y]
  for i in range(x + 1, len(forest[x])):
    total += 1
    if(forest[i][y] >= check):
      return total
  return total

def countTreesLeft(forest, x, y):
  total = 0
  check = forest[x][y]
  for i in reversed(range(x)):
    total += 1
    if(forest[i][y] >= check):
      return total
  return total

def countTreesDown(forest, x, y):
  total = 0
  check = forest[x][y]
  for i in range(y + 1, len(forest[y])):
    total += 1
    if(forest[x][i] >= check):
      return total
  return total

def countTreesUp(forest, x, y):
  total = 0
  check = forest[x][y]
  for i in reversed(range(y)):
    total += 1
    if(forest[x][i] >= check):
      return total
  return total

def scenicScore(forest, x, y):
  total = 1
  total *= countTreesUp(forest,x,y)
  total *= countTreesLeft(forest,x,y)
  total *= countTreesDown(forest,x,y)
  total *= countTreesRight(forest,x,y)
  return total
  

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
    sScore = scenicScore(forest, x, y)
    if(sScore > total):
      total = sScore

print(total)

