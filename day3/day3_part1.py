import sys
import os

testInput = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
rucksack_file_path = "input.txt"

item_code_a = ord('a') - 1
item_code_A = ord('A') - 1
lettersInAlphabet = 26

def toPriority(item):
  item_code = ord(item)
  if(item_code < item_code_a):
    item_code -= (item_code_A - lettersInAlphabet)
  else:
    item_code -= item_code_a
  return item_code

with open(rucksack_file_path) as f:
  lines = [line.rstrip() for line in f]

total = 0
for line in lines:
#for line in testInput.splitlines():
  compart1 = line[0:(len(line)//2)]
  compart2 = line[len(line)//2:]

  # Sanity check
  assert(len(compart1) == len(compart2))

  for item1 in compart1:
    for item2 in compart2:
      if(item1 == item2):
        targetItem = item1
        break

  total += toPriority(targetItem)

print(total)