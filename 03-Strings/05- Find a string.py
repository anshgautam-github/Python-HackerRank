# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs
# in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Sample Input : ABCDCDC , CDC
# Sample Output : 2



def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1

    return count



# find() returns the index of the first occurrence, not the number of occurrences.

# Why count() is not enough You might think: s.count("CDC")
  
# But this problem wants overlapping matches.
# Example:
# s = "AAAA"
# sub = "AA"
# Possible matches:
# AAAA
# ^^
#  AA
#   ^^
# There are 3 occurrences.

# But:s.count("AA") returns: 2 because count() counts non-overlapping matches.
