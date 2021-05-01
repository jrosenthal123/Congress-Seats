fname="us-states-populations.txt"
fh=open(fname)
seats=dict()
pop=dict()
mult=dict()

import math

for line in fh:
    line=line.rstrip()
    words=line.rsplit("\t", 1)
    seats[words[0]]=seats.get(words[0],0)+1
    words[1]=words[1].replace(",","")
    pop[words[0]]=pop.get(words[0],words[1])
    for i in range(2,70):
        dummy_mult=1/(math.sqrt(i*(i-1)))
        new_word=words[0]+"-"+str(i)
        mult[new_word]=dummy_mult*float(pop[words[0]])

lst = list()
lst2 = list()
for k, v in mult.items():
    newtup = (v, k)
    lst.append(newtup)

lst=sorted(lst, reverse=True)
lst=lst[:394]

for j in range(len(lst)):
    dum=lst[j][1].split("-",1)
    lst2.append(dum[0])

for j in lst2:
    seats[j]=seats.get(j,1)+1

with open("states_seats.txt","w") as fn:
    for k, v in seats.items():
        fn.write("%s\t%s\n" % (k, v))
