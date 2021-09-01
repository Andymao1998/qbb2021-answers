import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
mut_pos = int(sys.argv[3])
f = open(gtf_file)

genes = []
for line in f:
    if line.startswith("#"):
        continue
    fields = line.strip("\r\n").split("\t")
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1]
        genes.append((gene_name, start, end))
#print(genes)

lo = 0
hi = len(genes)
condition = 0
query = mut_pos
n = 0
mid=0
while condition==0:
    old_mid = mid
    mid =(1/2)*(lo + hi)
    gene_name = genes[int(mid)][0]
    gene_info_start = genes[int(mid)][1]
    gene_info_end = genes[int(mid)][2]
    n += 1
    if (gene_info_start <= query) and (query <= gene_info_end):
        print(gene_name, str(query-gene_info_start))
        condition = 2
    elif old_mid == mid:
        print(genes[int(lo)][0], genes[int(lo)][1], genes[int(lo)][2], genes[int(hi)][0], genes[int(hi)][1],genes[int(hi)][2])
        gene_1 = genes[int(lo)]
        gene_2 = genes[int(hi)]
        gene_o = [gene_1, gene_2]
        condition = 2
    elif query < gene_info_start:
        hi = mid
    else:
        lo = mid
print("Iteration Number",n)
for t in gene_o:
    distance = min(abs(t[1]-query),abs(t[2]-query))
    print(t[0], distance)