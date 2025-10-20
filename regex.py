import re

"""
Simple regex examples — minimal and easy to read.
Save as regex.py and run to see outputs.
"""

def simple_search_examples():
    text = "Contact: alice@example.com, bob@work.co.uk; visit http://example.com/page"
    emails = re.findall(r"\S+@\S+\.\S+", text)          # quick email-like matches
    print("emails:", emails)

    first_url = re.search(r"https?://\S+", text)        # first URL
    print("first url:", first_url.group(0) if first_url else None)

    print("starts with 'Contact':", bool(re.match(r"Contact", text)))  # prefix check


def simple_sub_split_validate():
    s = " apple , banana ,cherry "
    cleaned = re.sub(r"\s*,\s*", ",", s).strip()       # remove extra spaces around commas
    print("cleaned:", cleaned)

    parts = re.split(r"[,\s]+", cleaned)               # split on commas or whitespace
    print("parts:", parts)

    # very simple email validation (pragmatic, not RFC-complete)
    email_re = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    print("alice@example.com valid?", bool(email_re.match("alice@example.com")))
    print("bad@@example..com valid?", bool(email_re.match("bad@@example..com")))

pattern = r"^[A-Za-z]+$"
words = ["Hello", "World123", "Test", "Hi!", "Python"]

for word in words:
    if re.match(pattern, word):
        print(f"{word} ✅ Only letters")
    else:
        print(f"{word} ❌ Contains something else")


if __name__ == "__main__":
    simple_search_examples()
    simple_sub_split_validate()
