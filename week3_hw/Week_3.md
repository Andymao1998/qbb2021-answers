### Visualize genetic relatedness between the strains by performing principal component analysis and plotting the first two components.
VCF=~/qbb2021-answers/week3_hw/genotypes.vcf
plink --vcf $VCF --double-id --allow-extra-chr --set-missing-var-ids @:#  --make-bed --out pruned
plink --vcf $VCF --double-id --allow-extra-chr --set-missing-var-ids @:#--make-bed --pca --out genotypes
less -S genotypes.eigenvec

### Visualize the allele frequency spectrum by plotting a histogram of allele frequencies.
plink --vcf $VCF --freq --out allele_freq
plotting steps shown in jupyter notebook

### Using plink, perform quantitative association testing for each phenotype. Use the top 10 principal components (eigenvectors) as covariates in your analysis, to adjust for non-independence due to relatedness.

plink --vcf $VCF --pheno CB1908_IC50.txt --allow-no-sex --covar top_10_PC.txt --assoc --out CB1908_IC50

plink --vcf $VCF --pheno GS451_IC50.txt.txt --allow-no-sex --covar top_10_PC.txt --assoc --out GS451_IC50

