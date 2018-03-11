

def is_palindrome(s):

    reverse = []
    i = len(s) - 1
    while i >= 0:
        reverse.append(s[i])
        i -= 1
    return ''.join(reverse) == s


# Takes care of sentence, consider only ascii
# def is_palindrome(s):
#
#     ascii_s = ''.join([c.lower() for c in s.lower() if 97 <= ord(c) < 122])
#
#     reverse = []
#     i = len(ascii_s) - 1
#     while i >= 0:
#         reverse.append(ascii_s[i])
#         i -= 1
#     return ''.join(reverse) == ascii_s


# Use list indexing, cleaner code
# def is_palindrome(s):
#
#     ascii_s = ''.join([c.lower() for c in s.lower() if 97 <= ord(c) < 122])
#
#     return ascii_s[len(ascii_s)::-1] == ascii_s
