import sys
import re
# cat rosalind_subs.txt | python3 task7_matchstrings.py
# cat testmatch.txt | python3 task7_matchstrings.py
hd=0

seqs=[seq[:-1] for seq in sys.stdin.readlines()]
print(seqs)

pos=[]
for i in range(len(seqs[0])-len(seqs[1])):
    subs=seqs[0][i:i+len(seqs[1])]
    if str(subs)==seqs[1]:
      pos.append(str(i+1))
print(' '.join(pos))
