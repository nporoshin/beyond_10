import os
import sys
import shutil

def создание():
    новая_директория = input('введите имя для новой директории: ')
    print(f' новая_папка: {новая_директория}  \n')
    if not os.path.exists(новая_директория):
        os.mkdir(новая_директория)
    else:
        print('Директория уже существует !')
    pass

def удаление():
    директория = input('введите имя удаляемой директории: ')
    print(f' удаляемая директория: {директория}  \n')
    if os.path.exists(директория):
        os.rmdir(директория)
    else:
        print('Такой директории не существует !')
    pass

def копирование():
    print('коптрование======')
    что = input('введите что копируем:')
    куда = input('введите куда копируем:')
    try:
        shutil.copy(что, куда)
    except Exception:
        print('ОШИБКА при копировании')
    pass

def просмотр_содержимого():
    содержимое = os.listdir()
    for i in содержимое:
        if os.path.isdir(i):
            print('директория:', i)
    for i in содержимое:
        if os.path.isfile(i):
            print('файл:',i)
    pass


def просмотр_директорий():
    содержимое = os.listdir()
    for i in содержимое:
        if os.path.isdir(i):
            print('директория:', i)
    pass

def просмотр_файлов():
    содержимое = os.listdir()
    for i in содержимое:
        if os.path.isfile(i):
            print('файл:',i)
    pass

def информацияОС():
    print(sys.platform)
    print(sys.path)
    print(sys.executable)
    pass

def смена_директории():

    pass