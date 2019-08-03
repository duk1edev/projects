class Book(object):
    def __init__(self, author, title,year,genre,comments=[]):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.comments = comments
    
    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return self.author == other.author and \
            self.title == other.title and \
            self.year == other.year and \
            self.genre == other.genre 
    
    def __as_string(self,format_string):
        return format_string.format(
            self.author,
            self.title,
            self.year,
            self.genre,
            self.comments
            )

    def __str__(self):
        book = self.__as_string('"{1}" by {0} (published in {3} year, genre: {4})'
                                ' \nComments: \n')
        comments = '\n'.join(map(str,self.comments)) or 'No comments.'
        return book + comments
    def __repr__(self):
        return self.__as_string("Book({0!r}, {1!r}, {2!r}, {3!r})")
                
class Comment(object):
    def __init__(self,mark,text):
        self.mark = mark
        self.text = text

    def __repr__(self):
        return 'Comment({!r}, {!r})'.format(self.mark,self.text)
    def __str__(self):
        return 'Mark: {} \nReview: {}'.format(self.mark,self.text)

def main():
    book1 = Book("Ayn Raid", "Atlant","1949","selfmaking")
    book2 = Book("Saveilev","Statistics and cats","2015","tutorial" )

    book1.comments = [
        Comment(5,'Awesome book, changed my perception of the life'),
        Comment(4,"Not bad, but Huxley's scenario seems more realistic to me"),
        ]

    print(book1)
    print()
    print(book2)
    print()
    print(repr(book1))
    print(repr(book2))

if __name__ == '__main__':
    main()
