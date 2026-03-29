
# Recursive Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Naive Recursive Fibonacci
def fibonacci_naive(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# Memoized Recursive Fibonacci
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Example usage
if __name__ == "__main__":
    num = 5

    print("Factorial:", factorial(num))

    print("Fibonacci (Naive):")
    for i in range(num):
        print(fibonacci_naive(i), end=" ")

    print("\nFibonacci (Memoized):")
    for i in range(num):
        print(fibonacci_memo(i), end=" ")


# Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} -> {target}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk
    print(f"Move disk {n} from {source} -> {target}")

    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Example run
tower_of_hanoi(3, 'A', 'C', 'B')

# Recursive Binary Search
def binary_search(arr, left, right, target):
    if left > right:
        return -1  # target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")