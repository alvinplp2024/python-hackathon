def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

def main():
    print("Welcome to the Voting Eligibility Checker!")

    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if check_voting_eligibility(age):
        print("Congratulations! You are eligible to vote.")
    else:
        print("Sorry, you are not eligible to vote yet.")

if __name__ == "__main__":
    main()
