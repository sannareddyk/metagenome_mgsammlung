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
import sys
import subprocess
import glob
from datetime import date
import threading
import time

start = time.time()

version = 0.11
print("Version: " + str(version))

wochenendeVersion = "1_6_7"
print("wochenendeVersion: " + wochenendeVersion)

krakenUniqVersion = "1_1"
print("krakenUniqVersion: " + krakenUniqVersion)


stage_infile = ""

#############
#Initialization functions
#############
def runStage(stage, programCommand):
    # Run a stage of this Pipeline
    print("######  "+ stage + "  ######")
    try:
        #print(programCommand)
        process = subprocess.Popen(programCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()
        process.wait()
    except OSError as e:
        print(programCommand)
        print("Execution failed:", e, file=sys.stderr)
        sys.exit(1)

def getDate():
    today = date.today()
    d = today.strftime("%Y_%m_%d")
    return d

##############
# Pipeline functions
############

def runWochenende(stage_infile):
    # run Wochenende pipeline
    global dirNameWochenende
    stage = "run Wochenende pipeline"
    dirNameWochenende = "analysis/" + getDate() + "Wochenende" + wochenendeVersion
    #print(dirNameWochenende)

    if not os.path.exists(dirNameWochenende):
        os.makedirs(dirNameWochenende)
        print("Directory",dirNameWochenende,"created")
    #else:
	#print("Directory",dirNameWochenende,"already exists")

    wochenendeCmd = ['sbatch', 'run_Wochenende_SLURM.sh', stage_infile]
    runStage(stage, wochenendeCmd)

def runKrakenuniq(stage_infile):
    ##krakenuniq pipeline
    global dirNameKrakenuniq
    stage = "run Krakenuniq pipeline"
    dirNameKrakenuniq = "analysis/" + getDate() + "KrakenUniq" + krakenUniqVersion
    

    if not os.path.exists(dirNameKrakenuniq):
        os.makedirs(dirNameKrakenuniq)
	#print("Directory", dirNameKrakenuniq, "created")
    #else:
	#print("Directory", dirNameKrakenuniq, "already exists")

    krakenuniqCmd = ['sbatch', 'run_krakenuniq_SLURM.sh', stage_infile]
    runStage(stage, krakenuniqCmd)

###########
#main function
###########

def main():
        for file in glob.glob("*R1.fastq"):
            runWochenende(file)
            runKrakenuniq(file)
        
        #while True:
           # if time.time() - start >1800:
                #break
                #os.system("sh cleanup.sh")
                #os.system("mv stats " + dirNameWochenende)
                #os.system("mv fastqc " + dirNameWochenende)
                #os.system("mv *.report.txt " + dirNameKrakenuniq)
                #os.system("mv *.xlsx " + dirNameKrakenuniq)
        
main()


