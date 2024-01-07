#!/usr/bin/python3
"""
Defination of text-indentation function.
"""

def text_indentation(text):
    """method for add 2 new line after '.?:' characters.

    Args:
        text: string text will be print.
    Raises:
        TypeError: if text not str.
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    n = 0
    while n < len(text) and text[n] == ' ':
        n += 1

    while n < len(text):
        print(text[n], end='')

        if text[n] == '\n' or text[n] in '.?:':
            if text[n] in '.?:':
                print('\n')
            print('\n')

            n += 1
            while n < len(text) and text[n] == ' ':
                n += 1

            continue

        n += 1

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
