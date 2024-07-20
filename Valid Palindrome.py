def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

input_str = input("Enter a string to check for palindrome: ")
print("Is palindrome:", is_palindrome(input_str))
