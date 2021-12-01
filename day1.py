import sys 

with open('inputs/day1.txt') as f:
  lines = f.read().splitlines()
    
def day1_part1():
  counter = 0
  
  for i in range(len(lines) - 1):
    counter += 1 if int(lines[i+1]) - int(lines[i]) > 0 else 0
  
  return counter

print(day1_part1())

def day1_part2():
  prev, counter = sys.maxsize, 0
  
  # create a 3-item sliding window 
  for i in range(len(lines) - 2):
    window = sum([int(item) for item in lines[i:i+3]])
    counter += 1 if window > prev else 0
    prev = window
  
  return counter

print(day1_part2())
