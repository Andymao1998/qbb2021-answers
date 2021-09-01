import sys 

arg1 = sys.argv[1]
arg2 = sys.argv[2]

fs = open(sys.argv[1], "r")
fly_dictionary = dict()
for line in fs:
    line_d = line.split()
    fly_dictionary[line_d[0]] = line_d[1]

table = open(sys.argv[2] , 'r')
data = []
for features in list(table):
    feature_r = features.split()
    if feature_r[8] in fly_dictionary.keys():
        feature_r[8] = fly_dictionary[feature_r[8]]
    else:
        if len(sys.argv) == 4:
            feature_r[8] = sys.argv[3]
        else:
            feature_r[8] = "N/A"
    data.append(feature_r)

data[0][8] = "Uniport ID"

for gg in data:
    print("\t".join(gg))