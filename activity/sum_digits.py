'''
sum_digits

What does this function do?
Sums the digits in a number by performing modulo division to
get the one's digit, and using regular division to shift the
remaining digits down by a power of 10 (one place to the right).

What is the O() of the time complexity? Why?

There are (at least) two perspectives for the time complexity of
this code:

O(log10 n). n in this case is the number. For a base 10 number,
log10 gives a value corresponding roughly to the number of
digits it has (log10(100) -> 2, log10(10000) -> 4). Another
perspective is that we are dividing the input by 10 with each
pass through the loop. Much like dividing data in half gives us
log(n) (really log2(n), diving by 10 gives us log10(n), so our
result is O(log10 n). As the number increases by a factor of 10,
the number of iterations increases by 1.

O(n). n in this case is the number of _digits_ in the number.
If the number is 123, it has 3 digits, and the while loop iterates
3 times. As the number of digits increases, the number of iterations
increases at the same pace.

It is _very_ important to specify our definition of n for these
two perspectives to make sense. In general, we cannot say that
O(log10 n) is equivalent to O(n). But as written, those definitions
are incomplete. We _must_ define what n means for it to make sense.

This allows us to say that it is equivalent to call this code either
1) O(log10 n), where n is the input number (e.g., 123), or
2) O(n), where n is the number of digits (e.g., 3).

The O(n) perspective is a very human interpretation due to how
we tend to experience numbers as a sequence of decimal digits, but
a computer doesn't store numbers in that way. As a result, the 
O(log10 n) view could be considered more precise, while the O(n) 
view might be more intuitive. But if we recognize that the number 
of decimal digits in a number is very closely related to its log10, 
that gives us a way to see how we can move between these two 
perspectives, and why they are equivalent, so long as we are 
explicit about our definition of n.

What is the O() of the space complexity? Why?
O(1), since the variables used are unrelated to the size of the
input.
'''

def sum_digits(number):
    sum = 0 
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def run_sum_digits():
    num = 123
    # num = 12345678
    # num = 123456789012345678901234567890
    print(f"sum of the digits: {sum_digits(num)}")