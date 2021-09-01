import sys #Let us access system-specific parameters and functions. This function provides the name of the existing python modules which have been imported.

gtf_file = sys.argv[1] # set first system argument
mut_chrom = sys.argv[2] # set second system argument
mut_pos = int(sys.argv[3]) # set thir system argument. Set input as an interger
f = open(gtf_file) # opens a file, and returns it as a file object

genes = [] # create an empty list called genes
for line in f: # create a for loop for each line in the file
    if line.startswith("#"): # if line starts with #, we don't want the information
        continue # if this is the case, continue let us starts the next loop
    fields = line.strip("\r\n").split("\t") # We strip each line off new line character and carriage return character
    start = int(fields[3]) # extract the start position of the gene profile, make the start an integer
    end = int(fields[4]) # extract the end position of the gene profile, make the end an integer
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';') # search for protein coding genes on the designated chromosome location
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1] # Extract gene names
        genes.append((gene_name, start, end)) #create a list of tuples including the name, start, and end positions of each protein coding gene.
#print(genes)

lo = 0 # define low
hi = len(genes) # define high
condition = 0 # set default condition
query = mut_pos # set query matching the third system argument
n = 0 # set the tally
mid=0 # set default mid for quality check
while condition==0: # when the condition is TRUE, enter while loop
    old_mid = mid 
    mid =(1/2)*(lo + hi) # define mid as the average of lo and hi
    gene_name = genes[int(mid)][0] # extract gene name from the tuple
    gene_info_start = genes[int(mid)][1] # extract start location
    gene_info_end = genes[int(mid)][2] # extract end location
    n += 1 # add 1 each time the while loop is executed
    if (gene_info_start <= query) and (query <= gene_info_end):
        print(gene_name, str(query-gene_info_start))
        condition = 2 # if we find the perfect match, set condition = false to exit the loop
    elif int(old_mid) == int(mid):# if the mid of our definition is constant, while the first argument is not true. The situation indicates that we can't find the perfect match per description and we need to output the neighboring two data for further comparison
        print(genes[int(lo)][0], genes[int(lo)][1], genes[int(lo)][2], genes[int(hi)][0], genes[int(hi)][1],genes[int(hi)][2])
        gene_1 = genes[int(lo)]
        gene_2 = genes[int(hi)]
        gene_o = [gene_1, gene_2]
        condition = 2 # set condition to exit the loop
    elif query < gene_info_start: # if the query is smaller than the start site of the called gene, we set the hi to be the current mid value
        hi = mid
    else:
        lo = mid # if the query is bigger than the end site of the called gene, we set the lo to be the current mid value
print("Iteration Number",n) # After the loop, we want to display the iteration number
for t in gene_o: # We have a list of the two genes, each element of the list is a tuple containing gene name, start site, end site.
    distance = min(abs(t[1]-query),abs(t[2]-query)) # calculate the distance between each gene and the query location
    print(t[0], distance) 