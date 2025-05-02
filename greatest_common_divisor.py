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
    while b != 0:
        a, b = b, a % b
    return a


def main():
    """
    Prompts the user to enter two integers and prints their greatest common divisor
    using either the incremental, decremental, or Euclid's algorithm.
    """
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        method = input("Choose method (1 for Incremental, 2 for Decremental, 3 for Euclid's Algorithm): ")

        if method == "1":
            gcd = greatest_common_divisor_incremental(a, b)
            print(f"The greatest common divisor of {a} and {b} (using Incremental) is {gcd}")
        elif method == "2":
            gcd = greatest_common_divisor_decremental(a, b)
            print(f"The greatest common divisor of {a} and {b} (using Decremental) is {gcd}")
        elif method == "3":
            gcd = greatest_common_divisor_euclid(a, b)
            print(f"The greatest common divisor of {a} and {b} (using Euclid's Algorithm) is {gcd}")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
