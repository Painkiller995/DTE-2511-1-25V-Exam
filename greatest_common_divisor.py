def greates_common_divisor(a, b):
    k = 1

    while k <= a and k <= b:
        if a % k == 0 and b % k == 0:
            gcd = k
        k += 1
    return gcd


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"The greatest common divisor of {a} and {b} is {greates_common_divisor(a, b)}")


if __name__ == "__main__":
    main()
