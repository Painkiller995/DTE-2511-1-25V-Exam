NUMBER_OF_PRIMES = 50  # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10  # Display 10 per line


def find_prime_numbers():
    """Find and display prime numbers."""

    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < NUMBER_OF_PRIMES:
        # Assume the number is prime
        is_prime = True  # Is the current number prime?

        # Test if number is prime
        divisor = 2
        while divisor <= number // 2:
            if number % divisor == 0:
                # If true, the number is not prime
                is_prime = False  # Set is_prime to false
                break  # Exit the for loop
            divisor += 1

        # Display the prime number and increase the count
        if is_prime:
            count += 1  # Increase the count
            display_prime_numbers(number, count)

        # Check if the next number is prime
        number += 1


def display_prime_numbers(number, count):
    print(format(number, "5d"), end="")
    if count % NUMBER_OF_PRIMES_PER_LINE == 0:
        print()


if __name__ == "__main__":
    find_prime_numbers()
