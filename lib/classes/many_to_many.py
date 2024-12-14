class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str) or not (5<= len(title) <=50):
            raise ValueError("Title must be of type string or 5 to 50 chars long ")
        self._title = title
        Article.all.append(self)
    
    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if hasattr(self, "._title"):
            raise AttributeError("Title cannot be changed")
        

    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self,obj):
        if isinstance(obj,Author):
            self._author = obj

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,obj):
        if isinstance(obj,Magazine):
            self._magazine = obj

class Author:
    all =[]


    def __init__(self, name):
        if not isinstance(name,str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        Author.all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if hasattr(self, "._name"):
            raise AttributeError("Name cannot be changed")
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles() if article.magazine in Magazine.all]))

    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)    
        return new_article
    
    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([magazine.category for magazine in self.magazines() if self in magazine.contributors()]))

class Magazine:
    all=[]

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str) and (2 <= len(value) <= 16):
            self._name = value
    
    @property 
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if isinstance(value,str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles() if article.author in Author.all]))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return[article.title for article in self.articles()]            

    def contributing_authors(self): 
        authors = [author for author in self.contributors() if sum(1 for article in self.articles() if article.author == author) > 2] 
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
         if len(Article.all) == 0:
             return None
         return max(cls.all, key=lambda mag: len(mag.articles()))