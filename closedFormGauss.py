from math import*

# Gives sum of numbers from 1 to 100


print "This program will sum numbers 1 to 100"
print
n = 0

list = []
while n < 100:
    n += 1
    list.append(n)

print "The sum of 1 to", n, "is", sum(list[0:])

print "Now, we want to try the closed for solution."
print 
print
new_n = int(raw_input("Enter the nth digit of your sum: "))

result = float(new_n*(new_n + 1)/2)

print result

