import math  
# Function 1: Check if number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Function 2: Check if a number is even
def is_even(n):
    return n % 2 == 0

# Function 3: Check if a number is a perfect square
def is_perfect_square(n):
    if n < 0:
        return False  # negative numbers can't be perfect squares
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

# Main program
def main():
    # Step 1: Get input from the user
    numbers = input("Enter numbers separated by space: ").split()
    numbers = [int(num) for num in numbers]  # convert input strings to integers

    # Step 2: Initialize counters for summary
    prime_count = 0
    even_count = 0
    odd_count = 0
    square_count = 0

    # Step 3: Analyze each number
    for n in numbers:
        print(f"\nAnalyzing number: {n}")
        
        # Prime check
        if is_prime(n):
            print(f"{n} is prime")
            prime_count += 1
        else:
            print(f"{n} is not prime")

        # Even or odd check
        if is_even(n):
            print(f"{n} is even")
            even_count += 1
        else:
            print(f"{n} is odd")
            odd_count += 1

        # Perfect square check
        if is_perfect_square(n):
            print(f"{n} is a perfect square")
            square_count += 1

    # Step 4: Summary
    print("\n--- Summary ---")
    print(f"Total numbers analyzed: {len(numbers)}")
    print(f"Primes: {prime_count}")
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Perfect squares: {square_count}")

if __name__ == "__main__":
    main()
