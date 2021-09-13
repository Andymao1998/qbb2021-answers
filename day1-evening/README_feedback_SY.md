### Comments

Great: Clean for loops.

To improve: It would be nice to have your code documented better - right now you just pasted in the code from your jupyter cells, but it's hard to tell what's going on if you're not super familiar with the assignment. Same goes for formatting the output so that it's readable.

I like your use of a set to identify PCR duplicates. But I think this may be identifying the # of alignments that have at least one PCR duplicate, not the actual number of duplicates. If you wanted to do this, you would have to compare the CIGAR strings of alignments to the CIGAR string of the previous alignment.

### Completion:

Found:
Python script
Output file

Missing:
