import sys
sums=0
integers=sys.stdin.readline()[:-1].split(' ')
print(integers)
for i in range(int(integers[0]),int(integers[1])+1):
   if i % 2 == 1:
      sums+=i

print(sums)

