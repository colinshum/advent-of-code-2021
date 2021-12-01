class Day1:
  def __init__(self):
    with open('inputs/day1.txt') as f:
      self.data = [int(i) for i in f.read().splitlines()]
      
  def part1(self):
    return len(list(filter(lambda x: x[1] > x[0], zip(self.data, self.data[1:]))))
  
  def part2(self):
    return len(list(filter(lambda x: x[1] > x[0], zip(self.data, self.data[3:]))))

if __name__ == '__main__':
  print(Day1().part1())
  print(Day1().part2())
