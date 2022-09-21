# '''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

with open('file.txt', 'w') as data:
    data.write('абвешка абв fsz wefef hello worldабв\n')


with open('file.txt', 'r') as line:
    old_data = line.read()


def delt_char(text):
    new_text = " ".join(filter(lambda x: 'абв' not in x, text.split()))
    return new_text


with open('file.txt', 'w') as new_line:
    new_data = delt_char(old_data)
    new_line.write(new_data)
 
 
data_rez = open('file.txt', 'r')
for line in data_rez:
    print(line)
    print(" ".join(filter(lambda x: 'абв' not in x, line.split())))
data_rez.close()
 
with open('file.txt', 'w+') as data:
    data.writelines('абвешка абв fsz wefef hello worldабв\n')
    data.seek(0, 0)
    print('Иcходный текст: ')
    print(data.readlines())
    data.seek(0, 0)
    data.write(" ".join(filter(lambda x: 'абв' not in x, data.readline().split())))
    data.seek(0, 0)
    print('Итоговый текст: ')
    print(data.readlines()[1:])
 
 
with open('file.txt', 'w+') as data:
    data.writelines('абвешка абв fsz wefef hello worldабв\n')
    data.seek(0, 0)
    print('Иcходный текст: ')
    print(data.readlines())
    data.seek(0, 0)
    replaced = data.readlines()[0].split()
    replaced = [word for word in replaced if 'абв' not in word]

with open('file.txt', 'w+') as data:
    data.write(str(replaced))
    data.seek(0, 0)
    print('Итоговый текст: ')
    print((' '.join(data.readlines())))