def fibonacci_sequence(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib
n = int(input("Viết số n tương ứng số số hạng: "))
fib_sequence = fibonacci_sequence(n)
print(f"{fib_sequence}")
