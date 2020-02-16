# High Performance FizzBuzz
FizzBuzz is a common developer interview question for novice developers. The rules are simple - for every number between 1 to 100 do the following:
* If the number is divisible by 3, print "Fizz"
* If the number is divisible by 5, print "Buzz"
* If the number is divisible by both 3 and 5, print "FizzBuzz"
* If the number doesn't meet any of the above criteria - simply print the number. 

For just about 99% of you, this sounds super simple (as it should be). However, I was curious, how can we make it run as fast as posible, using high performance python optimizations, and after many experimentation, I came up with the following in Python, the language I have been using the most profesionally.This can serve as a simple introduction to high performance programming, because for many of us - a millisecond can make all the difference in the world. 

## Running Fastest Fizzbuzz
For now, to run the fastest FizzBuzz, just run it like a normal python script
```
python fastestfizzbuzz.py
```
To adjust the number of iterations, as well as turning printing off and on - you will have to adjust/comment the appropriate values in the code.

## Notes
1. The biggest time saver was with string processing. Instead of constantly printing or appending strings, we create an array of strings, join it with a newline and print it at the very end of the function call.
2. Redefining functions like `functional_append = array_to_convert.append` and `functional_str = str` places them in the local function scope. When python interprets a function - it searches first in the local scope, then the file, all the way up to imported and system functions. Seeing the function in the local scope speeds up our operation, especially if its performed repeatedly.
3. The `print(to_return)` line should be commented out if you want to test with larger numbers of iteration. With string console printing, the improvements will be hardly noticable and "random" depending in string processing.


### TODO
* provide command line arguments to set iteration number and printing option
* provide refernence and explanation to more "speed tricks" and why some, like mapping arrays, etc, were not used here.
* create similar projects in other languages. 
* try to make this darn thing even faster
