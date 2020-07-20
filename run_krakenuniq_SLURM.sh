#!/bin/bash

# set partition
#SBATCH -p normal

# set run on bigmem node only
#SBATCH --mem 500000

# set run on 16 cores
#SBATCH --cpus-per-task 16

# set max wallclock time
#SBATCH --time=47:00:00

# set name of job
#SBATCH --job-name=runKrakUniq

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<mail_address_for_slurm>

#Add miniconda3 to PATH
. /mnt/sfb900nfs/groups/tuemmler/keerthi/miniconda3/etc/profile.d/conda.sh

#activate env on cluster
conda activate krakenuniq

#db path
db=/lager2/rcug/seqres/metagenref/krakenuniq/db

echo "Input file: " $1
echo "Output dir: " $2
fastq=$1
outDir=$2
	krakenuniq --db $db --preload
	krakenuniq --db $db --threads 16 $fastq --report-file $outDir/$fastq.report.txt --unclassified-out $outDir/$fastq.unclassified.txt --classified-out $outDir/$fastq.classified.txt --output $outDir/$fastq.output.txt
