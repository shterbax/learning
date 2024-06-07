def first_word(text):
    """ Пошук першого слова """
    symbols_replace = {
        46: 32,
        44: 32,
        33: 32,
        63: 32,
        45: 32,
        58: 32,
    }
    text = text.translate(symbols_replace)
    text = text.split()

    return text[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
