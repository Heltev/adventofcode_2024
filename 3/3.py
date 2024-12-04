import sys,re
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def get_product(factors):
  left_side, right_side = factors.split(',')
  return int(left_side)*int(right_side)

def main():
  corrupt_data = readfile()
  mul_statements = []
  part1_temp_list=[]
  part2_temp_list=[]
  for line in corrupt_data:
    part1_temp_list.append(re.findall("mul\(\d{1,3},\d{1,3}\)",line)) 
    part2_temp_list.append(re.findall("mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)",line)) 
  mul_statements = [mul.split('mul')[1][1:-1] for line in part1_temp_list for mul in line]
  
  mul_results = 0
  for element in mul_statements:
    mul_results += get_product(element)
  print(mul_results)

  mul_results = 0
  instructions = [element for line in part2_temp_list for element in line]
  do = True
  for instruction in instructions:
    if instruction == 'do()':
      do = True
    elif instruction == "don't()":
      do = False
    else:
      if do:
        mul_results += get_product(instruction.split('mul')[1][1:-1])

  print(mul_results)

main()