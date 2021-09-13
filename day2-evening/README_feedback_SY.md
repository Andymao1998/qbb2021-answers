### Comments

Great: Awesome documentation!!! Although I agree with Mike's comment about putting the documentation and the code on separate lines for readability.

To improve: How will you account for situations where the same kmer exists in multiple locations in the query sequence? Right now, your dictionary will overwrite the entry for that kmer each time it re-encounters it. I'll also note that you don't technically need to add both the start and end positions of the kmer to the dictionary - you should know the end position already, since you know the value of k (and even if you didn't, you have the actual kmer sequence to reference as well).

### Completion:

Found:
Python script

Missing:
Output file
