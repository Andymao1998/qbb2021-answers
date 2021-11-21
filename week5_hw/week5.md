# Part 1: ChIP-seq

wget https://bx.bio.jhu.edu/data/msauria/cmdb-lab/g1e.tar.xz
get the data

tar xzf g1e.tar.xz
unpack the data

# Mapping reads

bowtie2 -x /Users/cmdb/data/indexes/bowtie2/mm10/mm10 -U CTCF_ER4.fastq -S CTCF_ER4.sam
bowtie2 -x /Users/cmdb/data/indexes/bowtie2/mm10/mm10 -U CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x /Users/cmdb/data/indexes/bowtie2/mm10/mm10 -U input_ER4.fastq -S ER4.sam
bowtie2 -x /Users/cmdb/data/indexes/bowtie2/mm10/mm10 -U input_G1E.fastq -S G1E.sam

Pay attention that these are unpaired reads, by using less command 

# Mapping reads

conda activate 
enter chipseq environment
pip install --upgrade numpy

macs2 callpeak -t CTCF_ER4.sam -c ER4.sam --name=CTCF_ER4 --gsize=61000000 --bdg 
macs2 callpeak -t CTCF_G1E.sam -c G1E.sam --name=CTCF_G1E --gsize=61000000 --bdg 

# Differential binding

## Sites gained during differentiation
bedtools subtract -A -a ER4/CTCF_ER4_peaks.narrowPeak -b G1E/CTCF_G1E_peaks.narrowPeak > differential_binding_ER4 
sites gained during differentiation

## Sites lost during differentiation
bedtools subtract -A -a G1E/CTCF_G1E_peaks.narrowPeak -b ER4/CTCF_ER4_peaks.narrowPeak > differential_binding_G1E 
sites lost during differentiation

## Feature overlapping
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b G1E/CTCF_G1E_peaks.narrowPeak > G1E_intersect 

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b ER4/CTCF_ER4_peaks.narrowPeak > ER4_intersect



## Feature geenration for the sites that are either gained or lost after differentitaion 

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b differential_binding_ER4 > sites_gained_after_diferentiation

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b differential_binding_G1E > sites_lost_after_diferentiation


# Plotting is demonstrated in Jupyter Notebook

## Motif Discovery
mkdir jaspar
cd jaspar
wget http://jaspar2018.genereg.net/download/CORE/JASPAR2018_CORE_non-redundant_pfms_meme.zip
unzip JASPAR2018_CORE_non-redundant_pfms_meme.zip

sort -k8,8nr ER4/CTCF_ER4_peaks.narrowPeak > ER4_sorted.narrowPeak
head -n 100 ER4_sorted.narrowPeak > ER4_top100
bedtools getfasta -fi /Users/cmdb/data/genomes/mm10.fa -bed ER4_top100 > ER4_top100.fa


meme-chip -db /Users/cmdb/data/meme_db/motifs/motif_databases.12.21.tgz ER4_top100.fa
tomtom memechip_out/meme_out/meme.txt  ~/qbb2021-answers/week5_hw/jaspar/JASPAR2018_CORE_non-redundant_pfms_meme/MA*