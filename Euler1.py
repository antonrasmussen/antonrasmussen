
print""
print""
print "Euler 1"
print""
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
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
