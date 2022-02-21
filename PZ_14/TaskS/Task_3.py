#  выписать цифры
import re
s = re.compile(r"^[\w]+[0-9]")
print(s.findall("Мне17, а им всем за 90"))