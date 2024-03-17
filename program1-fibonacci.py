def generate_fibonacci(n):
    
    # Initializing the Fibonacci sequence with the first two terms
    fibonacci = [0, 1]

    # Generating the Fibonacci sequence up to the nth term of the user
    for i in range(2, n):
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)
    
    return fibonacci

def main():
    print("Welcome to the Fibonacci Sequence Generator!")
    
    # Input validation loop
    while True:
        try:
            n = int(input("Enter the number of terms for the Fibonacci sequence: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generating the Fibonacci sequence
    fibonacci = generate_fibonacci(n)
    
    # Output the Fibonacci sequence
    print("The Fibonacci sequence up to the", n, "term(s) is:")
    print(fibonacci)

if __name__ == "__main__":
    main()
