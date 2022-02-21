# выписать большие буквы
import re
tyt = re.compile(r'[А-ЯЁ]')
print(re.findall(tyt, 'меня зовут МАКСИМм, а Вас?'))
