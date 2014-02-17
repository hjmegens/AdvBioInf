import sys
from itertools import product
# cat rosalind_revp.txt | python3 task29_palindrome.py
# cat test_palindrome.fa | python3 task29_palindrome.py
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
dna=seqs[0][1]
n=2 # minlength palindrome
m=6 # maxlength palindrome
#print(len(dna))
positions=[]
for l in range(n,m+1):
   for i in range(l,len(dna)-l+1):
      lagfrag=dna[i-l:i]
      leadfrag=dna[i:i+l]
      revcomp_leadfrag=leadfrag.translate(str.maketrans('ACGT','TGCA'))[::-1]
#      print(lagfrag,leadfrag,revcomp_leadfrag)
      if lagfrag == revcomp_leadfrag:
#         print(lagfrag,leadfrag,revcomp_leadfrag,str(i-l+1))
         positions.append([str(i-l+1),2*len(lagfrag)])
for position in positions:
   print(str(position[0]),str(position[1]))

