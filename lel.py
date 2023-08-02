def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

word = "level"
if is_palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
