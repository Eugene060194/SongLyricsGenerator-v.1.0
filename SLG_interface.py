"""Данный код описывает пользовательский интерфейс "генератора песенных текстов",
а так же связывает интерфейс с основным кодом программы. Интерфейс написан
с помощью встроенной библиотеки Tkinter."""

import os  # Используется для открытия сгенерированного файла после выполнения программы
import SLG_algorithm  # Основной модуль для генерации
from tkinter import *  # используется для создания пользовательского интерфейса
from tkinter import messagebox  # используется для вывода диалоговых окон на экран
from tkinter import ttk  # используется для создания шкалы прогресса
from threading import Thread  # используется для создания дополнительного программного потока

f = 0  # определяет тип рифмы куплетов(0-тип не выбран, 1-перекрестная, 2-последовательная)


def type_rhyme_1():  # функция нажатия на кнопку перекрестной рифмы(объявляет 1-ый тип рифмы)
    """
    Функция для присвоения переменной f значения 1.
    Соответствует перекрестному типу рифмы.
    Так же сообщает о смене типа рифмы пользователю.

    :return: -
    """
    # Использование внешней переменной
    global f
    # Переопределение внешней переменной (отвечает за тип рифмы куплета)
    f = 1
    # функция для вывода диалогового окна
    messagebox.showinfo('SongGen', 'Установлен перекрестный тип рифмы')
    # переопределение виджета описывающего тип рифмы
    RHYME_LABEL.config(text='Тип рифмы - перекрестный')


def type_rhyme_2():  # функция нажатия на кнопку последовательной рифмы(объявляет 2-ой тип рифмы)
    """
    Функция для присвоения переменной f значения 2.
    Соответствует последовательному типу рифмы.
    Так же сообщает о смене типа рифмы пользователю.

    :return: -
    """
    # Использование внешней переменной
    global f
    # Переопределение внешней переменной (отвечает за тип рифмы куплета)
    f = 2
    # функция для вывода диалогового окна
    messagebox.showinfo('SongGen', 'Установлен последовательный тип рифмы')
    # переопределение виджета описывающего тип рифмы
    RHYME_LABEL.config(text='Тип рифмы - последовательный')  # переопределение свойства(текст виджета)


def start_gen(val1, val2, val3, val4, val5):  # основная функция генерации
    """

    :param val1:
    :param val2:
    :param val3:
    :param val4:
    :param val5:
    :return:
    """
    # Использование внешней переменной
    global f
    # Блок try/except для перехвата TclError, при неверном пользовательском вводе
    try:
        # Условие генерации с перекрестной рифмой куплета
        if f == 1:
            # запуск модульных функций генерации
            SLG_algorithm.verse_cross(val1.get(), val2.get(), val3.get())
            SLG_algorithm.chorus(val4.get(), val5.get())
        # Условие генерации с последовательной рифмой куплета
        elif f == 2:
            # запуск модульных функций генерации
            SLG_algorithm.verse_stream(val1.get(), val2.get(), val3.get())
            SLG_algorithm.chorus(val4.get(), val5.get())
        # Условие вывода окна ошибки
        elif f == 0:
            messagebox.showinfo('SongGen', 'не выбран тип рифмы!')
        # открытие готового текста по завершении генерации
        os.startfile('COMPLETE_TEXT.txt')
    except TclError:
        messagebox.showinfo('SongGen', 'неверный ввод!')
    # остановка работы шкалы прогресса
    PB.stop()


def start_button():  # промежуточная функция, присваиваемая кнопке начала генерации
    """
    Данная функция выполняет следующие задачи:
    1) Запуск основной функции генерации в параллельном потоке
    2) Передача аргументов, в виде данных с полей ввода в основную
    функцию генерации
    3) Запуск работы шкалы прогресса

    :return: -
    """
    # Запуск работы шкалы прогресса
    PB.start([6])
    # Объявление переменной с информацией о дополнительном потоке программы (основная функция генерации)
    th = Thread(target=start_gen, args=(a, b, c, d, e))
    # Запуск второго потока
    th.start()


# создание окна программы
window = Tk()
# установка цвета фона окна
window['bg'] = 'yellow'
# установка названия программы
window.title('SLG v.1.0')
# тут можно настроить прозрачность окна
window.wm_attributes('-alpha', 0.95)
# установка базовых размеров окна
window.geometry('535x300')
# установка запрета на изменение геметрии окна
window.resizable(width=False, height=False)

# Объявление переменных для полей ввода
a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()

# Создание текстовых виджетов
NAME_VERSE = Label(text='_______Параметры куплета_______')
NAME_VERSE.grid(row=0, column=1, sticky='ns')
NAME_1 = Label(text='Кол-во рифмованных строк:')
NAME_1.grid(row=1, column=0, sticky='e')
NAME_2 = Label(text='Кол-во куплетов:')
NAME_2.grid(row=2, column=0, sticky='e')
NAME_3 = Label(text='Кол-во словосочетаний в строке:')
NAME_3.grid(row=3, column=0, sticky='e')
NAME_CHORUS = Label(text='_______Параметры припева_______')
NAME_CHORUS.grid(row=6, column=1, sticky='ns')
NAME_4 = Label(text='Кол-во пар строк:')
NAME_4.grid(row=7, column=0, sticky='e')
NAME_5 = Label(text='Кол-во слов в строке:')
NAME_5.grid(row=8, column=0, sticky='e')

# Создания полей ввода для соответсвующих текстовых виджетов
input_1 = Entry(textvariable=a)
input_1.grid(row=1, column=2, sticky='w')
input_2 = Entry(textvariable=b)
input_2.grid(row=2, column=2, sticky='w')
input_3 = Entry(textvariable=c)
input_3.grid(row=3, column=2, sticky='w')
input_4 = Entry(textvariable=d)
input_4.grid(row=7, column=2, sticky='w')
input_5 = Entry(textvariable=e)
input_5.grid(row=8, column=2, sticky='w')

# Создание кнопок для выбора/переключения типа рифмы куплета
RHYME_BUTTON_1 = Button(text='Перекрестная рифма', command=type_rhyme_1)
RHYME_BUTTON_1.grid(row=4, column=0, sticky='e')
RHYME_BUTTON_2 = Button(text='Последовательная рифма', command=type_rhyme_2)
RHYME_BUTTON_2.grid(row=4, column=2, sticky='w')

# Создания текстового виджета описывающего выбранный тип рифмы куплета
RHYME_LABEL = Label(text='Тип рифмы не выбран')
RHYME_LABEL.grid(row=5, column=1, sticky='ns')

# Создание кнопки для начала генерации
START_BUTTON = Button(text='Генерировать!', command=start_button)
START_BUTTON.grid(row=9, column=1, sticky='ns')

# Создание шкалы прогресса выполнения программы
PB = ttk.Progressbar(window, orient=HORIZONTAL, length=150, mode='indeterminate')
PB.grid(row=10, column=1, sticky='ns')

# Программный цикл tkinter
window.mainloop()
