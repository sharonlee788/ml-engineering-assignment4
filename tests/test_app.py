"""
Run the tests
"""
from app import build_filename

def test_build_filename():
    """ Simple test"""
    assert build_filename("kelly") == "kelly_output.txt"

#