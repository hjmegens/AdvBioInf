import sys
from itertools import permutations
# echo '4' | python3 task12_enumeration.py
n=sys.stdin.readline()[:-1]
n=int(n)
allnumbers=[]
for i in range(n):
   allnumbers.append(str(i+1))
allnumbers=''.join(allnumbers)
print(allnumbers)

combs=permutations(allnumbers,len(allnumbers))
num=0
for comb in combs:
   num+=1
print(num)


combs=permutations(allnumbers,len(allnumbers))
for comb in combs:
   formatstring=''
   for i in range(n):
      formatstring+=comb[i]+' '
   
   print(formatstring[:-1])
