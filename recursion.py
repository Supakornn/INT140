# W7recursion
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

#factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  

#exponential
def exponential(x, n):
    if n <= 0:
        return 1

    return x * exponential(x, n-1)

print(exponential(2, 3))  

#fibonacci
def fibonacci(n):
    if n <= 0:
        return
    elif n ==1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

#palindrome
def palindrome(s): 
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

print(palindrome("madam")) 

