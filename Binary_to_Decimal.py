def binary_to_decimal(binary_str):
    try:
        decimal_val = int(binary_str, 2)
        print(f"The decimal equivalent of {binary_str} is {decimal_val}")
    except ValueError:
        print("Invalid binary input.")

if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    binary_to_decimal(binary_input)
