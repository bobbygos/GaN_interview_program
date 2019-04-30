import fizzBuzzPlus
import pytest

@pytest.fixture(scope='session')
def setup():
    test = fizzBuzzPlus.FizzBuzzPlus()
    yield test
    
def test_three_is_mutiple_of_three(setup):
    test = setup
    assert test.multipleOfThree(3)
    
def test_four_is_not_multiple_of_three(setup):
    test = setup
    assert test.multipleOfThree(4) == False

def test_thirteen_contains_three(setup):
    test = setup
    assert test.containsThree(13)
    
def test_fourteen_does_not_contain_three(setup):
    test = setup
    assert test.containsThree(14) == False
