
# from author import Author
# from magazine import Magazine

class Article():

    def __init__(self,author,magazine,title):
        self._author = author
        self._magazine = magazine
        self._title=title

        author.add_article(self)
        author.add_magazine(magazine)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        ## Make all checks here
        self._title=value

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine

