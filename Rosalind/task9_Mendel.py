import sys

# hom_dom,het,hom_recessive - what is prob of ofspring with dominant allele?
#echo '25 27 22' | python3 task9_Mendel.py 
#0.7720288781932618

homdom,het,homrec = sys.stdin.readline()[:-1].split(' ')
homdom=int(homdom)
het=int(het)
homrec=int(homrec)
allinds=homdom+het+homrec

hethet=((1/allinds)*(1/(allinds-1))*het*(het-1))/4
homrechomrec=(1/allinds)*(1/(allinds-1))*homrec*(homrec-1)
homrechet=(1/allinds)*(1/(allinds-1))*homrec*het*2*0.5

notdom=hethet+homrechomrec+homrechet
dom=1-notdom
print(dom)
