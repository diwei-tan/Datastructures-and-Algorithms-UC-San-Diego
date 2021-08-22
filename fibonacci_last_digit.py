# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    fib = [1, 1]

    for i in range(2, n):
        fib.append((fib[i-1] + fib[i-2]) % 10)

    return fib[n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
