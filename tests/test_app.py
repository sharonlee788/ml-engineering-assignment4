import os
from app import build_filename

def test_build_filename():
    assert build_filename("kelly") == "kelly_output.txt"