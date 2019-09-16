### COMP90049 Project1 Lexical Normalization Based on Tweets
This is the Project 1 for COMP90049 (Knowledge Technologies) from the University of Melbourne.

This project implements a misspelling correction system for lexical normalisation task based on three different approximate string matching algorithms in Python, including Global Edit Distance, N-grams and Soundex. For more details, please check the [project report](https://github.com/Andy-TK/COMP90049_Project1_Lexical_Normalization_Based_on_Tweets/blob/master/COMP90049%20Project%201%20Report.pdf).

#### Python Library Sources:
* Global Edit Distance
Library: python-Levenshtein 0.12.0
Author: Antti Haapala
URL: https://github.com/ztane/python-Levenshtein

* N-grams
Library: ngram 3.3.2
Author: Graham Poulter
URL: https://github.com/gpoulter/python-ngram

* Soundex
Library: jellyfish 0.7.1
Author: James Turk
URL: https://github.com/jamesturk/jellyfish

#### How does the program work?
The dataset contains three text file: `misspell.txt`,`dict.txt` and `correct.txt`.
Some functions are defined in the code:
* `get_filelist(filename)`: transfer the text file into a string list of lexical tokens.

* `get_keys(d, value)`: return tokens with specific values (minimum distance or maximum similarity).

* `code_compare(s1, s2)`: calculate the distance between two Soundex code.

The variables `match` and `total` are used to store the number of correct tokens retrieved and the total number of retrieved tokens respectively. The variable `test_size` corresponds to the total number of misspell tokens as well as the correct tokens among the dataset.

For each token in misspell list, find the distance or similarity between itself and each word from the dictionary and record the minimum distance or the maximum similarity. Then using `get_keys(d, value)` function to retrieve the corresponding candidate tokens with the minimum distance or the maximum similarity from the dictionary and store the returned words into a result list. Note that for N-grams, if the maximum similarity is 0, then return an empty list instead of the entire dictionary. Also, for Soundex, check whether the misspell token is made up of pure alphabets, and if not, just return an empty list. Calculate the length of the result list and adds it up to the variable `total`. Check if the result list contains the corresponding correct token, and if it does, adds 1 to the variable `match`.

After looping the whole misspell corpus, count the number of correct tokens retrieved and the total number of retrieved tokens and calculate the values of Precision, Recall and F-score:

`precision = match/total`

`recall = match/test_size`

`f_score = 2*precision*recall/(precision+recall)`
