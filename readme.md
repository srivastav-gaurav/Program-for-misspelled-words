# How many ways can a word be misspelled if only upto 2 deletion, 2 substitution, 2 insertion allowed

Misspell file has "Mistakes" class which can be used to get all possible error that can happen when writing a word.
Possible reasons of mistakes are 3. These are **deletion, substitution, insertion.**

This class gives wrong spelled word list by making following assumption:
- The limit of substitution and insertion of alphabets is 2. If more then 2 substitution in one call is made,  class will give "Limit Crossed" error.
- When dealing with double substitution, the alphabets change takes place together not separately. e.g. G##IL, GM##L.         
  Not  ~~G#A#L~~
- When dealing with double insertion, the alphabets insertion takes place together not separately. e.g. G##MAIL, GM##AIL.        
  Not  ~~G#MA#IL~~ 
- All three action "deletion", "substitution", "insertion" never take place together. This class deals with any two action at a time.

Example: Suppose the word here is "GMAIL". "GMAIL" constitue of four alphabet "g", "m", "a", "i", "l".
Possible mistakes as we previously said are --

Deletion
1.  "MAIL", "GAIL", "GMIL", "GMAL", "GMAI"
2.  "AIL", "GIL", "GML", "GMA"

Substitution
1.  "AMAIL", "BMAIL", "CMAIL", "DMAIL", .....
2.  "AAAIL", "ABAIL", "ACAIL", "ADAIL", .....

Insertion
1.  "AGMAIL", "GAMAIL", "GMAAIL", "GMAIAL", "GMAILA", "BGMAIL", "GBMAIL", ....
2.  "AAGMAIL", "GAAMAIL", "GMAAAIL", "GMAIAAL", ....


## How to use misspell.py
- run misspell.py and fill the inputs

Follwing is the example if word is **"*bat*"** and allowed values to class parameters are ***n_del=1, n_sub=0, n_ins=0***:

```
Give a word with alphabets only:  bat
Give a whole number for number of deletion:  1
Give a whole number for number of substitution:  0
Give a whole number for number of insertion:  0



 'Y' , if you want count the of words or, 'N' for not:  n
```

**Output**
: Listing misspell words from word: 'bat'; number_of_deletion: '1'; number_of_substitution: '0'; number_of_insertion: '0' 

> ['ba', 'at', 'bt'];  Number of words: 3
