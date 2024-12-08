import pytest
from classes.many_to_many import Magazine
from classes.many_to_many import Article
from classes.many_to_many import Author

class TestMagazine:
    """Tests for the Magazine class"""

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16

        # Invalid name check
        with pytest.raises(ValueError):
            magazine_1.name = "New Yorker Plus X"  # This should raise an exception

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        magazine_1.category = "Lifestyle"
        assert magazine_1.category == "Lifestyle"

        # Invalid category check
        with pytest.raises(ValueError):
            magazine_2.category = 2  # This should raise an exception

    def test_category_len(self):
        """magazine category should not be empty"""
        magazine_1 = Magazine("Vogue", "Fashion")

        assert magazine_1.category != ""

        # Test invalid empty category
        with pytest.raises(ValueError):
            magazine_1.category = ""  # This should raise an exception
