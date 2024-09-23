'''
most_common_entry

What does this function do?
Finds the most common entry in a list of values

What is the O() of the time complexity? Why?

For the original case:
O(n^2), the outer loop examines each item in the list, and the
inner loop counts how many their are of that item. For the outer
loop, that makes n loops, and the inner loop loops (n-1), (n-2),
(n-3), etc. The sum of the inner terms (there are n-1 of them)
simplifies to roughly (n-1)n - (some constant) = n^2 - n - ..., 
which results in O(n^2)

For this modified case:
O(n), it loops over the numbers in the list once, then at worst
once more (when iterating over the map). This is 2n iterations,
or O(n).

What is the O() of the space complexity? Why?

For the original case:
O(1), the only variables used are not dependent on the size
of the input.

For this modified case:
O(n), at worst, the map will hold a pair of values for each 
value in the list (value and count). There are a few variables
that are not related to the number of items in the list as
well, but we can ignore those, leading to 2n size, or O(n)

Notice this shows an example of the tradeoff in space and time.
The revised version has a lower time complexity, but a higher
space complexity. This is a common tradeoff we have to consider.
'''

def most_common_entry(numbers):
    entry = numbers[0]
    max_number_of_occurences = 1

    current_index = 0
    while current_index < len(numbers):
        j = current_index + 1
        current_entry = numbers[current_index]

        current_count = 1
        while j < len(numbers):
            if numbers[j] == current_entry:
                current_count += 1

            j += 1

        if current_count > max_number_of_occurences:
            max_number_of_occurences = current_count
            entry = numbers[current_index]

        current_index += 1

    return entry

def run_most_common_entry():
    numbers = [1, 1, 2, 3, 5, 8, 13, 5, 21, 5]
    print(f"most common entry is: {most_common_entry(numbers)}")