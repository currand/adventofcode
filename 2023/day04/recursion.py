def factorial(n: int) -> int:
    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)

def fibonacci(n):
    print(f"Calling fibonacci({n})")  # Print the current function call
    if n == 0:  # Base case
        print(f"fibonacci({n}) = 0")  # Print the result for base case
        return 0
    elif n == 1:  # Base case
        print(f"fibonacci({n}) = 1")  # Print the result for base case
        return 1
    else:  # Recursive case
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"fibonacci({n}) = fibonacci({n - 1}) + fibonacci({n - 2}) = {result}")  # Print the result of the recursive case
        return result

# Test the function
# print(fibonacci(6))  # Output: 8

# sum a list
def list_sum(l: list) -> int:
    # base case is when a list is empty
    if len(l) == 0:
        return 0
    else:
        return l.pop() + list_sum(l)

print(list_sum([1,2,3,4]))