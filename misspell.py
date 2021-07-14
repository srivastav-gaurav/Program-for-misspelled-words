from itertools import permutations
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

    # letters choosen one at a time
    perm_1 = permutations(alpha, 1)
    one_letter = ["".join(i) for i in perm_1]

    # letters choosen two at a time
    perm_2 = permutations(alpha, 2)
    two_letter = ["".join(i) for i in perm_2]


    def __init__(self, word, n_ins=0, n_del=0, n_sub=0):

        self.word = word.lower()
        self.n_ins = n_ins
        self.n_del = n_del
        self.n_sub = n_sub
        self.alpha = string.ascii_lowercase
        self.nLetters = len(word)

    def error(self):

        """ One stage for all solution """

        if self.n_del == self.n_sub == self.n_ins == 0:
            return "No error"

        elif self.n_del in (1,2) and self.n_sub == 0 and self.n_ins == 0:
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).deletion()

        elif self.n_del == 0 and self.n_sub in (1,2) and self.n_ins == 0:
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).substitution()

        elif self.n_del == 0 and self.n_sub == 0 and self.n_ins in (1,2):
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).insertion()

        elif self.n_del in (1,2) and self.n_sub in (1,2) and self.n_ins == 0:
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).del_sub()

        elif self.n_del in (1,2) and self.n_sub == 0 and self.n_ins in (2,2):
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).del_ins()

        elif self.n_del == 0 and self.n_sub in (1,2) and self.n_ins in (1,2):
            return Mistakes(self.word, n_del = self.n_del, n_sub = self.n_sub, n_ins = self.n_ins).sub_ins()

        else:
            return "Limit Crossed"



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
            return word[0:i] + letters + word[i+j:]
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
        # 1 deletion, 0 substitution, 0 insertion
        if self.n_del == 1:
            mistakes1 = permutations(self.word, self.nLetters-1)
            mD1 = ["".join(i) for i in mistakes1]
            return Mistakes.cleaner(self.word, mD1)

        # 2 deletion , 0 substitution, 0 insertion
        elif self.n_del == 2:
            mistakes2 = permutations(self.word, self.nLetters-2)
            mD2 = ["".join(i) for i in mistakes2]
            return Mistakes.cleaner(self.word, mD2)



    def substitution(self):
        """   mistakes through substitution   """

        # 1 substitution, 0 insertion and 0 deletion
        if self.n_sub == 1 and self.n_ins == 0:
            sub_1 = list()
            for i in range(len(self.word)):
                sub_1 = sub_1  + ["".join(Mistakes.substitute(self.word, i, 1, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, sub_1)

        # 2 substitution, 0 insertion and 0 deletion
        elif self.n_sub == 2 and self.n_ins == 0:
            sub_2 = list()
            for i in range(len(self.word)):
                sub_2 = sub_2 + ["".join(Mistakes.substitute(self.word, i, 2, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, sub_2)



    def insertion(self):
        """   mistakes through insertion   """

        # 1 insertion
        if self.n_ins == 1:
            ins_1 = list()
            for i in range(len(self.word)):
                ins_1 = ins_1 + ["".join(Mistakes.insert(self.word, i, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, ins_1)

        # 2 insertion
        elif self.n_ins == 2:
            ins_2 = list()
            for i in range(len(self.word)):
                ins_2 = ins_2 + ["".join(Mistakes.insert(self.word, i, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, ins_2)



    def sub_ins(self):
        """   mistakes through both substitution and insertion   """

        # 1 substitution and 1 insertion
        if self.n_sub == 1 and self.n_ins == 1:
            sub1_ins1 = list()
            sub_1 = Mistakes(self.word, n_sub = self.n_sub).substitution()
            for changed_word in sub_1:
                for i in range(len(changed_word)):
                    sub1_ins1 = sub1_ins1 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.one_letter]
                # break
            return Mistakes.cleaner(self.word, sub1_ins1)

        # 1 substitution and 2 insertion
        if self.n_sub == 1 and self.n_ins == 2:
            sub1_ins2 = list()
            sub_1 = Mistakes(self.word, n_sub = self.n_sub).substitution()
            for changed_word in sub_1:
                for i in range(len(changed_word)):
                    sub1_ins2 = sub1_ins2 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.two_letter]
                # break
            return Mistakes.cleaner(self.word, sub1_ins2)


        # 2 substitution and 1 insertion
        if self.n_sub == 2 and self.n_ins == 1:
            sub2_ins1 = list()
            sub_2 = Mistakes(self.word, n_sub = self.n_sub).substitution()
            for changed_word in sub_2:
                for i in range(len(changed_word)):
                    sub2_ins1 = sub2_ins1 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.one_letter]
                # break
            return Mistakes.cleaner(self.word, sub2_ins1)

        # 2 substitution and 2 insertion
        if self.n_sub == 2 and self.n_ins == 2:
            sub2_ins2 = list()
            sub_2 = Mistakes(self.word, n_sub = self.n_sub).substitution()
            for changed_word in sub_2:
                for i in range(len(changed_word)):
                    sub2_ins2 = sub2_ins2 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.two_letter]
                break
            return Mistakes.cleaner(self.word, sub2_ins2)



    def del_sub(self):
        """ mistakes through both deletion and substitution   """

        # 1 deletion and 1 substitution
        if self.n_del == 1 and self.n_sub == 1:
            del1_sub1 = list()
            D1 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D1:
                for i in range(len(changed_word)):
                    del1_sub1 = del1_sub1 + ["".join(Mistakes.substitute(changed_word, i, 1, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, del1_sub1)

        # 1 deletion and 2 substitution
        if self.n_del == 1 and self.n_sub ==2:
            del1_sub2 = list()
            D1 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D1:
                for i in range(len(changed_word)):
                    del1_sub2 = del1_sub2 + ["".join(Mistakes.substitute(changed_word, i, 2, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, del1_sub2)


        # 2 deletion and 1 substitution
        if self.n_del == 2 and self.n_sub == 1:
            del2_sub1 = list()
            D2 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D2:
                for i in range(len(changed_word)):
                    del2_sub1 = del2_sub1 + ["".join(Mistakes.substitute(changed_word, i, 1, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, del2_sub1)

        # 2 deletion and 2 substitution
        if self.n_del == 2 and self.n_sub ==2:
            del2_sub2 = list()
            D2 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D2:
                for i in range(len(changed_word)):
                    del2_sub2 = del2_sub2 + ["".join(Mistakes.substitute(changed_word, i, 2, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, del2_sub2)



    def del_ins(self):
        """   mistakes through both deletion and insertion   """

        # 1 deletion and 1 insertion
        if self.n_del == 1 and self.n_ins == 1:
            del1_ins1 = list()
            D1 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D1:
                for i in range(len(changed_word)):
                    del1_ins1 = del1_ins1 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, del1_ins1)

        # 1 deletion and 2 insertion
        if self.n_del == 1 and self.n_ins ==2:
            del1_ins2 = list()
            D1 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D1:
                for i in range(len(changed_word)):
                    del1_ins2 = del1_ins2 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, del1_ins2)


        # 2 deletion and 1 insertion
        if self.n_del == 2 and self.n_ins == 1:
            del2_ins1 = list()
            D2 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D2:
                for i in range(len(changed_word)):
                    del2_ins1 = del2_ins1 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.one_letter]
            return Mistakes.cleaner(self.word, del2_ins1)

        # 2 deletion and 2 insertion
        if self.n_del == 2 and self.n_ins ==2:
            del2_ins2 = list()
            D2 = Mistakes(self.word, n_del=self.n_del).deletion()

            for changed_word in D2:
                for i in range(len(changed_word)):
                    del2_ins2 = del2_ins2 + ["".join(Mistakes.insert(changed_word, i, letters, True)) for letters in Mistakes.two_letter]
            return Mistakes.cleaner(self.word, del2_ins2)





a = Mistakes("bat", n_del=1, n_sub=1, n_ins=0)

print(a.error())
print(len(a.error()))

# OUTPUT : ['bw', 'jb', 'ib', 'ak', 'bo', 'bs', 'ba', 'tm', 'zt', 'bz', 'tc', 'tl', 'mb', 'ga', 'bm', 'th', 'bb', 'lt', 'as', 'db', 'bq', 'tz', 'am', 'tg', 'te', 'al', 'ai', 'gt', 'bl', 'bu', 'bg', 'qb', 'ka', 'hb', 'dt', 'rb', 'ab', 'ae', 'ht', 'yt', 'za', 'at', 'ta', 'tk', 'ah', 'bc', 'qa', 'bv', 'tw', 'yb', 'ap', 'bd', 'xa', 'aw', 'nt', 'cb', 'xt', 'mt', 'tb', 'td', 'tp', 'oa', 'fa', 'kb', 'et', 'aq', 'ty', 'pa', 'va', 'bt', 'tt', 'bn', 'tn', 'jt', 'vb', 'ra', 'na', 'wt', 'az', 'tr', 'fb', 'ca', 'ts', 'it', 'tv', 'aa', 'zb', 'vt', 'ha', 'qt', 'ut', 'tq', 'xb', 'ct', 'ot', 'bi', 'aj', 'by', 'wb', 'ac', 'pb', 'ay', 'bp', 'ax', 'ft', 'ao', 'ti', 'be', 'bh', 'ea', 'tx', 'af', 'gb', 'br', 'an', 'wa', 'da', 'st', 'ad', 'tj', 'pt', 'tf', 'ya', 'rt', 'bk', 'bj', 'ub', 'lb', 'bx', 'bf', 'tu', 'sa', 'to', 'ar', 'au', 'sb', 'ma', 'eb', 'nb', 'av', 'ua', 'la', 'ia', 'ag', 'ja', 'kt', 'ob']

# len: 147
