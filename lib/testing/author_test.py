import pytest
from classes.many_to_many import Author
from classes.many_to_many import Article
from classes.many_to_many import Magazine

class TestAuthor:
    """Tests for the Author class"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_author_articles(self):
        """Author has many articles"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "Dating life in NYC")

        assert len(author_1.articles()) == 2
        assert article_1 in author_1.articles()
        assert article_2 in author_1.articles()

    def test_author_unique_articles(self):
        """Author's articles should be unique"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "How to wear a tutu with style")  # Same title

        # Expecting only one article due to title uniqueness
        assert len(author_1.articles()) == 1


