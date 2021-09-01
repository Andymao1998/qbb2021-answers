import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = int(sys.argv[3])

from fasta_reader import FASTAReader # wget the FASTA Parser file from the lecture in the terminal, import the function into the script
fs = open(arg1) # open the file
sequence_1 = FASTAReader(fs) # Use the FASTAReader function on the target file
query_gene = sequence_1[0][1] # the query gene Fasta file only has one tuple consisting of one gene, pull out the sequence
kmers_query = {} # create an empty list
for i in range(0, len(query_gene) - arg3): # K-mer generater using a for loop, the k-mer has to span the range of the sequence length - k-mer length
    kmer = query_gene[i:i+arg3] # show the sequence of the k-mer
    kmers_query.setdefault(kmer,0) # set the default in the dictionary
    kmers_query[kmer] = (i,i+arg3) # add each k-mer's sequence and its location into the dictionary (location is stored as a tuple)

#for key in kmers_query:
#    print(key, kmers_query[key]) 

table = open(arg2) # open the target file
sequence_2 = FASTAReader(table) # process the file through FASTA to generate the gene list
blast = {} # create an empty dictionary
for t in range(0, len(sequence_2)): # Out loop for each of the gene in the target file
    name = sequence_2[t][0] # extract the name
    target_gene = sequence_2[t][1] # extract the sequence
    for c in range(0, len(target_gene)-arg3 + 1): # in each of the gene, create an inner loop to k-merize
        kmer_target = target_gene[c:c+arg3]
        if kmer_target in kmers_query.keys(): # match the target k-mer against the query k-mer dictionary 
            print(name, kmers_query[kmer_target][0], c, kmer_target)# if a match exists, print out the name of the gene in the target file, the start position of the k-mer from the query, the start position of the k-mer in the target [overlap location of the gene, and the sequence of the k-mer.]
            
        

