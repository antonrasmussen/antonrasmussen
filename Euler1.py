
print""
print""
print "Euler 1"
print""
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

'''
After a bit more experience with Python and Data Science, I began Project Euler anew. The following is my  11/18/14 
method of solving PE1

We want to know sum of all multiples of 3 and 5 below 1000.

So, we need three steps:

(1) Sum of all multiples of 3 below 1000.
(2) Sum of all multiples of 5 below 1000.
(3) Sum of all multiples of 15 below 1000.

We will subtract (3) from (1) + (2) to address overcounting.

NOTE: Thanks to Gauss, we know that the sum of 1 to n = [(n*(n+1))/2]

Finding Multiples:

(1) All multiples of 3 are 3, 6, 9, ... , 999
(2) All multiples of 5 are 5, 10, 15, ... , 995
(3) All multiples of 15 are 15, 30, ... , 945

Using our Gauss info, we get:

(1) 3*1 + 3*2 + ... + 999 = 3*(1 + 2 + . . . 333), which implies:
- the sum of multiples of 3 below 1000 = 3*[(333*334)/2] = 166833

NOTE: if you're wondering where 333 came from,
it's just floor(999/3).

Likewise for (2) and (3):

- the sum of multiples of 5 below 1000 = 5*[(199*200)/2] = 99500
- the sum of multiples of 15 below 1000 = 15*[(66*67)/2] = 30240

NOTE: if you're wondering where 199 and 66 came from,
it's just floor(999/5) and floor(999/15), respectively.

'''
import numpy as np

n3 = np.floor(999/3) # these are "n" in Gauss' formula.
n5 = np.floor(999/5)
n15 = np.floor(999/15)

multThreeSum = 3 * np.sum(range(n3 + 1)) # use n + 1 since it starts at 1
multFiveSum = 5 * np.sum(range(n5 + 1))
multFifteenSum = 15 * np.sum(range(n15 + 1))

print(multThreeSum + multFiveSum - multFifteenSum)





'''






'''
#This was a cool method I found

end = 1000
bucket = set([])


for i in range(3, end, 3):
  bucket.add(i)

for i in range(5, end, 5):
  bucket.add(i)

total = sum(bucket)

print total



#this was my original approach but I made a mistake at (&)

result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i #(&)
print result
'''
'''

Interesting closed solution:

'''


def PE1(a, b, n):
    def f(x, n):
        fl = int((n-1)/x)
        return x * fl * (fl+1)
    return (f(a,n) + f(b,n) - f(a*b,n))/2
	
print PE1(3,5,1000)
