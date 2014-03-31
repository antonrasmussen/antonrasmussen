# Finds the nth fibonacci number recursively
# Only good for n <= 30

def recur_fib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)
    
print recur_fib(30)  #Enter F# to get the F#th Fib.
