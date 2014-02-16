import sys
import re
# cat testORF.fa | python3 task15_ORF.py
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

def translate_and_orf(dna,candidates):
   for j in range(3):
      dnastr=dna[j:]
      protein=translate(dnastr)
      for k in range(len(protein)):
      
         orf=re.findall('M\w*?\*',protein[k:])
         for candidate in orf:
            candidates.add(candidate)

   return(candidates)

seqs = sys.stdin.read().split('>')[1:]
seqs = [ element.split('\n',1) for element in seqs]
seqs = [[element[0],element[1].replace('\n','')] for element in seqs]
forward=seqs[0][1]
revcomp=forward.translate(str.maketrans('ACGT','TGCA'))[::-1]

candidates=set()
candidates=translate_and_orf(forward,candidates)
candidates=translate_and_orf(revcomp,candidates)
for candidate in candidates:
   print(candidate[:-1])

