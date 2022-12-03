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
input = lines
#input = testInput.splitlines()
for n in range(0, len(input), 3):

  line1 = input[n]
  line2 = input[n+1]
  line3 = input[n+2]
  
  for item1 in line1:
    for item2 in line2:
      if(item1 == item2):
        for item3 in line3:
          if(item1 == item3):
            targetItem = item1
            break

  total += toPriority(targetItem)

print(total)