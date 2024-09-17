# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find all two-digit prime numbers
two_digit_primes = [num for num in range(10, 100) if is_prime(num)]

# Display the result
print("The two-digit prime numbers are:")
print(two_digit_primes)
