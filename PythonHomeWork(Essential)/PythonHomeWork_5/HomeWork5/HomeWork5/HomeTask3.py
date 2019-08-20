class WordSequence(list):
    """Класс для последовательности слов"""

    _delimiters  = ('.',',',':',';','- ',' -')

    def __init__(self,text):
        words = [word.casefold() for word in WordSequence._split(text)]
        for word in words:
            if word not in self:
                self.append(word)



    @staticmethod
    def _split(text):

        string  = text
        for delimiter in WordSequence._delimiters:
            string  = string.replace(delimiter,' ')
        return string.split()


def main():
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    Quam quidem, veniam dolor ipsum sapiente ullam mollitia molestias 
    repellendus nesciunt voluptas.'''

    words = WordSequence(text)

    for word in sorted(words):
        print(word)


if __name__ == '__main__':
    main()
