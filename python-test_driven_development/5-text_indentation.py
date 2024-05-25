#!/usr/bin/python3
"""
This function prints a text with 2 new lines
after each ".", "?", ":"
"""


def text_indentation(text):
    """
    This function returns the updated text with new lines.

    Args:
    text (str): full text

    Return:
        prints new text with 2 new lines as per required
        characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result, end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
