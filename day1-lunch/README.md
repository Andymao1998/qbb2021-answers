#This is for excercise 1.c#

(base) (12:44:48)~/qbb2021-answers/$cp /Users/cmdb/qbb2021/data/*.bed day1-lunch

(base) (12:49:40)~/qbb2021-answers/day1-lunch/$cp /Users/cmdb/qbb2021/data/dm6.chrom.sizes day1-lunch

#This is for excercise 2.b#

(base) (13:15:35)~/qbb2021-answers/day1-lunch/$wc -l *.bed

Biological observations:

#1 K27me3 marks are more prevalent in comparison to K4me3 and K9me3

#2 LADs in Drosophila melanogaster are limited to chromosome 2, 3 and X

#Summarize distribution of gene annotations across chromosomes#

(base) (13:48:07)~/qbb2021-answers/day1-lunch/$cut -f 1 fbgenes.bed | uniq -c

#Biological observations for question 3#

1. There are more gene annotations on chromosome 3 in total than on chromosome 2

2. There are very few genes on chromosome Y or chromosome M

#4 

(base) (22:48:38)~/qbb2021-answers/day1-lunch/$bedtools intersect -a fbgenes.bed -b K9me3.bed -wa | cut -f 1 | uniq -c  

Observations for question 4 

1. Chromosome 2,3, and X has more genes with H3K9 marks compared with chromosome 4

2. Chromosome Y has few genes with H3K9 activation marks in comparison to other chromosomes.

3. On chromosome 2, the left arm emcompass more genes with H3K9 marks while on chromosome 3, vice versa.
