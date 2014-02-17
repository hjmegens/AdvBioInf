import sys
import math

# echo '6 16' | python3 task28_Mendel2.py
# echo '2 1' | python3 task28_Mendel2.py
vals=sys.stdin.readline()[:-1].split(' ')
numgen=int(vals[0])
minnumAaBb=int(vals[1])
probs=0
numdescendents=2**numgen
print(numdescendents)
for i in range(minnumAaBb,numdescendents+1):
   factor=math.factorial(numdescendents)/(math.factorial(numdescendents-i)*math.factorial(i))
   prob=factor*(0.25**i)*(0.75**(numdescendents-i))
   print(i,prob,factor)
   probs+=prob
print(probs)
         
