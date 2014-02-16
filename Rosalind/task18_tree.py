import sys

# cat rosalind_tree.txt | python3 task18_tree.py

numinds=sys.stdin.readline()[:-1]
print(numinds)
edges=[]
for line in sys.stdin.readlines():
   inds=line[:-1].split(' ')

#   print(inds)
   edges.append(inds)
#print(edges)
inter_edges=edges[:]
currentlength_edges=len(edges)+1
while len(edges) < currentlength_edges:
   print(len(edges),currentlength_edges) 
   currentlength_edges=len(edges)
   for i in range(1,len(edges)):
      testset=edges[i-1][:]
   
      for j in range(i,len(edges)):
      
         compare=edges[j][:]
#         print(testset,compare,i,j)
         for k in range(len(compare)):

            if compare[k] in testset:
               newset=list(set(testset+compare))
               if testset in inter_edges and compare in inter_edges:
                  inter_edges.remove(testset)
                  inter_edges.remove(compare)
                  inter_edges.append(newset)
               break
               #print(inter_edges, newset)

   edges=inter_edges[:]
#print(edges)
print(len(edges))
            
# instinker: correcte antwoord: Nedges (regel1) - 1 - aantal edges in lijst.   
