# Example usage of split() and strip() in Python

text = "  Hello, world! Welcome to Python.  "

# strip() removes leading and trailing whitespace
stripped_text = text.strip()
print(f"After strip(): '{stripped_text}'")

# split() splits the string into a list using the specified separator (default is any whitespace)
words = stripped_text.split()
print(f"After split(): {words}")

# split() with a custom separator
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")
print(f"Split by comma: {fruits}")

# different types of strip()
custom_text = "---Hello, World!---"
custom_stripped = custom_text.strip("-")
print(f"Custom strip(): '{custom_stripped}'")


text= "Hello, world! Welcome to Python."
newtext= text.split(" ",1)[0]
print(newtext)