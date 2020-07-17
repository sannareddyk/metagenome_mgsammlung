#!/bin/bash
outDir=$1
mkdir -p $outDir/stats
mkdir -p $outDir/fastqc


rm *.tmp
rm *.trm.fastq
rm *.trm.bam
rm *.trm.s.bam
rm *.trm.s.bam.bai
mv *.bam.stats $outDir/stats
mv *.bam.txt $outDir/stats
mv *_out $outDir/fastqc
mv *ndp* $outDir
#srun -c 56 pigz -p 56 *.fastq &


