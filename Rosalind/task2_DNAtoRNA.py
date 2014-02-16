import sys
# echo 'ACGACGTTTA' | python3 task2_DNAtoRNA.py

for DNA in sys.stdin.readlines():
   RNA=DNA.replace('T','U')
   print(RNA)
