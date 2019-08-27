#!/bin/bash
GENOME=/Users/cmdb/qbb2019-answers/genomes/BDGP6
ANNOTATION=/Users/cmdb/qbb2019-answers/genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq 
  hisat2 -p 4 -x $GENOME -U $SAMPLE.fastq  -S $SAMPLE.sam 
  samtools sort -@ $THREADS $SAMPLE.sam  -O bam  > $SAMPLE.sorted.bam
  samtools index $SAMPLE.sorted.bam
  stringtie $SAMPLE.sorted.bam -e -B -p $THREADS -G $ANNOTATION -o quantitate.$SAMPLE.bam
 done
 