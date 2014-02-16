import sys

mydict=dict()
for line in sys.stdin.readlines():
   parts=line[:-1].split(' ')
   for part in parts:
      if part in mydict.keys():
         mydict[part]+=1
      else:
         mydict[part]=1
for key in mydict.keys():
   print(key,mydict[key])



