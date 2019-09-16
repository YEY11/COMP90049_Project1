from jellyfish import soundex

def get_filelist(filename):
    with open(filename) as original_file:
        return original_file.read().splitlines()

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def code_compare(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

my_dict = get_filelist("dict.txt")
misspell = get_filelist("misspell.txt")
correct = get_filelist("correct.txt")

match = 0
total = 0
test_size = len(misspell)
soundex_result = list(range(test_size))

for i in range(test_size):
    if misspell[i].isalpha():
        s1 = soundex(misspell[i])
        min_distance = code_compare(s1, soundex(my_dict[0]))
        distance_dict = {}
        for item in my_dict:
            s2 = soundex(item)
            distance = code_compare(s1, s2)
            distance_dict[item] = distance
            if distance < min_distance:
                min_distance = distance
        soundex_result[i] = get_keys(distance_dict, min_distance)
    else:
        soundex_result[i] = []
    print('Word Number:',i+1,'/',test_size)
    print('MISSPELL:',misspell[i],'\nSOUNDEX:',soundex_result[i],'\nCORRECT:',correct[i],'\n--------------------------------')    
    total += len(soundex_result[i])
    if correct[i] in soundex_result[i]:
        match += 1

precision = match/total
recall = match/test_size
f_score = 2*precision*recall/(precision+recall)

print('Precision of SOUNDEX:',precision)
print('Recall of SOUNDEX:',recall)
print('F-score of SOUNDEX:',f_score)





