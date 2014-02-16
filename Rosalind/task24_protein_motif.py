import sys
import urllib.request
import re
# cat test_prot_motif.txt | python3 task24_protein_motif.py
# cat rosalind_mprt.txt | python3 task24_protein_motif.py
# 'MLNIHK*EDGFACYTWVQPSR'
# 'MLNIHK*EDGFACYTWVQSR'
# N{P}[ST]{P}
prots=[part[:-1] for part in sys.stdin.readlines()]
print(prots)
allprots=[]
for prot in prots:
   req = urllib.request.Request('http://www.uniprot.org/uniprot/'+prot+'.fasta')
   response = urllib.request.urlopen(req)
   the_page = str(response.read())
   record=the_page.split(r'\n',1)
   allprots.append([prot,record[1].replace(r'\n','').replace(r"'",'')])
#print(allprots)
lengthmatch=4
for prot in allprots:
   protid=prot[0]
   seq=prot[1]
   pos=[]
   for i in range(len(seq)-lengthmatch):
      if re.match(r'N[MLNIHKEDGFACYTWVQSR][ST][MLNIHKEDGFACYTWVQSR]',seq[i:i+4]):
         pos.append(i+1)
   
   #m=re.finditer(r'N[MLNIHKEDGFACYTWVQSR][ST][MLNIHKEDGFACYTWVQSR]',seq)
   #pos=[match.start()+1 for match in m]
   if len(pos)>0:
      print(protid)
      print(' '.join([str(p) for p in pos]))
      
   
