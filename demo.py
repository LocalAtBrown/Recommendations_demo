"""
Mathematical utilities for Fibonacci sequence operations.
"""

def generate_fibonacci(n):
    """
    Generate Fibonacci sequence up to n numbers.
    
    Args:
        n (int): Number of elements in the sequence.
        
    Returns:
        list: List containing the Fibonacci sequence up to n elements.
    """
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

def nth_fibonacci(n):
    """
    Calculate the Nth Fibonacci number using iterative approach.
    
    Args:
        n (int): Position in the Fibonacci sequence.
        
    Returns:
        int: The Nth Fibonacci number.
        
    Raises:
        ValueError: If n is negative or not an integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    fib = [0, 1]
    for i in range(2, n):
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)
    return fib[n-1]

def is_fibonacci_number(x):
    """
    Check if a number is part of the Fibonacci sequence.
    
    Args:
        x (int): Number to check.
        
    Returns:
        bool: True if x is in the Fibonacci sequence, False otherwise.
    """
    # A number is a Fibonacci number if and only if 5*x^2 +4 or 5*x^2 -4 is a perfect square
    import math
    s = 5 * x * x + 4
    return (math.isqrt(s) ** 2 == s) or (math.isqrt(s+1) ** 2 == s)
