import Levenshtein

def get_filelist(filename):
    with open(filename) as original_file:
        return original_file.read().splitlines()

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

my_dict = get_filelist("dict.txt")
misspell = get_filelist("misspell.txt")
correct = get_filelist("correct.txt")

match = 0
total = 0
test_size = len(misspell)
ged_result = list(range(test_size))

for i in range(test_size):  
    min_distance = Levenshtein.distance(misspell[i], my_dict[0])
    distance_dict = {}
    for item in my_dict:
        distance = Levenshtein.distance(misspell[i], item)
        distance_dict[item] = distance
        if distance < min_distance:
            min_distance = distance
    ged_result[i] = get_keys(distance_dict, min_distance)
    print('Word Number:',i+1,'/',test_size)
    print('MISSPELL:',misspell[i],'\nGED:',ged_result[i],'\nCORRECT:',correct[i],'\n--------------------------------')    
    total += len(ged_result[i])
    if correct[i] in ged_result[i]:
        match += 1

precision = match/total
recall = match/test_size
f_score = 2*precision*recall/(precision+recall)

print('Precision of GED:',precision)
print('Recall of GED:',recall)
print('F-score of GED:',f_score)
