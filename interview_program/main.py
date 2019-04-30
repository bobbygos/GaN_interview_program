import fizzBuzzPlus

if __name__ == '__main__':
    fizzBuzz = fizzBuzzPlus.FizzBuzzPlus()
    for x in range(100):
        # Wanted to start at 1.
        num = x+1
        fizzBuzzFlag = False
        if fizzBuzz.multipleOfThree(num) or fizzBuzz.containsThree(num):
            # Default is /n. This waits for the endline until the end of the loop.
            print ("Fizz", end = '')
            fizzBuzzFlag = True
        if fizzBuzz.multipleOfFive(num) or fizzBuzz.containsFive(num):
            # Default is /n. This waits for the endline until the end of the loop.
            print ("Buzz", end = '')
            fizzBuzzFlag = True
        if fizzBuzzFlag:
            # Causes newline if a Fizz and/or Buzz was printed.
            print ("")
        else:
            # Print number if not Fizz and/or Buzz.
            print (num)