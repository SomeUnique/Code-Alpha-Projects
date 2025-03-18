# Fibonacci Series Generator in Python

def fibonacci_series(n):
    # First two numbers in Fibonacci sequence
    a, b = 0, 1
    series = []
    
    for _ in range(n):
        series.append(a)
        # Next number is the sum of the previous two
        a, b = b, a + b
    
    return series

# Get number of terms from user
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = fibonacci_series(num_terms)
    print("Fibonacci series:")
    print(fib_series)
