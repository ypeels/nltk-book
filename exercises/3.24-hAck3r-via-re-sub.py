'''
Exercise 3.24

Using re.sub, which WAS NOT COVERED in the text...
'''

patterns = [
        (r'[aA][tT][eE]', r'8'),
        (r'[aA]', r'4'),
        (r'[eE]', r'3'),
        (r'[iI]', r'1'),
        (r'[oO]', r'0'),
        (r'[lL]', r'|'),
        (r'[sS]', r'5'),
        (r'\.', r' 5w33t!')
        ]


def hacker(str):
    import re
    for pattern, replacement in patterns:
        str = re.sub(pattern, replacement, str)
    return str

if __name__ == "__main__":
    print hacker(raw_input("Give me some text to h4ck3rize: "))
        
