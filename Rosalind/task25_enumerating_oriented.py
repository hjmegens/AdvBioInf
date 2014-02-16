import sys
from itertools import product
# echo '3' | python3 task25_enumerating_oriented.py
n=sys.stdin.readline()[:-1]
n=int(n)
allnumbers=[]
for i in range(n):
   allnumbers.append(str(i+1))
   allnumbers.append(str((i+1)*-1))
print(allnumbers)


combs=product(allnumbers, repeat=n)
results=[]
for comb in combs:
   formatstring=''
   testset=set()
   for i in range(n):
      testset.add(abs(int(comb[i])))
      formatstring+=comb[i]+' '
   if len(testset)==n:
      results.append(formatstring[:-1])
print(len(results))
for result in results:
   print(result)
