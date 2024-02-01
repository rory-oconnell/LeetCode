def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
    
# Example usage:
print(factorial(3)) # 6