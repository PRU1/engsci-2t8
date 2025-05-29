def string_times(str, n):
    """
    https://codingbat.com/prob/p193507
    
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    string_times('Hi', 2) â†’ 'HiHi'
    string_times('Hi', 3) â†’ 'HiHiHi'
    string_times('Hi', 1) â†’ 'Hi'
    """
    return n*str

def front_times(str, n):
    """
    https://codingbat.com/prob/p165097

    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

    front_times('Chocolate', 2) â†’ 'ChoCho'
    front_times('Chocolate', 3) â†’ 'ChoChoCho'
    front_times('Abc', 3) â†’ 'AbcAbcAbc'
    """
  # case 1: length of string >= 3
    temp = ""
    if len(str) >= 3:
        temp = str[0] + str[1] + str[2]
    else:
        for i in range(len(str)):
            temp += str[i]

    return n*temp


def array_count9(nums):
    """
    https://codingbat.com/prob/p166170

    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) â†’ 1
    array_count9([1, 9, 9]) â†’ 2
    array_count9([1, 9, 9, 3, 9]) â†’ 3
    """
    count = 0
    for elem in nums:
        if elem == 9:
            count += 1
    return count

def array_front9(nums):
    """
    https://codingbat.com/prob/p110166

    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

    array_front9([1, 2, 9, 3, 4]) â†’ True
    array_front9([1, 2, 3, 4, 9]) â†’ False
    array_front9([1, 2, 3, 4, 5]) â†’ False
    """
    count = len(nums) if len(nums) < 4 else 4
    for i in range(count):
        if nums[i] == 9:
            return True
    return False

def array123(nums):
    """
    https://codingbat.com/prob/p193604
    
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

    array123([1, 1, 2, 3, 1]) â†’ True
    array123([1, 1, 2, 4, 1]) â†’ False
    array123([1, 1, 2, 1, 2, 3]) â†’ True
    """
    for i in range(len(nums)-3+1):
        # look ahead
        temp = [nums[i], nums[i+1], nums[i+2]]
        if temp == [1,2,3]:
            return True
    return False

def string_match(a, b):
    """
    https://codingbat.com/prob/p182414
    
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

    string_match('xxcaazz', 'xxbaaz') â†’ 3
    string_match('abc', 'abc') â†’ 2
    string_match('abc', 'axc') â†’ 0
    """
      # assume both are the same sized string??
    count = 0
    yippie = min(len(a),len(b))
    for i in range(yippie-1):
        if a[i] == b[i] and a[i+1] == b[i+1]:
            count += 1
    return count

def first_half(str):
    """
    https://codingbat.com/prob/p107010

    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

    first_half('WooHoo') â†’ 'Woo'
    first_half('HelloThere') â†’ 'Hello'
    first_half('abcdef') â†’ 'abc'
    """
    test=''
    for i in range(len(str)//2):
        test += str[i]
    return test


def without_end(str):
    """
    https://codingbat.com/prob/p138533
    
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

    without_end('Hello') â†’ 'ell'
    without_end('java') â†’ 'av'
    without_end('coding') â†’ 'odin'
    """
    return str[1:-1]


def combo_string(a, b):
    """
    https://codingbat.com/prob/p194053

    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') â†’ 'hiHellohi'
    combo_string('hi', 'Hello') â†’ 'hiHellohi'
    combo_string('aaa', 'b') â†’ 'baaab'
    """
    # if len(a) <= len(b)
    if len(a) <= len(b):
        return a+b+a
    else:
        return b+a+b

def left2(str):
    """
    https://codingbat.com/prob/p160545
    
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

    left2('Hello') â†’ 'lloHe'
    left2('java') â†’ 'vaja'
    left2('Hi') â†’ 'Hi'
    """
    return str[2:] + str[0] + str[1]

def near_ten(num):
    """
    https://codingbat.com/prob/p165321

    Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

    near_ten(12) â†’ True
    near_ten(17) â†’ False
    near_ten(19) â†’ True
    """
    if num % 10 <= 2 or num % 10 >= 8:
        return True
    return False

def count_code(str):
    """
    https://codingbat.com/prob/p186048

    Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

    count_code('aaacodebbb') â†’ 1
    count_code('codexxcode') â†’ 2
    count_code('cozexxcope') â†’ 2
    """
    count = 0
    for i in range(len(str)-3):
        compare = str[i]+str[i+1]+str[i+3]
        if compare == "coe":
            count += 1
    return count


def end_other(a, b):
    """
    https://codingbat.com/prob/p174314

    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

    end_other('Hiabc', 'abc') â†’ True
    end_other('AbC', 'HiaBc') â†’ True
    end_other('abc', 'abXabc') â†’ True
    """
    a = a.lower()
    b = b.lower()
    endA = a[-len(b):]
    endB = b[-len(a):]
    if endA == b or endB == a:
        return True
    return False

def centered_average(nums):
    """
    https://codingbat.com/prob/p126968

    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

    centered_average([1, 2, 3, 4, 100]) â†’ 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) â†’ 5
    centered_average([-10, -4, -2, -4, -2, 0]) â†’ -3
    """
    nums.sort()
    sum = 0
    for elem in nums:
        sum += elem

    sum -= nums[0]
    sum -= nums[-1]

    return sum/(len(nums)-2)

"""
https://www.cs.toronto.edu/~guerzhoy/180/midterm/mt2022/paper.pdf#page=7

Write a function that, when called, returns the next digit of Ï€ (approx 3.14159...). You may assume that
the function will not be called more than 10 times.

The function would be used like this:

print(next_digit_pi()) # 3
print(next_digit_pi()) # 1
print(next_digit_pi()) # 4
print(next_digit_pi()) # 1

You may import math and use math.pi
"""

import math

# Define any additional global variables here
superPi = str(math.pi)
counter = 0

print(superPi)

def next_digit_pi():
    global superPi
    global counter
    value = ''
    if superPi[counter] == '.':
        counter += 1 
    value = superPi[counter]
    counter += 1 
    return value

if __name__ == "__main__":
    # Add any code to test your functions here
    pass