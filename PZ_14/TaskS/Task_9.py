# выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами)
import re
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    s = re.compile(r"<a href=.+")
    print(s.findall(text))
