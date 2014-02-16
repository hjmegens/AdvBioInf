import sys
# cat rosalind_pdst.txt | python3 task27_pairwisedist.py
# cat test_pairwisedist.fa | python3 task27_pairwisedist.py 
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]

matrix=[0 for i in range(len(seqs))]
matrix=[matrix[:] for i in range(len(seqs))]
print(matrix)
print(seqs)
for i in range(len(seqs)):
   for j in range(len(seqs)):
      hd=0
      for k in range(len(seqs[i][1])):
         if seqs[i][1][k] != seqs[j][1][k]:
           hd+=1
      dist=hd/len(seqs[i][1])
      matrix[i][j]=dist
      matrix[j][i]=dist    
print(matrix)
for row in matrix:
   print(' '.join([str(i) for i in row]))
