import sys

dna=sys.stdin.readline()[:-1]
n=int(sys.stdin.readline()[:-1])

mydict=dict()
for i in range(len(dna)-n):
   kmer=dna[i:i+n]
   if kmer in mydict.keys():
      mydict[kmer]+=1
   else:
      mydict[kmer]=1

maxvalue=max(mydict.values())
for k,v in mydict.items():
   if v == maxvalue:
      print(k,end=' ')
