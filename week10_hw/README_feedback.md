Missing the overall t-SNE or UMAP plot with at least 8 cell types labeled (-1)
Basically where you code 
```sc.pl.umap(adata, color = 'leiden' , title = "UMAP")
sc.pl.umap(adata, color = ['Lhx6', "Dbi", "Nefm", "Adarb2", "C1qb", "Gria2", "Arpp21", "Bsg"] , 
           title = ['Lhx6', "Dbi", "Nefm", "Adarb2", "C1qb", "Gria2", "Arpp21", "Bsg"])``` 
Ideally that plot would have each cluster have a label for the gene (either on the plot directly or in the legend) 

4/5
