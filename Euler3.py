'''

A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Brute force approach

# Algorithm: List all possible three digit products and determine whether they create palindromes

numb_tuple = (0,1,2,3,4,5,6,7,8,9)

# There are 10^3 three digit numbers

for i in range(1000):
   print i
   
