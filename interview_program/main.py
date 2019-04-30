import fizzBuzzPlus

if __name__ == '__main__':
    fizzBuzz = fizzBuzzPlus.FizzBuzzPlus()
    for x in range(100):
        num = x+1
        fizzBuzzFlag = False
        if fizzBuzz.multipleOfThree(num) or fizzBuzz.containsThree(num):
            print ("Fizz", end = '')
            fizzBuzzFlag = True
        if fizzBuzz.multipleOfFive(num) or fizzBuzz.containsFive(num):
            print ("Buzz", end = '')
            fizzBuzzFlag = True
        if fizzBuzzFlag:
            print ("")
        else:
            print (num)