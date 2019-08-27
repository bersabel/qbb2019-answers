
#a
head -n 40000 ../day2-morning/SRR072903.fastq > SRR072903.10K.fastq
wc -l SRR072903.10K.fastq 
#b
fastqc SRR072903.10K.fastq
#c
hisat2 [options]* -x <ht2-idx> {-1 <m1> -2 <m2> | -U <r> | --sra-acc <SRA accession number>} [-S <sam>]
hisat2 -p 4 -x /Users/cmdb/qbb2019-answers/genomes/BDGP6 -U /Users/cmdb/qbb2019-answers/day2-lunch/SRR072903.10K.fastq -S  /Users/cmdb/qbb2019-answers/day2-lunch/SRR072903.sam

#d
samtools view -S -b sample.sam > sample.bam
samtools sort - o bam sample.bam > sample.sorted.bam

samtools view -S -b sample.sam | samtools sort -O bam  > sample.sorted.bam
samtools view -S -b SRR072903.sam | samtools sort -O bam  > SRR072903.sorted.bam
#e
/Users/cmdb/qbb2019-answers/day2-lunch/SRR072903.sorted.bam -e -B -p 4 -G /Users/cmdb/qbb2019-answers/genomes/BDGP6.Ensembl.81.gtf -o quantitate.SRR072903.bam
