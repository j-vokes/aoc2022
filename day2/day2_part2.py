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

class Strategy(Enum):
  Win=1
  Draw=2
  Lose=3

def getShape(type_str):
  if(type_str=="A"):
    return Shape.Rock
  elif(type_str=="B"):
    return Shape.Paper
  elif(type_str=="C"):
    return Shape.Scissors

def getStrategy(type_str):
  if(type_str=="Z"):
    return Strategy.Win
  elif(type_str=="Y"):
    return Strategy.Draw
  elif(type_str=="X"):
    return Strategy.Lose

def getShapeScore(shape):
  if shape == Shape.Rock:
    return score_rock
  elif shape == Shape.Scissors:
    return score_scissors
  elif shape == Shape.Paper:
    return score_paper

def getWinLossScore(result):
  return score_win if result == Strategy.Win else score_loss

playbook = {}
playbook[Shape.Rock,Strategy.Win] = Shape.Paper
playbook[Shape.Rock,Strategy.Lose] = Shape.Scissors

playbook[Shape.Scissors,Strategy.Win] = Shape.Rock
playbook[Shape.Scissors,Strategy.Lose] = Shape.Paper

playbook[Shape.Paper,Strategy.Win] = Shape.Scissors
playbook[Shape.Paper,Strategy.Lose] = Shape.Rock




def match(play1, strategy):
  if(strategy == Strategy.Draw):
    return score_draw + getShapeScore(play1)
  else:
    result = playbook[play1, strategy]
    return getWinLossScore(strategy) + getShapeScore(playbook[play1, strategy])

strategy_file_path = "/home/jamesv/sandbox/snippets/python/aoc2022/day2/day2_input.txt"

with open(strategy_file_path) as f:
  lines = [line for line in f]

totalScore = 0

for line in lines:
#for line in testInput.splitlines():
  strategy_line = line.rstrip().split(" ")
  match_score = match(getShape(strategy_line[0]), getStrategy(strategy_line[1]))
  totalScore += match_score

print(totalScore)