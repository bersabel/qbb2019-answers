#!/usr/bin/env python3



# align the contigs === gives me a fafsa file == Manipulate

# compute contgs , min/max, averg contig length and N50 

# align them to the genome command line 
# fafsa file read it from sys.argv
# fassa reader get reader and seq
# for each seq find length and store and count number contigs
# at the end find max,min,avg etc



import sys

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def next(self):
        
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        #If reach this point, ident is set correctly
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
        sequence = "".join(sequences)
        return ident, sequence 
        
for i in range(1, len(sys.argv)):
        contig_file = open(sys.argv[i])
        contig_reader = FASTAReader(contig_file)
        contig_counter = 0
        contig_lengths = []

        while True:
            ident, sequence = contig_reader.next()
            if not ident is None:
                contig_counter += 1
                contig_lengths.append(len(sequence))
            else:
                break
avegcontigs = sum(contig_lengths)/len(contig_lengths)
print("The min is", min(contig_lengths), "the max number is", max(contig_lengths), "the average is", avegcontigs, "number of contig is", contig_counter)   

# contigs_sorted = sorted(contig_lengths)
# avg_contigs_sorted = sum(contigs_sorted)/2
# for i in avg_contigs_sorted:       
# N50
# List with the length of count
#sort list
#add the list and divided by 2
# for i in list less than or greater than 
        
        # ./firstclasscode contigs.fasta

# comands for running 

# ./velveth outputvelvet 21 -fastq -shortPaired -spearate rreadslow.fa readslow2.fa
# ./velvetg outputvelvet 

# lastZ target query  target is refereance query is the contig.fa for each command long
 # --chain -- format = general and output
# truspades.py --only-assembler --pel-1 reads_low_1.fastq --pel-2 reads_low_fastq -o <namefolder>
# spades.py -s reads_low_1.fastq -sreads_low_2.fastq -o spades

#nanopore --nanopore followedby file name
#bettercoverage  (velvet and spades but different )
 





