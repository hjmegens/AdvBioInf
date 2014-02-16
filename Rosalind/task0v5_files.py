import sys

lines=sys.stdin.readlines()
for i in range(len(lines)):
   if i % 2 == 1:
      print(lines[i][:-1])



