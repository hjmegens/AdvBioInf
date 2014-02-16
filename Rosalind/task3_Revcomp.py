import sys
# echo 'ACGACGTTTA' | python3 task3_Revcomp.py
# cat rosalind_revc.txt | python3 task3_Revcomp.py
forward=''
for line in sys.stdin.readlines():
   forward=forward+line[:-1]

revcomp=forward.translate(str.maketrans('ACGT','TGCA'))[::-1]
print(revcomp)
