'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота. Достаточно сделать так, 
чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
b) Подумайте как наделить бота ""интеллектом"". 
Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. 
Достаточно довести игру до такой ситуации.'''

# вариант человека против человека:

# from random import randint
#
# candies = int(input('Введите общее количество конфет для игры: '))
# gamer1 = input('Введите имя первого игрока: ')
# gamer2 = input('Введите имя второго игрока: ')
# flag = randint(0, 2)
# if flag:
#     print(f'Первым ходит {gamer1}')
# else:
#     print(f'Первым ходит {gamer2}')
#
#
# def step_check(name):
#     number = int(input(f'{name}, введите количество конфет, которое возьмете, в диапазоне от 1 до 28: '))
#     if 1 <= number <= 28:
#         return number
#     else:
#         number = int(input("Необходимо взять конфеты в диапазоне от 1 до 28 шт.: "))
#         return number
#
#
# def step_print(name, numb, candy):
#     print(f'{name} взял {numb} конфет. В куче осталось {candy} конфет')
#
#
# while candies > 0:
#     if flag:
#         num = step_check(gamer1)
#         candies -= num
#         flag = False
#         step_print(gamer1, num, candies)
#     else:
#         num = step_check(gamer2)
#         candies -= num
#         flag = True
#         step_print(gamer2, num, candies)
# if flag:
#     print(f'Выиграл {gamer2}')
# else:
#     print(f'Выиграл {gamer1}')


##############################################################################################3
# вариант человека против бота:

# from random import randint

# candies = 51
# print(f'Играете против бота, на столе {candies} конфет.Выигрывает тот,кто забирает последние конфеты')
# step = randint(0, 2)
# while candies > 0:
#     if step:
#         if candies > 28:
#             bot_step = randint(0, 29)
#         else:
#             bot_step = randint(0, candies)
#         candies -= bot_step
#         print(f'Бот взял {bot_step} конфет, на столе осталось {candies}')
#         step = False
#     else:
#         people_step = int(input('Сколько конфет возьмете от 1 до 28? \n'))
#         if 1 <= people_step <= 28:
#             candies -= people_step
#             print(f'На столе осталось {candies} конфет')
#             step = True
#         else:
#             people_step = int(input('Введите количество от 1 до 28: '))
# if step:
#     print('Вы победили!)')
# else:
#     print('Вы проиграли(')

 
 