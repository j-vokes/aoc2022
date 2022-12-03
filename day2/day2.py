import sys
import os
from enum import Enum

score_rock = 1
score_paper = 2
score_scissors = 3

score_win = 6
score_draw = 3
score_loss = 0

testInput = "A Y\nB X\nC Z"

class Shape(Enum):
  Rock=1
  Paper=2
  Scissors=3

def getShape(type_str):
  if(type_str=="A" or type_str=="X"):
    return Shape.Rock
  elif(type_str=="B" or type_str=="Y"):
    return Shape.Paper
  elif(type_str=="C" or type_str=="Z"):
    return Shape.Scissors

def getShapeScore(shape):
  if shape == Shape.Rock:
    return score_rock
  elif shape == Shape.Scissors:
    return score_scissors
  elif shape == Shape.Paper:
    return score_paper

def getWinLossScore(result):
  return score_win if result == 1 else score_loss

playbook = {}
playbook[Shape.Rock,Shape.Scissors] = [1, 0]
playbook[Shape.Scissors,Shape.Paper] = [1, 0]
playbook[Shape.Paper,Shape.Rock] = [1, 0]

playbook[Shape.Scissors,Shape.Rock] = [0, 1]
playbook[Shape.Paper,Shape.Scissors] = [0, 1]
playbook[Shape.Rock,Shape.Paper] = [0, 1]




def match(play1, play2):
  if(play1 == play2):
    return [score_draw + getShapeScore(play1), score_draw + getShapeScore(play2)]
  else:
    result = playbook[play1, play2]
    return [getWinLossScore(result[0]) + getShapeScore(play1), getWinLossScore(result[1]) + getShapeScore(play2)]

strategy_file_path = "/home/jamesv/sandbox/snippets/python/aoc2022/day2/day2_input.txt"

with open(strategy_file_path) as f:
  lines = [line for line in f]

totalScore = 0

for line in lines:
  strategy_line = line.rstrip().split(" ")
  match_score = match(getShape(strategy_line[0]), getShape(strategy_line[1]))
  totalScore += match_score[1]

print(totalScore)