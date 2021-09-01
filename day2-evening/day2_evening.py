import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = int(sys.argv[3])

from fasta_reader import FASTAReader
fs = open(arg1)
sequence_1 = FASTAReader(fs)
query_gene = sequence_1[0][1]
kmers_query = {}
for i in range(0, len(query_gene) - arg3):
    kmer = query_gene[i:i+arg3]
    kmers_query.setdefault(kmer,0)
    kmers_query[kmer] = (i,i+arg3)

#for key in kmers_query:
#    print(key, kmers_query[key]) 

table = open(arg2)
sequence_2 = FASTAReader(table)
blast = {}
for t in range(0, len(sequence_2)):
    name = sequence_2[t][0]
    target_gene = sequence_2[t][1]
    for c in range(0, len(target_gene)-arg3):
        kmer_target = target_gene[c:c+arg3]
        if kmer_target in kmers_query.keys():
            print(name, kmers_query[kmer_target][0], c, kmer_target)

