# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def valid_palindrome(s):
    for i in range(len(s)):#range is required bcs looping is only possible through elements, otherwise use while
        temp = s[:i] + s[i+1:]
        if temp[::] == temp[::-1]:
            print(temp)
            return True

    return False

print(valid_palindrome('radkar'))
print(valid_palindrome('pivooip'))
print(valid_palindrome('radafa'))
