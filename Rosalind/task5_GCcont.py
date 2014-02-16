import sys
# cat rosalind_gc.txt | python3 task5_GCcont.py
# cat testfa.fa | python3 task5_GCcont.py
topgc=0
topgcid='Na'

seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
for seq in seqs:
   length=len(seq[1])
   Cs=seq[1].count('C')
   Gs=seq[1].count('G')
   gc=(Cs+Gs)/length
   print(seq[0],length,gc)
   if gc >topgc:
      topgc=gc
      topgcid=seq[0]

print(topgcid)
print(100*topgc)
