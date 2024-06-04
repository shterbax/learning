def is_palindrome(text):

    symbols_replace = {
            46: None,
            44: None,
            33: None,
            63: None,
            32: None,
            45: None,
            58: None,
        }

    text = text.lower().translate(symbols_replace)

    return text == text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'