import sys
import math
# cat test_RNA_secstruct.fa | python3 task23_RNA_secondary_structure.py
# cat rosalind_pmch.txt | python3 task23_RNA_secondary_structure.py
seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
dna=seqs[0][1]
As=dna.count('A')
Cs=dna.count('C')
AU=math.factorial(As)
CG=math.factorial(Cs)
print(AU*CG)
