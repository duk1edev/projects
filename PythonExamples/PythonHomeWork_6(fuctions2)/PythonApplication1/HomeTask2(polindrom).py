#1
def check_polindrom(word):
    inver_word = word[::-1]
    if inver_word == word:
        print("{} - polindrom".format(word))
        print("(iver){} = {}".format(inver_word,word))
    else:
        print("{} - not polindrom".format(word))
#2
def check_polindrom_2(word):
    lenth = len(word)
    word_chars = list(word)
    rev_word = list(word)
    for i in range(lenth):
        rev_word[lenth - 1] = word_chars[i]
        lenth-=1
    if rev_word == word_chars:
        print("{} - polindrom".format(word_chars))
        print("(iver){} = {}".format(rev_word,word_chars))
    else:
        print("{} - not polindrom".format(word))

word = input("Enter the word : ")
check_polindrom_2(word)
check_polindrom(word)

