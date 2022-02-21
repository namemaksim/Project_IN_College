import re  # импортируем модуль для работы с регул. выражениями
with open('text.txt', 'r', encoding='utf-8') as text:
    with open('_Otvet_.txt', 'w', encoding='utf-8') as f:
        result = re.compile(r'\d\d\.\d\d\.\d\d\d\d', re.S)  # компилируем регул. выраж. по формату даты
        result = re.findall(result, text.read())  # находит все элементы схожие с регул. выраж.
        print('Ответ: ', ' '.join(result))  # вывод ответа
        f.write(' '.join(result))  # вывод ответа 2
