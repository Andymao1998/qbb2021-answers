### Getting the data
wget "https://github.com/bxlab/qbb2021/raw/main/week2/BYxRM_subset.tar.xv"
decompress the target file
tar -xvzf BYxRM_subset.tar.xv

I will be aligning reads from your yeast samples to the Saccharomyces cerevisiae reference genome. This reference is called sacCer3 by the UCSC genome browser, but its name in the NCBI Assembly archive is R64-1-1. You need this info later for snpEff.

wget "http://hgdownload.soe.ucsc.edu/goldenPath/sacCer3/bigZips/chromFa.tar.gz"
tar -xvzf chromFa.tar.gz
cat chr*.fa > sacCer3.fa 
concatenate the all chromosome files into one file sacCer3.fa
rm chr*.fa
remove all the original chromosome.fa files 


### Step 1: Index the sacCer3 genome
bwa index sacCer3.fa

### Step 2: Alignment with bwa mem
Align your reads against the sacCer3 reference genome.
bwa mem -o SAM/aln-se-*.sam -R "@RG\tID:Sample*\tSM:Sample*" sacCer3.fa A01_*.fastq
*denoting 9, 11, 23, 24, 27, 31, 35, 39, 62, 63

### Step 3: Create a sorted bam file with samtools, for input to variant callers
-o flag to provide output argument while -O to specifiy the format of the output file 
(base) (16:01:02)~/qbb2021-answers/week2_hw/SAM/$samtools sort -O BAM -o aln-se-*.bam aln-se-*.sam
*denoting 9, 11, 23, 24, 27, 31, 35, 39, 62, 63

### Step 4: Variant calling with freebayes
Use freebayes to identify genetic variants in all of your yeast strains concurrently. It will output results in Variant Call Format (VCF). You should consider using the -f, --genotype-qualities, and -p flags.

tar -xvzf freebayes-1.3.5-src.tar.gz



#### Check for function of the flags
freebayes --help
freebayes -f sacCer3.fa -p 1 -= *.bam > var.vcf


### Step 5: Filter variants based on genotype quality using vcffilter
Filter your VCF so that you only keep variants whose estimated probability of being polymorphic is greater than 0.99. You should consider how to do this with the -f flag.

options:
    -f, --info-filter     specifies a filter to apply to the info fields of records,
                          removes alleles which do not pass the filter
    -g, --genotype-filter specifies a filter to apply to the genotype fields of records
    -k, --keep-info       used in conjunction with '-g', keeps variant info, but removes genotype
    -s, --filter-sites    filter entire records, not just alleles
    -t, --tag-pass        tag vcf records as positively filtered with this tag, print all records
    -F, --tag-fail        tag vcf records as negatively filtered with this tag, print all records
    -A, --append-filter   append the existing filter tag, don't just replace it
    -a, --allele-tag      apply -t on a per-allele basis.  adds or sets the corresponding INFO field tag
    -v, --invert          inverts the filter, e.g. grep -v
    -o, --or              use logical OR instead of AND to combine filters
    -r, --region          specify a region on which to target the filtering, requires a BGZF
                          compressed file which has been indexed with tabix.  any number of
                          regions may be specified.

Filter the specified vcf file using the set of filters.
Filters are specified in the form "<ID> <operator> <value>:
 -f "DP > 10"  # for info fields
 -g "GT = 1|1" # for genotype fields
 -f "CpG"  # for 'flag' fields

Operators can be any of: =, !, <, >, |, &

Any number of filters may be specified.  They are combined via logical AND
unless --or is specified on the command line.  Obtain logical negation through
the use of parentheses, e.g. "! ( DP = 10 )"

For convenience, you can specify "QUAL" to refer to the quality of the site, even
though it does not appear in the INFO fields.

type: filter

vcffilter -f "QUAL > 20" vcr.vcf > vcr.vcf.refined

### Step 6: Decompose complex haplotypes using vcfallelicprimitives
We suggest using the -k and -g flags to keep annotations for the variant sites and sample genotypes in your VCF.


options:
    -m, --use-mnps          Retain MNPs as separate events (default: false).
    -t, --tag-parsed FLAG   Tag records which are split apart of a complex allele with this flag.
    -L, --max-length LEN    Do not manipulate records in which either the ALT or
                            REF is longer than LEN (default: 200).
    -k, --keep-info         Maintain site and allele-level annotations when decomposing.
                            Note that in many cases, such as multisample VCFs, these won't
                            be valid post-decomposition.  For biallelic loci in single-sample
                            VCFs, they should be usable with caution.
    -g, --keep-geno         Maintain genotype-level annotations when decomposing.  Similar
                            caution should be used for this as for --keep-info.

Type: transformation

vcfallelicprimitives -k -g var.vcf.refined > allelic.primitive

### Step 7: Variant effect prediction with snpeff ann
snpeff download R64-1-1.99
snpeff ann R64-1-1.99 allelic.primitive > prediction.vcf

### Step 8: Exploratory data analysis through plotting
In Python, produce a nicely formatted and labeled multi-panel plot describing your variants.
I choose bcftools for the initial extraction of data from vcf file
Download bcftools 
tar -xvzf bcftools-1.13.tar.bz2
cd bcftools-1.13  
./configure --prefix= /Users/cmdb/miniconda3/bin
make
make install

export PATH=/Users/cmdb/miniconda3/bin/bin:$PATH


bcftools query -f '%DP\n' prediction.vcf > read.depth.csv
bcftools query -f '%QUAL\n' prediction.vcf > qual.csv
bcftools query -f '%AF\n' prediction.vcf > allele_freq.csv
bcftools query -f '%ANN\n' prediction.vcf > variant.info


Proceed to Jupyter Notebook :>


