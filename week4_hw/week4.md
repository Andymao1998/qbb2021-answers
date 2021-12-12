## Assignment 4: DNA Methylation

### creating the environment
conda create -n week6 -c bioconda -c anaconda fastqc bismark samtools bowtie2 igv

### Look for a section called Accession Numbers (Usually in the “Data Availability” section after the discussion). Use the information you find there to locate the data in the sequence read archive.
 
Accession Number GSE76505.

SRX1515374: GSM2027208: RNA-Seq E4.0ICM rep1; Mus musculus; RNA-Seq

SRX1515397: GSM2027231: STEM-seq E5.5Epi rep1; Mus musculus; Bisulfite-Seq

### creating an index folder and move chr6.fa.gz into this folder.
mkdir index 
mv chr6.fa.gz index

### Unpack the data
mkdir raw
cd raw
tar xzf methylation_fastq.tar.gz

## Bisulfite mapping with Bismark

bismark_genome_preparation --parallel 7 index chr6.fa.gz


bismark index -1 SRR3083926_1.chr6.fastq -2 SRR3083926_2.chr6.fastq -B E4.0ICM
bismark index -1 SRR3083929_1.chr6.fastq -2 SRR3083929_2.chr6.fastq -B E5.5Epi


## Remove the duplicates
deduplicate_bismark -p E4.0ICM_pe.bam -o E4.0ICM --bam

deduplicate_bismark -p E5.5Epi_pe.bam -o E5.5Epi --bam


##  create sorted BAM files and index

samtools sort -o E4.0ICM_sorted -O BAM E4.0ICM.deduplicated.bam
samtools sort -o E5.5Epi_sorted -O BAM E5.5Epi.deduplicated.bam

samtools index -b E4.0ICM_sorted.bam
samtools index -b E5.5_sorted.bam


## To extract methylation data

bismark_methylation_extractor -p --bedgraph --comprehensive E4.0ICM.deduplicated.bam
bismark_methylation_extractor -p --bedgraph --comprehensive E5.5Epi.deduplicated.bam



## extract the promoters and write them to a bed file and remove duplicates

awk 'BEGIN{OFS="\t"}{if ($4 == "+") print $3,$5 - 2000,$5,$13,$12,$4; else print $3,$6,$6 + 2000,$13,$12,$4;}' mm10_refseq_genes_chr6_50M_60M.bed | grep -v Rik | uniq -f 3 | sort -k2,2n > promoters.bed



## For each promoter, find the total methylation signal in E4 to E5.5 cells (sum all methylation site scores). 

methylation scores occuring in each promoter for E4.0 cells
bedtools map -a promoters.bed -b E4.0ICM.deduplicated.bedGraph -c 4 -o sum > E4.0_promoter
bedtools map -a promoters.bed -b E5.5Epi.deduplicated.bedGraph -c 4 -o sum > E5.5_promoter