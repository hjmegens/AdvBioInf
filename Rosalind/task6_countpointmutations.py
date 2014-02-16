import sys
# cat testhamming.txt | python3 task6_countpointmutations.py
# cat rosalind_hamm.txt | python3 task6_countpointmutations.py
hd=0

seqs=[seq[:-1] for seq in sys.stdin.readlines()]
print(seqs)
for i in range(len(seqs[0])):
   if seqs[0][i] != seqs[1][i]:
      hd+=1
length=len(seqs[0])
print(length,hd)
