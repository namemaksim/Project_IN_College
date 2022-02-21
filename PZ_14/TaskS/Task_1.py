# выписать цифры
import re
tyt = re.compile(r'\d')
print(re.findall(tyt, 'се96годня я пошел с Лерой гулять'))
