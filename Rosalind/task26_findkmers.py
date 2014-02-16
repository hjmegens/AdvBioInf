import sys
from itertools import product
# cat rosalind_kmer.txt | python3 task26_findkmers.py
# cat test_kmercount.fa | python3 task26_findkmers.py
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
dna=seqs[0][1]
n=4
dnaletters='ACGT'

combs=product(dnaletters,repeat=n)
kmertable=[]
for comb in combs:
   formatstring=''
   for i in range(n):
      formatstring+=comb[i]
   
   kmertable.append(formatstring)
#print(kmertable)
kmercount=[0 for i in range(len(kmertable))]
print(kmercount)
for i in range(len(dna)):
   for j in range(len(kmertable)):
      if dna[i:i+n]==kmertable[j]:
         kmercount[j]+=1
print(' '.join([str(i) for i in kmercount]))
