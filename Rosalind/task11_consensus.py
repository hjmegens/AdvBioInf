import sys
# cat rosalind_cons.txt | python3 task11_consensus.py >textfile.txt

topgc=0
topgcid='Na'
 
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
matrix=[]
numseqs=len(seqs)
lengthseqs=len(seqs[0][1])
print(numseqs,lengthseqs)
for seq in seqs:
   matrix.append(list(seq[1]))
matrix2=[]
#print(matrix)
for i in range(lengthseqs):
   column=[]
   for j in range(numseqs):   
      column.append(matrix[j][i])
#   print(column)
   As=''.join(column).count('A')
   Cs=''.join(column).count('C')
   Gs=''.join(column).count('G')
   Ts=''.join(column).count('T')
   matrix2.append([As,Cs,Gs,Ts])

#print(matrix2)
DNA=''
for element in matrix2:
   if element[0]>=element[1] and element[0]>=element[2] and element[0]>=element[3]:
      if element[0]+element[1]+element[2]+element[3] != numseqs:
         print('error! wrong number in matrix')
      DNA+='A'
   elif element[1]>=element[0] and element[1]>=element[2] and element[1]>=element[3]:
      if element[0]+element[1]+element[2]+element[3] != numseqs:
         print('error! wrong number in matrix')
      DNA+='C'
   elif element[2]>=element[1] and element[2]>=element[0] and element[2]>=element[3]:
      if element[0]+element[1]+element[2]+element[3] != numseqs:
         print('error! wrong number in matrix')
      DNA+='G'
   elif element[3]>=element[1] and element[3]>=element[2] and element[3]>=element[0]:
      if element[0]+element[1]+element[2]+element[3] != numseqs:
         print('error! wrong number in matrix')
      DNA+='T'
print(len(matrix2),len(matrix2[0]))
print(len(DNA),lengthseqs,DNA)
bases=['A','C','G','T']
for i in range(4):
   mystring = bases[i]+':'
   for j in range(len(matrix2)):
      mystring+=(' '+str(matrix2[j][i]))
   print(mystring)

      
