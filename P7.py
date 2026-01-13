def palindrome_check(s):
    empty = ""
    length = len(s)
    for i in range(length-1, -1, -1):
        empty += s[i]
    return s == empty

def is_palindrome(e):
    return e == e[:: -1]


s = input("Enter a word")
e = input("Enter a word")
print(palindrome_check(s))
print(is_palindrome(e))