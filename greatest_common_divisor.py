import time


def greatest_common_divisor_incremental(a, b):
    """
    Returns the greatest common divisor (GCD) of two numbers using an incremental approach.
    """
    gcd = 1
    k = 1
    while k <= a and k <= b:
        if a % k == 0 and b % k == 0:
            gcd = k
        k += 1
    return gcd


def greatest_common_divisor_decremental(a, b):
    """
    Returns the greatest common divisor (GCD) of two numbers using a decremental approach.
    """
    for k in range(min(a, b), 0, -1):
        if a % k == 0 and b % k == 0:
            return k
    return 1


def greatest_common_divisor_euclid(a, b):
    """
    Returns the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    """
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor_euclid(b, a % b)


def test_method(method, a, b):
    """
    Helper function to test each method and print the result along with the time taken.
    """
    start_time = time.time()  # Start the timer
    gcd = method(a, b)  # Call the method
    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate time taken

    return gcd, elapsed_time


def main():
    """
    Prompts the user to enter two integers, tests all GCD methods,
    and prints their results along with the time taken for each method.
    """
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        methods = [
            (greatest_common_divisor_incremental, "Incremental"),
            (greatest_common_divisor_decremental, "Decremental"),
            (greatest_common_divisor_euclid, "Euclid's Algorithm"),
        ]

        for method, method_name in methods:
            gcd, elapsed_time = test_method(method, a, b)
            print(f"\nMethod: {method_name}")
            print(f"The greatest common divisor of {a} and {b} is {gcd}")
            print(f"Time taken: {elapsed_time:.6f} seconds")

    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
