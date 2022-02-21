# найдите пустые строчки
import re
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    s = re.compile(r"^\s*$")
    print(s.findall(text))
