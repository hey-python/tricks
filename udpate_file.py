import re

file_name = 'test.txt'


def replace_nth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    new_string = before + after
    return new_string


with open(file_name, 'r+') as f:
    text = ''
    lines = f.readlines()
    for line in lines:
        text += replace_nth(line, 'e', '/', 2)
    f.seek(0)
    f.write(text)
    f.truncate()
