class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        # Add the article to the author's list of articles
        self.author.add_article(self)
        # Add the article to the magazine's list of articles
        self.magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Article title cannot be empty.")
        self._title = value


