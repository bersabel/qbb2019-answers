#!/usr/bin/env python3

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
    target_seq_d[ident] = sequence
    
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
            value = kmer_positions[kmer]
            for ident,i in value:
                
                target_seq = target_seq_d[ident]
                length_target = len(target_seq)
                length_query  = len(sequence)
                extend_right = True
                extended_kmer = kmer 
                i = 0
                j = 0
            while True:
                if extend_right:
                    if sequence[k+j+1] == target_seq[k+i+1]:
                        i += 1
                        j += 1
                        extended_kmer += sequence[k+j+1]
                    else:
                        extend_right = False 
                    extension_list[extended_kmer] = target_seq 
                else:
                        break
                if i+k == length_target or j+k == length_query :
                        extend_right = False
                        break
sorted(extended_kmer, reverse = True, key = len)  
for extended_kmer in extension_list:
    print(extended_kmer)      
                        
                        
                        
                        
                        
