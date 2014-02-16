import sys
import re
# cat rosalind_mrna.txt | python3 task22_RNAstrings.py
prot=sys.stdin.readline()[:-1]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
prot=list(prot)
posb=1
for aa in prot:
   posb=posb*amino_acids.count(aa)

posb=posb*3
print(posb)
print(posb % 1000000)
   

