
import re

example = '走る'
# Unicode representation of hiragana all through hexidecimal values 
hiragana_pattern = '[\u3040-\u309F]'
katakana_pattern = '[\u30A0-\u30FF]'

print(x)


start = 0x3040
end = 0x309F

for code_point in range(start, end + 1):
    print(chr(code_point), end=' ')