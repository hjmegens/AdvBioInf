import sys
from itertools import product
# cat testlex.txt | python3 task14_enumeration_lex.py 
lexic=sys.stdin.readline()[:-1]
n=sys.stdin.readline()[:-1]
n=int(n)
allnumbers=lexic.replace(' ','')
combs=product(str(allnumbers),repeat=n)
num=0
for comb in combs:
   num+=1
print(num)


combs=product(str(allnumbers),repeat=n)
for comb in combs:
   formatstring=''
   for i in range(n):
      formatstring+=comb[i]
   
   print(formatstring)
