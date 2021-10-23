#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys

arg1 = sys.argv[1]
arg2 = pd.read_csv(sys.argv[2], sep = '\s+', index_col=0)
gap_penalty = float(sys.argv[3])
path = sys.argv[4]


fsarg1 = open(arg1)
from fasta_reader import FASTAReader
g = FASTAReader(fsarg1)
query_1 = g[0][1]
query_2 = g[1][1]


F_matrix = np.zeros((len(query_1)+1, len(query_2)+1))
TB_matrix = np.empty((len(query_1)+1, len(query_2)+1))
TB_matrix[0, 0] = 0

for i in range(len(query_1)+1):
    F_matrix[i,0] = i * gap_penalty
for j in range(len(query_2)+1):
    F_matrix[0,j] = j*gap_penalty

for i in range(1, len(query_1)+1):
    for j in range(1, len(query_2)+1):
        d = F_matrix[i-1, j-1] + arg2[query_1[i-1]].loc[query_2[j-1]]
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty
        F_matrix[i, j] = max(d, h, v) 
        if max(d, h, v) == d:
            TB_matrix[i, j] = 1
        elif max(d, h, v) == h:
            TB_matrix[i, j] = 2
        elif max(d, h, v) == v:
            TB_matrix[i, j] = 3

sequence_1_align = ""
sequence_2_align = ""
gap1_count = 0
gap2_count = 0
a = len(query_1)
b = len(query_2)
while a >= 1 and b >= 1:
    if TB_matrix[a, b] == 1:
        sequence_1_align = query_1[a - 1] + sequence_1_align
        sequence_2_align = query_2[b - 1] + sequence_2_align
        a = a - 1
        b = b - 1
    elif TB_matrix[a, b] == 2:
        sequence_1_align = '-' + sequence_1_align
        sequence_2_align = query_2[b - 1] + sequence_2_align
        b = b - 1
        gap1_count += 1
        
    elif TB_matrix[a, b] == 3:
        sequence_1_align = query_1[a - 1] + sequence_1_align
        sequence_2_align = '-' + sequence_2_align
        a = a - 1
        gap2_count += 1
    
    elif TB_matrix[a, b] == 0:
        break

g1 = open("Protein_1.txt","w+")
g1.write(sequence_1_align)
g1.close()

g2 = open("Protein_2.txt","w+")
g2.write(sequence_2_align)
g2.close()

g3 = open("info_AA.txt", "w+")
g3.write("alignment score:" + str(F_matrix[len(query_1), len(query_2)]) + '\n' + "gaps in AA 1" + ":" + str(gap1_count) + '\n' 
+ "gaps in AA 2" + ":" + str(gap2_count))

# df = pd.DataFrame(data=F_matrix.astype(float))
# df.to_csv('path/F-out.csv', sep=' ')
