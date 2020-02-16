# High Performance FizzBuzz
FizzBuzz is a common developer interview question for novice developers. The rules are simple - for every number between 1 to 100 do the following:
* If the number is divisible by 3, print "Fizz"
* If the number is divisible by 5, print "Buzz"
* If the number is divisible by both 3 and 5, print "FizzBuzz"
* If the number doesn't meet any of the above criteria - simply print the number. 

For just about 99% of you, this sounds super simple (as it should be). However, I was curious, how can we make it run as fast as posible, using high performance python optimizations, and after many experimentation, I came up with the following in Python, the language I have been using the most profesionally.This can serve as a simple introduction to high performance programming, because for many of us - a millisecond can make all the difference in the world. 

## Running Fastest Fizzbuzz
To run Fastest FizzBuzz - run it from your favorite command line utility:
```
python fizzbuzz.py [-n <numberofruns>] [-q]
```
-n <numberofruns> - optional positive integer value - the amount of times to run the fizbuzz command. Defaults to 1
-q - Flag to run the fizzbuzz function in quiet mode (Without the output as described above) - used to test speed differences that would be hard to measure with string display, etc.

## Notes
1. The biggest time saver was with string processing. Instead of constantly printing or appending strings, we create an array of strings, join it with a newline and print it at the very end of the function call.
2. Redefining functions like `functional_append = array_to_convert.append` and `functional_str = str` places them in the local function scope. When python interprets a function - it searches first in the local scope, then the file, all the way up to imported and system functions. Seeing the function in the local scope speeds up our operation, especially if its performed repeatedly.
3. The optional `-q` should be set if you want to test with larger numbers of iterations. With string console printing, the improvements will be hardly noticable and "random" depending in string processing.


### TODO
* provide refernence and explanation to more "speed tricks" and why some, like mapping arrays, etc, were not used here.
* create similar projects in other languages. 
* try to make this darn thing even faster
