import os
import re

currentDir = ["/"]
commandsResponse = []

total_space_available = 70000000
unused_space_needed = 30000000

class Folder:
    def __init__(self, parent):
      self.subfolders = {}
      self.files = []
      self.parent = parent

def sizeOfDirectory(directory):
  total = 0
  for file in directory.files:
    total += file["size"]
  for subfolder in directory.subfolders.values():
    total += sizeOfDirectory(subfolder)

  return total

def totalDirectoriesSmallerThanSize(directory, sizeCmp):
  total = 0
  size = sizeOfDirectory(directory)
  if(size < sizeCmp):
    total += size

  for subfolder in directory.subfolders.values():
    total += totalDirectoriesSmallerThanSize(subfolder, sizeCmp)

  return total

def findSmallestDirLargerThanSize(directory, sizeCmp):
  sizeOfSmallest = None
  size = sizeOfDirectory(directory)
  if(size > sizeCmp):
    sizeOfSmallest = size

  for subfolder in directory.subfolders.values():
    size = findSmallestDirLargerThanSize(subfolder, sizeCmp)
    if size is not None and size < sizeOfSmallest:
      sizeOfSmallest = size

  return sizeOfSmallest

base_folder = Folder(None)
current_folder = base_folder

file_path = "input.txt"

with open(file_path) as f:
  lines = [line.rstrip() for line in f]

first = True
for line in lines:
  print(line)
  if line[0] == "$":
    if first:
      first = False
    else:
      commandsResponse.append(commandResponse)
    commandResponse = {}

  if "$ cd" in line:
    commandResponse["command"] = "cd"
    commandResponse["arguments"] = line.removeprefix("$ cd ")
  elif "$ ls" in line:
    commandResponse["command"] = "list"
  else:
    if "response" not in commandResponse:
      commandResponse["response"] = []

    if "dir" in line:
      # Directory
      commandResponse["response"].append({"type": "dir", "name": line.removeprefix("dir ")})
    else:
      # File
      match = re.search("[0-9]+", line)
      print(line, match.group(0))
      commandResponse["response"].append({"type": "file", "size": int(match.group(0)), "name": line[match.end(0)+1:]})

# Catch final response
commandsResponse.append(commandResponse)

for command in commandsResponse:
  if command["command"] == "cd":
    if(command["arguments"] == ".."):
      current_folder = current_folder.parent
    elif(command["arguments"] == "/"):
      current_folder = base_folder
    else:
      current_folder = current_folder.subfolders[command["arguments"]]
    print("Current directory changed to: {}".format(command["arguments"]))
  if command["command"] == "list":
    for response in command["response"]:
      if response["type"] == "dir":
        print("Directory: {}".format(response))
        current_folder.subfolders[response["name"]] = Folder(current_folder)
      elif response["type"] == "file":
        print("File: {}".format(response))
        current_folder.files.append(response)


print("Part 1: ", totalDirectoriesSmallerThanSize(base_folder, 100000))

spaceTaken = sizeOfDirectory(base_folder)
print("Total Size: ", spaceTaken)

current_unused_space = total_space_available - spaceTaken
size_to_delete = unused_space_needed - current_unused_space

print("Space to delete: ", size_to_delete)

print("Part 2: ", findSmallestDirLargerThanSize(base_folder, size_to_delete))