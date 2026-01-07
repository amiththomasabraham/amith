string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

half = len(string) // 2

if string[:half] == string[-half:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")
