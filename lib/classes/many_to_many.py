class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  # A list to store articles written by the author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Author name cannot be empty.")
        self._name = value

    def add_article(self, article):
        """Add an article to the author's list if it's not already present."""
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        """Return a list of unique articles by title."""
        unique_articles = []
        for article in self._articles:
            if article.title not in [a.title for a in unique_articles]:
                unique_articles.append(article)
        return unique_articles


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # A list to store articles related to the magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if value == "":
            raise ValueError("Category cannot be empty.")
        self._category = value

    def add_article(self, article):
        """Add an article to the magazine's list."""
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        """Return a list of articles published in the magazine."""
        return self._articles


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
