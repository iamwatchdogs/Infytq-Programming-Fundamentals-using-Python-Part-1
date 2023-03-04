#lex_auth_012693819159732224162

def check_palindrome(word):
    #Remove pass and write your logic here
    return word == word[::-1]

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
