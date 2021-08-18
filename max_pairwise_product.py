# python3
# NOTE: thought alt might be faster than if method, but it ended up slower?
# Reason: Sort is nlog(n), which is slower then n when n is huge.

def max_pairwise_product(numbers):
    largest = -99
    second_largest = -99
    for number in numbers:
        if number > largest:
            temp = largest
            largest = number
            if temp > second_largest:
                second_largest = temp
        elif number > second_largest:
            second_largest = number

    return largest * second_largest


def max_pairwise_product_alt(numbers):
    # alternative that maybe faster: sort and return first 2 multiplied
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
