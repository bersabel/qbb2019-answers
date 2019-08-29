#!/usr/b#!/usr/bin/env python3

"""Count all kmers in a FASTA file """



from fasta import FASTAReader 
import sys

reader1 = FASTAReader(open( sys.argv[1])) #SUBSET/TARGET
reader2 = FASTAReader(open( sys.argv[2])) #QUERY/YAK
k = int( sys.argv[3] ) #K

kmer_positions = dict()
target_seq_d = {}
extension_list = {}

for ident, sequence in reader1:
    sequence = sequence.upper()
    target_seq[ident] = sequence
    for i in range( 0, len(sequence)-k+1 ):
        kmer = sequence[i:i+k]
        if kmer in kmer_positions:
            kmer_positions[kmer].append((ident,i))
        else:
            kmer_positions[kmer] = [(ident,i)]
         
for ident, sequence in reader2:
    sequence = sequence.upper()
    for j in range( 0, len(sequence)-k+1 ):
        kmer = sequence[j:j+k]
        if kmer in kmer_positions:
            key = kmer_positions[kmer]
            for ident,i in key:
                target_seq = target_seq_d[ident]
                length-target = len(target_seq)
                length-query  = len(sequence)
                extend_right = True
                exteded_kmer = kmer 
            while True:
                if extend_right:
                    if sequence[k+j+1] == target_seq[k+i+1]:
                        i += 1
                        j += 1
                        exteded_kmer += sequence[k+j+1]
                    else:
                        extend_right = False 
                # this is where I would add the extenstion  
                else:
                    break
                if i+k == length-target or j+k == length-query:
                        extend_right = False 
               
            
            
                






in/env python3

"""Count all kmers in a FASTA file """



from fasta import FASTAReader 
import sys

reader1 = FASTAReader(open( sys.argv[1])) #SUBSET/TARGET
reader2 = FASTAReader(open( sys.argv[2])) #QUERY/YAK
k = int( sys.argv[3] ) #K

kmer_positions = dict()
for ident, sequence in reader1:
    sequence = sequence.upper()
    
    for i in range( 0, len(sequence)-k+1 ):
        kmer = sequence[i:i+k]
        if kmer in kmer_positions:
            kmer_positions[kmer].append((ident,i))
        else:
            kmer_positions[kmer] = [(ident,i)]
         
for ident, sequence in reader2:
    sequence = sequence.upper()
    for j in range( 0, len(sequence)-k+1 ):
        kmer = sequence[j:j+k]
        if kmer in kmer_positions:
            key = kmer_positions[kmer]
            for ident,i in key:
                
                