import re

example = '走る'
# Unicode representation of hiragana all through hexidecimal values 
hiragana_pattern = ''
katakana_pattern = ''


start = 0x3040
end = 0x309F

for code_point in range(start, end + 1):
    print(chr(code_point), end=' ')