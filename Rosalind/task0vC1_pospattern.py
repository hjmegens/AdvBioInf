import sys

pattern=sys.stdin.readline()[:-1]
dna=sys.stdin.readline()[:-1]
n=len(pattern)
matches=[]
for i in range(len(dna)-n):
   if pattern==dna[i:i+n]:
      matches.append(i)
print(' '.join([str(match) for match in matches]))
