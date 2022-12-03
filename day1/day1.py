import sys
import os

def total_sort(e):
  return e["total"]

calorie_file_path = "day1_input.txt"

with open(calorie_file_path) as f:
  lines = [line for line in f]

elves = []
elf_inventory = []

for line in lines:
  line = line.rstrip()
  if line != "":
    elf_inventory.append(int(line))
  else:
    elves.append({"total": sum(elf_inventory), "inventory": elf_inventory})
    elf_inventory = []

print(elves[0:3])
elves.sort(key=total_sort, reverse=True)
print(elves[0:3])

total = 0
for elf in elves[0:3]:
  total+= elf["total"]

print(total)