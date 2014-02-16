import sys
import re
# cat rosalind_grph.txt | python3 task16_adjacency_graph.py
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]

for seq	in seqs:
   for i in range(len(seqs)):
      #print(seq[1][len(seq[1])-3:],seqs[i][1][:3])

      if seq[1][len(seq[1])-3:]==seqs[i][1][:3] and seq[0] != seqs[i][0]:
         print(seq[0],seqs[i][0])



