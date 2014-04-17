'''

A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Brute force approach

# Algorithm: List all possible three digit products and determine whether they create palindromes

numb_tuple = (0,1,2,3,4,5,6,7,8,9)

# There are 10^3 three digit numbers minus the numbers with 0xx or 00x. 

count_three_digits = 0
for i in range(100,1000):
   count_three_digits += 1
   print count_three_digits

# Since there are 100 numbers that start with 0xx or 00x (namely, 000 to 099), there are 10^3 - 100 = 900 three-digit numbs 


# Since there are 900 three digit numbs and we want to know the number of products given two three-digit numbs
# we just use the multiplication rule (without replacement) to find that there are 900*899 total products given two three-digit numbs.

# Proof
'''

Step 1) Pick a three digit number. (There are 900 ways)
Step 2) For each three digit number, pick a NEW three digit number <- Needs to be new because x * y = y * x 

Thus there are 900 * 899 =  809100 total products given two three-digit numbers

'''

# Finding the 809100 products given two three-digit numbers

vect1 = range(100,1000)

loop = 1000
count = 0

while loop > 0:
   for i in vect1:
      print i * i+1
      loop -= 1
      count += 1
      print count

