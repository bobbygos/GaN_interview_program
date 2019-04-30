import fizzBuzzPlus

def test_mutiple_of_three_with_three():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.multipleOfThree(3)
    
def test_multiple_of_three_with_four():
    test = fizzBuzzPlus.FizzBuzzPlus()
    assert test.multipleOfThree(4) == False

