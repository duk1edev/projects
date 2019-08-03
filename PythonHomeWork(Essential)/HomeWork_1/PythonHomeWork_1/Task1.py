import copy
class Book(object):
    def __init__(self, title, author,year,genre):
        self.title = title
        self.author = author
        self.publication_year = year
        self.genre = genre

    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return self.author == other.author and \
            self.title == other.title and \
            self.publication_year == other.publication_year and \
            self.genre == other.genre


    def __as_string(self,format_string):
        return format_string.format(
            self.author,
            self.title,
            self.publication_year,
            self.genre
        )

    def __str__(self):
        return self.__as_string('"{1}" by {0} (published in {2}), genre : {3}')
    
    def __repr__(self):
        return self.__as_string("Book({0!r},{1!r},{2!r},{3!r})")

def main():
    orwell1984 = Book('1984',"George Orwell",1949,'asafssidsidguisdgbsuidfgdsgdfg')
    orwell1984_2 = copy.copy(orwell1984)
    source = Book("Source","Ayn Raid","1947","seflmaking")


    print(orwell1984)
    print(orwell1984_2)
    print(source)

    print(repr(orwell1984))
    print(repr(source))

    print(orwell1984 == orwell1984_2)
    print(orwell1984 != orwell1984_2)
    print(orwell1984 == source)
    print(orwell1984 != source)

if __name__ == '__main__':
    main()
