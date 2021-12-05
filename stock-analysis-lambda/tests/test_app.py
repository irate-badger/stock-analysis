from flask import app
import pytest
from src.app import welcome_


class TestApp:
    def test_welcome(self):
        assert welcome_() == "Example setup for the stock analysis"
