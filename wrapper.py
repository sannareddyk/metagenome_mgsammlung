#!/usr/bin/python3
"""
A wrapper script for running different metagenomics tools.
Author: Keerthi Sannareddy, June 2020


todo -
Add main method

Changelog
0.11 -refactor the two pipelines into methods/functions, write main function
0.10 initial commit

"""

import os
import glob
from datetime import date

version = 0.10
print("Version: " + version)

today = date.today()

# YY/mm/dd Date format
d1 = today.strftime("%Y__%m__%d")

##Wochenende pipeline
for file in glob.glob("*.fastq"):
    cmd = "sbatch run_Wochenende_SLURM.sh " + file
    os.system(cmd)

if not os.path.exists("analysis"):
    os.makedirs("analysis")

Version = os.system(
    "grep -m1 version run_Wochenende.py | awk -F '[\"-]' '{print $2}' - | sed 's/\./_/g'"
)

path = "analysis/" + d1 + "_Wochenende" + "_Version"

if not os.path.exists(path):
    os.makedirs(path)

# clean rundir after the run finishes and move data to path under analysis folder
os.system("sh cleanup.sh")

os.system("mv stats " + path)
os.system("mv fastqc " + path)

# get conda env and reference information
# conda env export >env.wochenende.yml
# reference and cmd line used can be extracted from slurm.out file

##krakenuniq pipeline
for file in glob.glob("*.fastq"):
    cmd = "sbatch run_krakenuniq_SLURM.sh " + file
    os.system(cmd)

if not os.path.exists("analysis"):
    os.makedirs("analysis")

path = "analysis/" + d1 + "_KrakenUniq" + "_Version"

if not os.path.exists(path):
    os.makedirs(path)

os.system("mv *.txt " + path)
os.system("mv *.xlsx " + path)

# get conda env and reference information
# conda env export >env.wochenende.yml
# reference and cmd line used can be extracted from slurm.out file
