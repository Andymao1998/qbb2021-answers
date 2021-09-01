import sys # import system argument

#arg1 = sys.argv[1] # import system argument 1
#arg2 = sys.argv[2] # import system argument 2

fs = open(sys.argv[1], "r") # open a file
fly_dictionary = dict() # create an empty dictionary 
for line in fs: # loop through each line
    line_d = line.split() # split each line by space
    fly_dictionary[line_d[0]] = line_d[1].strip("/n") # store the gene ID as keys and the protein ID as values 

table = open(sys.argv[2] , 'r') # open the second file
data = [] # create an empty list 
for features in table: # loop through each line
    feature_r = features.split() # split by space
    if feature_r[8] in fly_dictionary.keys(): # look for a match between the gene ID in target file and query file 
        feature_r[8] = fly_dictionary[feature_r[8]] # if there is a match, substitute the gene ID with the Uniport ID
    elif len(sys.argv) == 4: # If there is a third argument, substitute the gene ID with the third argument (string)
        feature_r[8] = sys.argv[3]
    else:
        feature_r[8] = "N/A" # If a third argument doesn't exist, put "N/A"
    data.append(feature_r) # Collect this new list

data[0][8] = "Uniport ID" # Change the name of the header

for gg in data: # join each element of the list with Tab to align the data better for visualization
    print("\t".join(gg))
