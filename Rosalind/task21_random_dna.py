import sys
from math import log
# cat test_random.txt | python3 task21_random_dna.py
dna=sys.stdin.readline()[:-1]
matrix=sys.stdin.readline()[:-1].split(' ')
print(dna)
print(matrix)
alliks=[]
dna=list(dna)
for gc in matrix:
   gc=float(gc)
   lik=0
   for base in dna:
      if base == 'A' or base == 'T':

         prob = (1-gc)/2
         lik+=log(prob,10)
         
      elif base == 'G' or base == 'C':
         prob= gc/2
         lik+=log(prob,10)
   alliks.append(lik)
for lik in alliks:
   print(' '+str(lik),end='')


