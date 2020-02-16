import time


def fizzBuzzFastest():
    """
    The following function is FizzBuzz optimized for speed in python.
    Various designs, patterns, ways of looping, ways of comparission, etc, were tested, and the following is the
    best performing FizzBuzz I was able to achieve (for now)
    After relevant sections of the code - I will comment below it to explain why I took this step
    Enjoy!
    --- Serge
    """
    array_to_convert = []
    # The largest speed improvement was made thanks to smarter memory allocation when creating and displaying strings
    # It is faster over time to print one large string than several smaller ones
    # Prints and string concatenations  are very costly operations, so we limit them
    # We will fill an array of strings and print its contents later
    functional_append = array_to_convert.append
    functional_str = str
    # The two lines above declare the list append and string conversion functions, respectively, in the local scope
    # It is faster than calling these functions "natively" in the loop below
    # Python looks for functions first in its local context, then in the global context, then in the system context
    # So by declaring these built in functions in the  local scope we save time
    for running_counter in range(1, 101):
        # After trying a while loop with counters, a map on array_to_convert to a function that performs the actions
        # below - a for loop was still my best possible outcome
        if not running_counter % 5:
            if not running_counter % 3:
                functional_append("FizzBuzz")
            else:
                functional_append('Buzz')

        elif not running_counter % 3:
            # Same as above. Divisions by 3 occur more than divisions by 3 - so when given the chance, we should search
            # for a 3 first because it occurs more often
            functional_append('Fizz')
        else:
            functional_append(functional_str(running_counter))
            # Here we get our look at the string conversion. Just like appends - this saves time by having string
            # Conversion stored in the localscope
    to_return = "\n".join(array_to_convert)
    # We build our string from our array of strings. Due to memory allocation in python, this saves us the most time

    # There is a certain speed threshhold that can be achieved if we choose to display a result over x iterations
    # Printing to the console is a taxing function, and it is hard to see speed improvements after a certain point
    # To truly optimize the function, comment the print statement below and run more iterations
    print(to_return)


print("About to run my fastest FizzBuzz")
start = time.time()
# Adjust the counter in the range below to truly push this function
for i in range(100):
    fizzBuzzFastest()
end = time.time()
diff = end - start
print("Took us " + str(diff))
print("Finished FizzBuzz")
