import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def main():
  lines = readfile()
  left_side = []
  right_side = []
  for element in lines:
    split_lines =element.split('  ')
    left_side.append(int(split_lines[0]))
    right_side.append(int(split_lines[1]))

  left_side.sort()
  right_side.sort()
  tot_dist = 0
  similarity_score = 0
  for x in range(len(left_side)):
    tot_dist += abs(left_side[x]-right_side[x])
    similarity_score += left_side[x]*right_side.count(left_side[x])
  print(tot_dist)
  print(similarity_score)


  # print(lines)
main()