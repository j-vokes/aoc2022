import os
import re

#01234567890
#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   5   9

#[D] [W] [W] [F] [T] [H] [Z] [W] [R]
# 1   2   3   4   5   6   7   8   9 
# 1   5   9   3   7   1   5   9   3

def addCargoFromLine(inventory, string, n, start=0):
  for i, elem in enumerate(string):
    if(i>=start):
      if((i-start) % n == 0):
        if(elem != ' '):
          # Valid item
          position = ((i - start) // n) + 1 # 1 index
          if(position not in inventory):
            inventory[position] = []

          inventory[position].append(elem)

  return inventory

def addInstructionsFromLine(instructions, line):
  match = re.findall("[0-9]+", line)
  if match:
    instructions.append({"count": int(match[0]), "source": int(match[1]), "dest": int(match[2])})

file_path = "input.txt"

with open(file_path) as f:
  lines = [line.rstrip() for line in f]

inventory = {}
instructions = []
for line in lines:
  if "[" in line:
    addCargoFromLine(inventory, line, 4, 1)
  if "move" in line:
    addInstructionsFromLine(instructions, line)

# Reverse stacks
for stack in inventory.values():
  stack.reverse()

inventory = dict(sorted(inventory.items()))

print(inventory)
print(instructions)

for instruction in instructions:
  print(instruction)
  for n in range(instruction["count"]):
    transfer = inventory[instruction["source"]].pop()
    inventory[instruction["dest"]].append(transfer)

for stack in inventory.values():
  print(stack[-1], end='')
