# How many ways can a word be misspelled if only upto 2 deletion, 2 substitution, 2 insertion allowed

Misspell file has "Mistakes" class which can be used get all possible error that can happen when writing a word.
Possible reasons of mistakes are 3.These are **deletion, substitution, insertion.**

This class gives wrong spelled word list by making following assumption:
- The limit of substitution and insertion of letters is 2. If more then 2 substitution in one call is made,  class will give "Limit Crossed" error.
- When dealing with double substitution, the letters change takes place together not separately. e.g. G##IL, GM##L.         
  Not  ~~G#A#L~~
- When dealing with double insertion, the letters insertion takes place together not separately. e.g. G##MAIL, GM##AIL.        
  Not  ~~G#MA#IL~~ 
- All three action "deletion", "substitution", "insertion" never take place together. This class deals with any two action at a time.

Example: Suppose the word here is "GMAIL". "GMAIL" constitue of four letters "g", "m", "a", "i", "l".
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
- instantiate with any variable and give values to parameter
- call method "error" to the instance of the class and store the value to print.

Follwing is the example if word is **"*bat*"** and allowed values to class parameters are ***n_del=1, n_sub=0, n_ins=0***:

```
word = Mistakes("bat", n_del=1, n_sub=0, n_ins=0)
error_word = word.error()

# printing the misspelled words
print(error_word)

# number of misspelled words
print(len(error_word))
```

**Output**
> ['ta', 'ab', 'tb', 'at', 'ba', 'bt']
  
> 6
