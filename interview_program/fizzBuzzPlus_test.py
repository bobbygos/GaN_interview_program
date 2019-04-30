import fizzBuzzPlus

def test_three_is_mutiple_of_three():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.multipleOfThree(3)
    
def test_four_is_not_multiple_of_three():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.multipleOfThree(4) == False

def test_thirteen_contains_three():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.containsThree(13)

def test_fourteen_does_not_contain_three():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.containsThree(14)
