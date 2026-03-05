# Examples of string methods in Python

# Test string
text = "Hello123 World!"
name = "John"
space_text = "   spaces   "
number = "12345"

# isalpha() - checks if all characters are alphabetic
print(f"Is '{name}' all alphabetic? {name.isalpha()}")  # True
print(f"Is '{text}' all alphabetic? {text.isalpha()}")  # False

# isdigit() - checks if all characters are digits
print(f"Is '{number}' all digits? {number.isdigit()}")  # True
print(f"Is '{text}' all digits? {text.isdigit()}")     # False

# isalnum() - checks if all characters are alphanumeric
print(f"Is 'Hello123' alphanumeric? {'Hello123'.isalnum()}")  # True
print(f"Is '{text}' alphanumeric? {text.isalnum()}")         # False

# strip() - removes leading and trailing whitespace
print(f"Original text: '{space_text}'")
print(f"Stripped text: '{space_text.strip()}'")

# upper() and lower() - change case
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# startswith() and endswith()
print(f"Does '{text}' start with 'Hello'? {text.startswith('Hello')}")
print(f"Does '{text}' end with 'World!'? {text.endswith('World!')}")
