import sys
# echo 'ACGACGTTTA' | python3 task1_Counting_nucleotides.py

for line in sys.stdin.readlines():
   As=line.count('A')
   Cs=line.count('C')
   Gs=line.count('G')
   Ts=line.count('T')
print(As,Cs,Gs,Ts)
