'''
Sidewinder problem from While Loops Problem Set

What does this function do?
Takes a circuitous path through a list to find the "end".

What is the O() of the time complexity? Why?
O(n), assuming the lists aren't malformed (no loops or errors).
To find the end requires at most visiting each position in the
list, so even though the order of iteration is odd, it's
still O(n)!

What is the O() of the space complexity? Why?
O(1), because there are only incidental temporary variables
that don't depend on the size of the data.
'''

def sidewinder(number_list):
    # ops = 0  # UNCOMMENT FOR INPUT/OPS COUNTING

    next_position = 0

    while number_list[next_position] != 0:
        # ops += 1  # UNCOMMENT FOR INPUT/OPS COUNTING
        next_position = number_list[next_position]

    # print(f"{len(number_list)=}, {ops=}")  # UNCOMMENT FOR INPUT/OPS COUNTING
    return next_position

def run_sidewinder():
    # Try each set of inputs
    numbers = [2, 6, 8, 5, 3, 7, 4, 9, 1, 0]
    # numbers = [39, 0, 0, 19, 43, 0, 0, 0, 0, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0, 42, 44, 0, 41, 0, 0, 0, 29, 0, 0, 38, 0, 0, 0, 0, 0, 26, 0, 0, 20, 3, 48, 18, 40, 13, 22, 0, 0, 0, 4, 35]
    # numbers = [13, 22, 0, 0, 72, 0, 20, 64, 67, 97, 0, 63, 0, 94, 30, 11, 57, 26, 31, 81, 35, 50, 0, 54, 47, 51, 86, 24, 49, 87, 78, 19, 6, 29, 40, 66, 39, 17, 65, 44, 1, 34, 28, 9, 23, 4, 80, 43, 46, 56, 52, 53, 68, 27, 45, 90, 77, 76, 98, 0, 0, 0, 0, 75, 16, 58, 85, 36, 37, 0, 0, 0, 21, 0, 0, 82, 84, 91, 93, 88, 79, 32, 7, 0, 18, 8, 14, 42, 95, 92, 41, 89, 25, 33, 15, 38, 0, 48, 55, 0]
    print(f"Found end of list at position: {sidewinder(numbers)}")

