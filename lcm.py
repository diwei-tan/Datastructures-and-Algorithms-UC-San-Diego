# Uses python3
import sys

def lcm_naive(a, b):
    return int((a * b / gcd(a, b)))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
