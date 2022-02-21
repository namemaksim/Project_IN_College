# Выделите одним махом только текстовую часть оглавления, без тегов
import re
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    s = re.compile(r":(.+)</a>;")
    print(s.findall(text))
