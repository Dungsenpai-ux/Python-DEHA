def fibonacci_sequence(n):
    # Initialize an array to store Fibonacci values
    fib = [0] * (n + 1)
    # Base cases
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    # Compute Fibonacci values iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

# Input from user
n = int(input("Enter a number n to calculate the Fibonacci sequence up to nth number: "))
fib_sequence = fibonacci_sequence(n)
print(f"The Fibonacci sequence up to {n}th number is: {fib_sequence}")
