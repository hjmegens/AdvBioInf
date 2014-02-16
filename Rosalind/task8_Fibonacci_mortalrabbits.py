import sys
# echo '89 20' | python3 task8_Fibonacci_mortalrabbits.py
n,m=sys.stdin.readline().split(' ')
n=int(n)
m=int(m)
k=1
rabbits=[]
for j in range(m+1):
   rabbits.append(0)

rabbits[1]=1
rabbits[-1]=1
rabbits=[rabbits]
print(rabbits)
for i in range(n-2):
   nextgen=[]
   for j in range(m+1):
      nextgen.append(0)

   for j in range(1,m):
      nextgen[j]=rabbits[len(rabbits)-1][j-1]
   
   fertile=0
   for val in nextgen:
      fertile+=val
   fertile+=rabbits[len(rabbits)-1][m-1]
   fertile-=nextgen[1]
   print(rabbits[len(rabbits)-1][m-1])
   nextgen[0]=fertile
   tot=0
   for val in nextgen:
      tot+=val
   nextgen[m]=tot
   #nextgen[0]=fertile+fertile-rabbits[len(rabbits)-1][m-1]
   rabbits.append(nextgen)
print(rabbits)
