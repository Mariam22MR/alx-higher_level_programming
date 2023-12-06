#!/usr/bin/python3
if __name__ == '__main__':
    """print all hidden directories"""
    import hidden_4
    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
