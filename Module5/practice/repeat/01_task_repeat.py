# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    pass
def gen_list(size, of, to):
    pass


import random


def gen_list(size, of=5, to=25):
    my_list = []
    for _ in range(size):
        my_list.append(random.randint(of, to))
    return my_list


print(gen_list(10, -30, 30))
