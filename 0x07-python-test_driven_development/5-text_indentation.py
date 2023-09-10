#!/c/Users/maham/AppData/Local/Microsoft/WindowsApps/python
"""
    This module contains a function that prints a text passed to it
    and prints two new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """this function prints a text and indents it properly

        Args:
        text: text to be indented.

        Returns: None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims = ".?:"
    sentences = []
    sentence = ""

    for char in text:
        if char.isspace():
            continue
        sentence += char
        if char in delims:
            sentences.append(sentence.strip())
            sentence = ""

    if sentence:
        sentences.append(sentence.strip())

    for i, sentence in enumerate(sentences):
        print(sentence)
        if i < len(sentences) - 1:
            print()
