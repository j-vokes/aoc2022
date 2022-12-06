import os

input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
marker_length = 14

def markerGenerator(data, n):
  for index in range(len(data) - n + 1):
    yield data[index:index+n]

with open("input.txt") as f:
  input = f.readline()


gen = markerGenerator(input, marker_length)
for i, marker in enumerate(gen):
  if len(set(marker)) == marker_length:
    print(i+marker_length)
    break