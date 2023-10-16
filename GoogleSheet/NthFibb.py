# First step it to generate a fibbonaci sequence

# Fibb = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...NthFibb]
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3

n = 3
fib = [0, 1]

if n < len(fib):
    print(fib[n])

else:
    while len(fib) <= n:
        last = fib[len(fib)-1]
        secondlast = fib[len(fib)-2]
        next = last + secondlast
        fib.append(next)
print(fib[n])



