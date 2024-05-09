class Author:
    def __init__(self, name:str):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "name"):
            print("Name can not be changed")
        elif type(value) != str:
            print("Name must be of type string")
        elif len(value) <= 0:
            print("Name must be longer than 0 characters")
        else:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)

    def topic_areas(self):
        topics_list = list({magazine.category for magazine in self.magazines()})
        if len(topics_list) > 0:
            return topics_list
        else:
            return None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    def article_titles(self):
        list_of_titles = [article.title for article in Article.all if article.magazine == self]
        return None if list_of_titles == [] else list_of_titles
    
    def contributing_authors(self):
        list_of_authors = [article.author for article in Article.all if article.magazine == self]
        new_list = list(set([author for author in list_of_authors if list_of_authors.count(author) >= 2]))
        return None if new_list == [] else new_list

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            print("Name must be of type string")
        elif len(value) < 2 or len(value) > 16:
            print("Category must be between 2 and 16 characters long")
        else:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) != str:
            print("Category must be of type string")
        elif len(value) <= 0:
            print("Category must be greater than 0 characters")
        else:
            self._category = value   



class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if type(value) == str and len(value) >= 5 and len(value) <= 50:
            self._title = value