import sys

# echo '5 3' | python3 task4_Fibonacci.py 
# echo '31 4' | python3 task4_Fibonacci.py 
n,k=sys.stdin.readline().split(' ')
n=int(n)
k=int(k)
rabbits=[1,1]
for i in range(n-2):
   rabbits.append(rabbits[i]*k+rabbits[i+1])
print(rabbits)
