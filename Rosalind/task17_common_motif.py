import sys
import re
# cat testcommonmotif.fa | python3 task17_common_motif.py
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]

minlength=-1
for seq in seqs:
   if len(seq[1])<minlength or minlength < 0:
      minlength=len(seq[1])
      refseq=seq[1]

commonmotif=''
for i in range(2,len(refseq)):
   if len(commonmotif) < i-3:
      break
   for j in range(len(refseq)-i):
      motif=refseq[j:j+i]
      numtimesfound=0
      for seq in seqs:
         if seq[1].count(motif)>0:
            numtimesfound+=1
      if numtimesfound == len(seqs):
         commonmotif=motif
         print(i,j,commonmotif)
         break
print(commonmotif)



