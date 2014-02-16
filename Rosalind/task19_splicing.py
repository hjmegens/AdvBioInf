import sys
import re
# cat rosalind_splc.txt | python3 task19_splicing.py
def translate(dna):
   codons=codon_table()
   protein=''
   for i in range(0,len(dna),3):
      codon=dna[i:i+3]
      if len(codon)==3:
         protein+=codons[codon]
   return protein

def codon_table():
   bases = ['T', 'C', 'A', 'G']
   codons = [a+b+c for a in bases for b in bases for c in bases]
   amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
   codon_table = dict(zip(codons, amino_acids))
   return codon_table


seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
dna=seqs[0][1]
for i in range(1,len(seqs)):
   intr=seqs[i][1]
   dna=dna.replace(intr,'N'*len(intr))

dna=dna.replace('N','')
protein=translate(dna)
print(protein[:-1])
