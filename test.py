# Example Python script to take 3 numbers as input, sum them, and show the output

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        total = num1 + num2 + num3
        print(f"The sum of the numbers is: {total}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()