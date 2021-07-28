from itertools import combinations, product
import string

class Mistakes:
    """
Mistakes class return all the possible error can happen when writing a word. Possible reasons of mistakes 3 things.
These are deletion, substitution, insertion.

    |This class gives wronged spell words list by making following assumption:
    |* The limit of substitution and insertion of letters is 2. More then 2 substitution in one call of the class give "Limit Crossed" error.
    |* When dealing with double substitution, the letters change takes place together not separately. e.g. G##IL, GM##L.
    |* When dealing with double insertion, the letters insertion takes place together not separately. e.g. G##MAIL, GM##AIL.
    |* All three action "deletion", "substitution", "insertion" never take place together. This class deals with any two action at a time.

Example: Suppose the word here is "GMAIL". "GMAIL" constitue of four letters "g", "m", "a", "i", "l".
Possible mistakes as we previously said through --

     ```````````` Deletion ````````````
    (1)  "MAIL", "GAIL", "GMIL", "GMAL", "GMAI"
    (2)  "AIL", "GIL", "GML", "GMA"

    `````````` Substitution ``````````
    (1)  "AMAIL", "BMAIL", "CMAIL", "DMAIL", .....
    (2)  "AAAIL", "ABAIL", "ACAIL", "ADAIL", .....

    ``````````` Insertion ````````````
    (1)  "AGMAIL", "GAMAIL", "GMAAIL", "GMAIAL", "GMAILA", "BGMAIL", "GBMAIL", ....
    (2)  "AAGMAIL", "GAAMAIL", "GMAAAIL", "GMAIAAL", ....
    """


     # alphabet letters
    alpha = string.ascii_lowercase

    def __init__(self, word, n_ins=0, n_del=0, n_sub=0, length = "N"):

        self.word = word.lower()
        self.n_ins = n_ins
        self.n_del = n_del
        self.n_sub = n_sub
        self.length = length.upper()

    @staticmethod
    def arsenal(num):
        letters = ["".join(i) for i in product(Mistakes.alpha, repeat = num)]
        return letters


    @staticmethod
    def insert(word, i, letters, continuous=True):
        """ returns word with letters inserted on a given index (i) """
        if continuous is True:
            return word[:i] + letters + word[i:]
        else:
            pass


    @staticmethod
    def substitute(word, i, j, letters, continuous=True):
        """ returns word with letters substituted on a given index (i) """
        if continuous is True:
            new_word = word[0:i] + letters + word[i+j:]
            if len(new_word) <= len(word):
                return new_word
        else:
            pass


    @staticmethod
    def cleaner(word, obj):
        """ takes care of repeated word in the list and also removes the original word because that is a right spelled word in a list for misspelled words """
        obj = list(set(obj))
        try:
            obj.remove(word)
            return obj
        except:
            return obj



    def deletion(self):
        """   mistakes by deletions   """

        mistakes = combinations(self.word, len(self.word)-self.n_del)
        wrong_words = ["".join(i) for i in mistakes]

        return Mistakes.cleaner(self.word, wrong_words)



    def substitution(self):
        """   mistakes through substitution   """

        arsenal = Mistakes.arsenal(num=self.n_sub)
        wrong_words = list()

        for i in range(len(self.word)):
            wrong_words = wrong_words  + [Mistakes.substitute(self.word, i, self.n_sub, letters, True) for letters in arsenal]

        return Mistakes.cleaner(self.word, wrong_words)


    def insertion(self):
        """   mistakes through insertion   """

        arsenal= Mistakes.arsenal(num=self.n_ins)
        wrong_words = list()

        for i in range(len(self.word)+1):
            wrong_words = wrong_words + [Mistakes.insert(self.word, i, letters, True) for letters in arsenal]

        return Mistakes.cleaner(self.word, wrong_words)



    def error(self):
        """   one stop for everything.  """

#         deletion
        if self.n_del > 0:
            del_words = Mistakes(self.word, n_del=self.n_del).deletion()

        else:
            del_words = [self.word]

#         substitution
        if self.n_sub>0:
            sub_words = list()
            for changed_word in del_words:
                if changed_word is not None:
                    sub_words = sub_words + Mistakes(changed_word, n_sub = self.n_sub).substitution()

        else:
            sub_words = del_words

#         insertion
        if self.n_ins > 0:
            wrong_words = list()
            for changed_word in sub_words:
                if changed_word is not None:
                    wrong_words = wrong_words + Mistakes(changed_word, n_ins=self.n_ins).insertion()

        else:
            wrong_words = sub_words

        wrong_words = Mistakes.cleaner(self.word, wrong_words)

        if self.length == "Y":
            return f"{wrong_words}; Number of words: {len(wrong_words)}"
        else:
            return wrong_words



def main():

    """ taking inputs """

    word = input("Give a word with alphabets only: ")
    while word.isalpha() is False:
        word = input("Give a word with alphabets only: ")

    dell = input("Give a whole number for number of deletion: ")
    while (dell).isnumeric() is False:
        dell = input("Give a whole number for number of deletion: ")

    sub = input("Give a whole number for number of substitution: ")
    while (sub).isnumeric() is False:
        sub = input("Give a whole number for number of substitution: ")

    ins = input("Give a whole number for number of insertion: ")
    while (ins).isnumeric() is False:
        ins = input("Give a whole number for number of insertion: ")
    print("\n")

    len_words = input(" 'Y' , if you want count the of words or, 'N' for not: ")
    while len_words not in ("Y", "y", "N", "n"):
        len_words = input(" 'Y' , if you want the count of words or, 'N' for not: ")

    print("\n")

    print(f"Listing misspell words from word: '{word}'; number_of_deletion: '{dell}'; number_of_substitution: '{sub}'; \
number_of_insertion: '{ins}'", "\n","\n")

    error_words = Mistakes(word=word, n_del=int(dell), n_sub=int(sub), n_ins=int(ins), length = len_words).error()
    print(error_words)

if __name__ == "__main__":
    main()


