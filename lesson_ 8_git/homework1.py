def popular_words (text: str, words: list) -> dict:

    result = {}
    text = text.lower()
    text = text.split()

    for word in words:
        result.update({word.lower(): text.count(word.lower())})

    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
