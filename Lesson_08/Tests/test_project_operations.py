"""Tests for project operations."""
import pytest
import time
from yougile_client import YougileClient, BASE_URL, API_KEY


class TestProjectOperations:
    """Tests for project operations - positive and negative scenarios."""

    # Тестовые данные
    VALID_PROJECT_TITLE = "Валидный проект"
    EMPTY_TITLE = ""
    VERY_LONG_TITLE = "X" * 1000
    INVALID_PROJECT_ID = "00000000-0000-0000-0000-000000000000"
    MALFORMED_PROJECT_ID = "invalid-id-format"

    @pytest.fixture
    def client(self):
        """Create client with API key."""
        client = YougileClient(base_url=BASE_URL)
        return client

    # ... остальные тесты остаются без изменений ...
    # (убраны константы BASE_URL и API_KEY из класса)