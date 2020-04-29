# metagenome_mgsammlung
An automated continuous analytics pipeline for metagenomics datasets.

Current dir structure:
```bash
mgsammlung/
├── analysis
│   ├── 2020_01_15
│   ├── 2020_01_16
│   ├── 2020_01_26
│   ├── 2020_02_12
│   ├── 2020_02_25
│   ├── 2020_03_11
│   ├── 2020_03_23
│   ├── 2020_03_24
│   └── 2020_03_27
├── fastq
│   ├── CF
│   ├── COPD
│   ├── grumaz_2020_minion
│   ├── sepsis_2020_rxx
│   └── wheezer
├── metadata
│   ├── CF
│   ├── cleanup_txt_by_date.sh
│   ├── COPD
│   └── wheezer
└── scripts
    └── metagen_mgsammlung
```
Renamed FASTQ file format:
```bash
COPD
├── COPD1_D_MG000001_2016_R1.fastq
├── COPD1_D_MG000001_2016_R2.fastq
├── COPD1_D_MG000005_2016_R1.fastq
├── COPD1_D_MG000005_2016_R2.fastq
```
Analysis folder structure:
```bash
2020_01_15
└── wochenende1_2
    ├── COPD1_D_MG000001_2016_R1.ndp.fastq
    ├── COPD1_D_MG000001_2016_R1.ndp.fastq.stats
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.fastq
    ├── COPD1_D_MG000001_2016_R1.ndp.lc_seqs.fq.fastq
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.01mm.bam
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.01mm.dup.bam
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.01mm.dup.bam.bai
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.01mm.dup.calmd.bam
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.01mm.dup.calmd.bam.bai
    ├── COPD1_D_MG000001_2016_R1.ndp.lc.trm.s.mq30.bam
    ├── fastqc
    └── stats  
 ```
Metadata:

Metadata at the moment in stored in each sub-folder in xlsx format

Scripts:

metagen_mgsammlung on gitlab

updated versions of Wochenende pipeline from github public repository, https://github.com/MHH-RCUG/Wochenende

other tools, kraken-uniq, latest version available on gitlab and the RCUG cluster
