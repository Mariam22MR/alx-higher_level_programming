#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        print('{} + {} = {}'.format(x, y, add(x, y)))
    elif operator == '-':
        print('{} - {} = {}'.format(x, y, sub(x, y)))
    elif operator == '*':
        print('{} * {} = {}'.format(x, y, mul(x, y)))
    elif operator == '/':
        print('{} / {} = {}'.format(x, y, div(x, y)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
