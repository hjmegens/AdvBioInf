import sys
# echo '17104 17298 19427 16437 18266 16731' | python3 task20_expected_offspring.py

#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa
#1 0 0 1 0 1
# 3.5
counts = sys.stdin.readline()[:-1].split(' ')
print(counts)


offspring=0
for i in range(len(counts)):
   if i == 0:
     offspring+=int(counts[i])*2 
   elif i == 1:
     offspring+=int(counts[i])*2
   elif i == 2:
     offspring+=int(counts[i])*2
   elif i == 3:
     offspring+=int(counts[i])*2*0.75
   elif i == 4:
     offspring+=int(counts[i])*2*0.5
print(offspring)
