import pytest
from string_utils import StringUtils


class TestStringUtils:
    def setup_method(self):
        self.utils = StringUtils()

    def test_capitalize_positive(self):
        assert self.utils.capitalize("skypro") == "Skypro"
        assert self.utils.capitalize("тест") == "Тест"
        assert self.utils.capitalize("123abc") == "123abc"
        assert self.utils.capitalize("hello world") == "Hello world"

    def test_capitalize_negative(self):
        assert self.utils.capitalize("") == ""
        assert self.utils.capitalize(" ") == " "
        assert self.utils.capitalize("Python") == "Python"
        assert self.utils.capitalize("1test") == "1test"
        with pytest.raises(AttributeError):
            self.utils.capitalize(None)

    def test_trim_positive(self):
        assert self.utils.trim("   skypro") == "skypro"
        assert self.utils.trim("тест  ") == "тест  "
        assert self.utils.trim("123") == "123"
        assert self.utils.trim("hello   world") == "hello   world"

    def test_trim_negative(self):
        assert self.utils.trim("") == ""
        assert self.utils.trim(" ") == ""
        assert self.utils.trim("   ") == ""
        assert self.utils.trim("\t skypro") == "\t skypro"
        with pytest.raises((AttributeError, TypeError)):
            self.utils.trim(None)

    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True
        assert self.utils.contains("тест", "т") is True
        assert self.utils.contains("123", "2") is True
        assert self.utils.contains("hello world", " ") is True

    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") is False
        assert self.utils.contains("", "a") is False
        assert self.utils.contains(" ", "x") is False
        assert self.utils.contains("123", "a") is False
        with pytest.raises((AttributeError, TypeError)):
            self.utils.contains(None, "a")
        with pytest.raises((AttributeError, TypeError)):
            self.utils.contains("test", None)

    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert self.utils.delete_symbol("тест", "т") == "ес"
        assert self.utils.delete_symbol("hello world", "l") == "heo word"

    def test_delete_symbol_negative(self):
        assert self.utils.delete_symbol("SkyPro", "U") == "SkyPro"
        assert self.utils.delete_symbol("", "a") == ""
        assert self.utils.delete_symbol(" ", " ") == ""
        assert self.utils.delete_symbol("123", "a") == "123"
        with pytest.raises((AttributeError, TypeError)):
            self.utils.delete_symbol(None, "a")
        with pytest.raises((AttributeError, TypeError)):
            self.utils.delete_symbol("test", None)
