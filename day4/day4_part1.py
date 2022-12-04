import sys
import os

testInput = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
file_path = "input.txt"

with open(file_path) as f:
  lines = [line.rstrip() for line in f]

# Expect "a-b" format
def toAssignment(text):
  values = text.split("-")
  return [int(values[0]),int(values[1])]

def assignmentSize(assignment):
  return assignment[1] - assignment[0]

assignments = []
for line in lines:
#for line in testInput.splitlines():
  assignment = [toAssignment(line.split(",")[0]), toAssignment(line.split(",")[1])]

  # Sort assignments
  swap = False
  if(assignment[0][0] == assignment[1][0]):
    if(assignmentSize(assignment[0]) < assignmentSize(assignment[1])):
      swap = True
  elif(assignment[0][0] > assignment[1][0]):
      swap = True

  if(swap):
    assignment[0], assignment[1] = assignment[1], assignment[0]
    
  assignments.append(assignment)

total = 0
for assignment in assignments:
  if(assignment[1][1] <= assignment[0][1]):
    total += 1
    print(assignment)

print(total)
  