from ngram import NGram

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
ngrams_result = list(range(test_size))

for i in range(test_size):
    max_similarity = 0
    similarity_dict = {}
    for item in my_dict:
        similarity = NGram.compare(misspell[i],item)
        similarity_dict[item] = similarity
        if similarity > max_similarity:
            max_similarity = similarity
    if max_similarity > 0:
        ngrams_result[i] = get_keys(similarity_dict, max_similarity)
    else:
        ngrams_result[i] = []
    print('Word Number:',i+1,'/',test_size)
    print('MISSPELL:',misspell[i],'\nN-GRAMS:',ngrams_result[i],'\nCORRECT:',correct[i],'\n--------------------------------')    
    total += len(ngrams_result[i])
    if correct[i] in ngrams_result[i]:
        match += 1

precision = match/total
recall = match/test_size
f_score = 2*precision*recall/(precision+recall)

print('Precision of N-GRAMS:',precision)
print('Recall of N-GRAMS:',recall)
print('F-score of N-GRAMS:',f_score)
