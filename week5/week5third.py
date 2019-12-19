#!/usr/bin/env python3
# loop through the amino seq but theoutput is nt for the aminos that have letter the ones that dont have letter are sub to -
# count is based on pep but out is into the nuc 
# looping through the pep add counter add in range equation 
# add to the counter at the end after equation 
import fasta
import sys
import numpy as np 
import matplotlib.pyplot as plt

nt = fasta.FASTAReader(open(sys.argv[1]))
amino = fasta.FASTAReader(open(sys.argv[2]))
# print('start')
nt_all = []
for(nt_id, nt_seq), (amino_id, amino_seq) in zip(nt,amino):
    nuc = []
    inj = 0
    for pep in amino_seq: 
        if pep is "-":
            nuc.append("---")
        else:
            nseq = nt_seq[inj:inj+3]
            nuc.append(nseq)
        inj = inj+3
        nt_all.append(nuc)
            # print(nseq)
print(len(nt_all[0]))
        # print(len(nt_all))
codon = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
        
sys = []
countsys = 0
nonsys =[]
countnonsys = 0
i = 0
x = 0
dif = []
ratio = []
# for item in nt_all[0]:
#     if x < 500:
#         for pep in nt_all:
#             if item == pep[i]:
#                  pass
#             elif item not in codon:
#                  pass
#             elif pep[i] not in codon:
#                  pass
#             elif codon[item] == codon[pep[i]]:
#                  countsys += 1
#             elif codon[item] != codon[pep[i]]:
#                  countnonsys += 1
#             else :
#                  pass         
for item in nt_all[0]:
    for pep in nt_all:
        if item == pep[i]:
            pass
        elif item not in codon:
            pass
        elif pep[i] not in codon:
            pass
        elif codon[item] == codon[pep[i]]:
            countsys += 1
        elif codon[item] != codon[pep[i]]:
            countnonsys += 1
        else :
            pass
    print(x)
    x = x + 1 
    sys.append(countsys)
    nonsys.append(countnonsys)
    diff = countnonsys - countsys
    dif.append(diff)
    rat = countnonsys - countsys
    ratio.append(rat)
    countsys = 0
    countnonsys = 0
print(dif)
deviation = np.std(dif)
print(deviation)
zscore = dif/deviation
print(zscore)
zscore = []
for di in dif:
    zscor = di/deviation
    zscore.append(zscor)


sig = []
xaxis = []
notsig = []
xaxis2 = []
count = 0
for num in ratio:
    if zscore[count] < -2:
        sig.append(num)
        xaxis.append(count)
    else:
        notsig.append(num)
        xaxis2.append(count)
    count += 1 
print('third')
fig, ax = plt.subplots()
ax.set_title('ratio vs zscore')
ax.set_xlabel('postion')
ax.set_ylabel('ratio')
ax.scatter(xaxis,sig, color = "red" , s = 3, alpha = 0.3)
ax.scatter(xaxis2,notsig, color = "blue",  s = 3, alpha = 0.3)
fig.savefig('zscore vs position')
plt.close(fig)
  
# standard deviation
# zscore for postive selction 
    


    
    
