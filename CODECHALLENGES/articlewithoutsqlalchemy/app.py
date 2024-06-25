from article import Article
from author import Author
from magazine import Magazine

# exampl;e

author=Author("John Babptize")
mag=Magazine("Babylon Times","Bible Journal")
article=Article(author,mag,"The saviour is here")

mag2=Magazine("On the Boat","Ark Journal")
article=Article(author,mag2,"Noahs Ark")

print(vars(article))
print(author.articles)
print(author.name)
for article in author.articles:
    print(article.title)
    print(vars(article.magazine))
    print("")