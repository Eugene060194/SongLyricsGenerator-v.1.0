"""Этот код предназначен для генерации "песенных текстов".
Словарная база взята из сети-интернет, и представляет собой .txt-файлы,
с отсортированными по алфавиту словами русского языка. В данном генераторе
используются только существительные, глаголы, местоимения и прилагательные.
Генерация осуществляется рандомным образом, с помощью модуля "random",
на основе пользовательских данных о кол-ве куплетов, кол-ве строк в куплетах,
кол-ве слосочетаний в куплетах, а так же анологичной информации о составе припева."""

# Подключаем модули
from random import randint, choice  # Используется для рандомизации текстового наполнения текста
import codecs  # Используется для корректного чтения словарных баз
import SLG_rhymes_module  # Специально созданный модуль, для подбора рифм, на основании словарных баз


def filtration(file, max_slog, max_cons):  # Функция фильтрации слов в базе
    """
    Функция фильтрации. Исключает из базы слишком длинные слова

    :param file: список со словами(база)
    :param max_slog: максимальное кол-во слогов в слове
    :param max_cons: максимальное кол-во согласных в слове
    :return: отфильтрованный список со словами
    """
    # Хранит список слов из базы
    file_list = (file.readlines())
    # Хранит прошедшие фильтр слова(пока пуст)
    filter_list = []
    # Цикл, просчитывающий кол-во гласных и согласных звуков в каждом слове из базы
    for i in file_list:
        # Хранит кол-во гласных звуков в слове
        slog_in_word = 0
        slog_in_word += str(i).count('а')
        slog_in_word += str(i).count('е')
        slog_in_word += str(i).count('ё')
        slog_in_word += str(i).count('и')
        slog_in_word += str(i).count('у')
        slog_in_word += str(i).count('о')
        slog_in_word += str(i).count('э')
        slog_in_word += str(i).count('ю')
        slog_in_word += str(i).count('я')
        slog_in_word += str(i).count('ы')
        # Хранит кол-во согласных звуков в слове
        consonant_letter = 0
        consonant_letter += str(i).count('б')
        consonant_letter += str(i).count('в')
        consonant_letter += str(i).count('г')
        consonant_letter += str(i).count('д')
        consonant_letter += str(i).count('ж')
        consonant_letter += str(i).count('з')
        consonant_letter += str(i).count('м')
        consonant_letter += str(i).count('н')
        consonant_letter += str(i).count('л')
        consonant_letter += str(i).count('п')
        consonant_letter += str(i).count('р')
        consonant_letter += str(i).count('с')
        consonant_letter += str(i).count('т')
        # Условие прохождения слова через фильтр
        if slog_in_word <= max_slog and consonant_letter <= max_cons:
            filter_list.append(i)
    file.close()
    return filter_list


def gen_block_words(x, y):  # Вспомогательная функция генерации словосочетаний в куплетах
    """
    Функция генерации словосочетаний

    :param x: первый список слов
    :param y: второй список слов
    :return: словосочетание
    """
    # Хранит список из двух рандомных слов баз "x" и "y"
    block_word = [x[randint(0, (len(x)-1))], y[randint(0, (len(y)-1))]]
    # Хранит первое слово, и далее исключает из него "\n" и "\r"
    fw1_1 = str(block_word[0])
    fw1_1.replace('\n', '')
    fw1_1.replace('\r', '')
    # Хранит второе слово, и далее исключает из него "\n" и "\r"
    tw1_1 = str(block_word[1])
    tw1_1.replace('\n', '')
    tw1_1.replace('\r', '')
    # Хранит "чистое" словосочетание(строка)
    block_word_clean = fw1_1+' '+tw1_1
    return block_word_clean


def search_rhyme_verse(base_str, file):  # Вспомогательная функция поиска рифмы (Используется для куплетов)
    """
    Функция поиска рифмы (для куплета).
    В куплете строки состоят из слововсочетаний

    :param base_str: строка, в виде списка, которую надо зарифмовать
    :param file: список слов в котором ищем рифму
    :return: список с рифмами
    """
    # Хранит последнее словосочетание рифмуемой строки
    a = str(base_str[len(base_str) - 1])
    # Хранит последнее слово в словосочетании
    a = str(a.split(' ')[1])
    # Хранит список с рифмами из модуля
    rhymes_words = SLG_rhymes_module.rhyme(a, file)
    # Проверка на пустоту списка с рифмами и дальнейший вывод функции
    if rhymes_words:
        return rhymes_words
    else:
        return ['!нет рифмы!']


def search_rhyme_chorus(base_str, file):  # Вспомогательная функция поиска рифмы (Используется для припева)
    """
    Функция поиска рифмы (для припева).
    В припеве строки состоят из отдельных слов

    :param base_str: строка, в виде списка, которую надо зарифмовать
    :param file: список слов в котором ищем рифму
    :return: список с рифмами
    """
    # Хранит последний элемент(слово) рифмуемой строки припева
    a = base_str[len(base_str)-1]
    # Хранит список с рифмами из модуля
    rhymes_words = SLG_rhymes_module.rhyme(a, file)
    # Проверка на пустоту списка с рифмами и дальнейший вывод функции
    if rhymes_words:
        return rhymes_words
    else:
        return ['!нет рифмы!']


def count_string(x, y):  # Вспомогательная функция подсчета размера строки (Нужна для соблюдения размера)
    """
    Функция подсчета размера строки.

    :param x: строка, размер которой считаем
    :param y: кол-во элементов строки(слов или словосочетаний)
    :return: кол-во слогов в строке
    """
    # Хранит кол-во слогов в строке
    slog_string = 0
    # Цикл проходящий по элементам строки и считающий кол-во слогов
    for y1_1_1 in range(0, y):
        slog_string += x[y1_1_1].count('а')
        slog_string += x[y1_1_1].count('е')
        slog_string += x[y1_1_1].count('ё')
        slog_string += x[y1_1_1].count('и')
        slog_string += x[y1_1_1].count('у')
        slog_string += x[y1_1_1].count('о')
        slog_string += x[y1_1_1].count('э')
        slog_string += x[y1_1_1].count('ю')
        slog_string += x[y1_1_1].count('я')
        slog_string += x[y1_1_1].count('ы')
    return slog_string


def exit_text(x, y, file):  # Вспомогательная функция для вывода и записи готовых строк в файл
    """
    Функция вывода и записи готовых строк в файл

    :param x: первая строка на запись
    :param y: вторая строка на запись
    :param file: файл, в который записываем строки
    :return: -
    """
    # Хранит первую строку пары, далее исключает "\n" и "\r"
    x = ' '.join(x)
    x = x.replace('\n', '')
    x = x.replace('\r', '')
    # Хранит вторую строку пары, далее исключает "\n" и "\r"
    y = ' '.join(y)
    y = y.replace('\n', '')
    y = y.replace('\r', '')
    # Проверка на прямое исполнение. Выведет строки на экран, при прямом исполнении
    if __name__ == '__main__':
        print(x)
        print(y)
    # Запись первой строки -> enter -> запись второй строки -> enter
    file.write(x), file.write('\n'), file.write(y), file.write('\n')


def verse_cross(value1, value2, value3):  # Функция для перекресной рифмы (куплет)
    """
    Функция генерации куплета с перекрестной рифмой.
    Генерация осуществляется словосочетаниями(2 слова).
    Делает вывод в .txt файл

    :param value1: кол-во ПАР строк в куплете (строка-рифма)
    :param value2: кол-во куплетов
    :param value3: кол-во словосочетаний в строке куплета
    :return: -
    """
    # Хранят последние две строки текста (для зарифмовки последующих двух)
    last_string_1 = ''
    last_string_2 = ''
    # Хранит в коде файл в который осуществляется запись готового текста
    complete = open('COMPLETE_TEXT.txt', 'w')
    # Хранит директивное кол-во слогов одной строки
    slog_block = 0
    # Цикл на воспроизводство куплетов
    for w in range(0, value2):
        # Запись номера куплета в файл
        complete.write('Куплет ' + str(w+1) + ':\n')
        # Цикл воспроизводства строк
        for i in range(0, value1):
            # Цикл поиска подходящей пары строк
            while True:
                # Хранят первую и вторую строки соответственно (обнуляют их при каждой итерации)
                string1 = []
                string2 = []
                # Условие заполнения первой и второй строк четверостишья
                if last_string_1 == '' and last_string_2 == '':
                    # Проверка наличия более 1 словосочетания в строке
                    if value3 > 1:
                        # Цикл заполнения первой строки (кроме последнего элемента)
                        for y1 in range(0, (value3-1)):
                            # Хранит рандомные словосочетания разных типов для заполнения
                            list_category1 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                              gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                            # Заполнение элемента строки
                            string1.append(choice(list_category1))
                    # Заполнение последнего элемента строки
                    string1.append(gen_block_words(ADJECTIVE_, WORDS_))
                    # Хранит кол-во слогов в первой строке (становится директивным на весь текст)
                    slog_string1 = count_string(string1, value3)
                    # Цикл подбора второй строки
                    while True:
                        # Проверка наличия более 1 словосочетания в строке
                        if value3 > 1:
                            # Цикл заполнения второй строки (кроме последнего элемента)
                            for y2 in range(0, (value3-1)):
                                # Хранит рандомные словосочетания разных типов для заполнения
                                list_category2 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                                  gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                                # Заполнение элемента строки
                                string2.append(choice(list_category2))
                        # Заполнение последнего элемента строки
                        string2.append(gen_block_words(ADJECTIVE_, WORDS_))
                        # Хранит кол-во слогов во второй строке
                        slog_string2 = count_string(string2, value3)
                        # Проверка соответствия размера строк между собой
                        if -1 <= slog_string1 - slog_string2 <= 1:
                            break
                        else:
                            string2 = []
                    # Проверка соответствия общего размера строк директивному
                    if slog_block == slog_string1:
                        # Хранит строки с текущей итерации для последующей
                        last_string_1 = string1
                        last_string_2 = string2
                        break
                    elif slog_block == 0:
                        last_string_1 = string1
                        last_string_2 = string2
                        break
                # Условие заполнения третьей и четвертой строк четверостишья
                else:
                    # Проверка наличия более 1 словосочетания в строке
                    if value3 > 1:
                        # Цикл заполнения третьей строки (кроме последнего элемента)
                        for y1 in range(0, (value3 - 1)):
                            # Хранит рандомные словосочетания разных типов для заполнения
                            list_category1 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                              gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                            # Заполнение элемента строки
                            string1.append(choice(list_category1))
                    # Заполнение последнего элемента при помощи функции подбора рифмы
                    string1.append(gen_block_words(ADJECTIVE_, search_rhyme_verse(last_string_1, WORDS_)))
                    # Хранит кол-во слогов в третьей строке
                    slog_string1 = count_string(string1, value3)
                    # Цикл подбора четвертой строки
                    while True:
                        # Проверка наличия более 1 словосочетания в строке
                        if value3 > 1:
                            # Цикл заполнения четвертой строки (кроме последнего элемента)
                            for y2 in range(0, (value3 - 1)):
                                # Хранит рандомные словосочетания разных типов для заполнения
                                list_category2 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                                  gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                                # Заполнение элемента строки
                                string2.append(choice(list_category2))
                        # Заполнение последнего элемента при помощи функции подбора рифмы
                        string2.append(gen_block_words(ADJECTIVE_, search_rhyme_verse(last_string_2, WORDS_)))
                        # Хранит кол-во слогов в четвертой строке
                        slog_string2 = count_string(string2, value3)
                        # Проверка соответствия размера строк между собой
                        if -1 <= slog_string1 - slog_string2 <= 1:
                            break
                        else:
                            string2 = []
                    # Проверка соответствия общего размера строк директивному
                    if slog_block == slog_string1:
                        # Обнуление переменных для подбора первой и второй строк в след. итерации
                        last_string_1 = ''
                        last_string_2 = ''
                        break
                    elif slog_block == 0:
                        last_string_1 = ''
                        last_string_2 = ''
                        break
            # Переназначение директивного размера (по умолчанию - 0)
            slog_block = slog_string1
            # Вывод подходящих строк
            exit_text(string1, string2, complete)
        # Проверка на прямое исполнение. Выведет enter, при прямом исполнении
        if __name__ == '__main__':
            print('\n')
        # записать enter между куплетами в итоговый файл
        complete.write('\n')
    complete.close()


def verse_stream(value1, value2, value3):  # Функция для последовательной рифмы (куплет)
    """
    Функция генерации куплета с последовательной рифмой.
    Генерация осуществляется словосочетаниями(2 слова).
    Делает вывод в .txt файл

    :param value1: кол-во ПАР строк в куплете (строка-рифма)
    :param value2: кол-во куплетов
    :param value3: кол-во словосочетаний в строке куплета
    :return: -
    """
    # Хранит в коде файл в который осуществляется запись готового текста
    complete = open('COMPLETE_TEXT.txt', 'w')
    # Хранит директивное кол-во слогов одной строки
    slog_block = 0
    # Цикл на воспроизводство куплетов
    for w in range(0, value2):
        # Запись номера куплета в файл
        complete.write('Куплет ' + str(w+1) + ':\n')
        # Цикл воспроизводства строк
        for i in range(0, value1):
            # Цикл поиска подходящей пары строк
            while True:
                # Хранят первую и вторую строки соответственно (обнуляют их при каждой итерации)
                string1 = []
                string2 = []
                # Проверка наличия более 1 словосочетания в строке
                if value3 > 1:
                    # Цикл заполнения первой строки (кроме последнего элемента)
                    for y1 in range(0, (value3-1)):
                        # Хранит рандомные словосочетания разных типов для заполнения
                        list_category1 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                          gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                        # Заполнение элемента строки
                        string1.append(choice(list_category1))
                # Заполнение последнего элемента строки
                string1.append(gen_block_words(ADJECTIVE_, WORDS_))
                # Хранит кол-во слогов в первой строке (становится директивным на весь текст)
                slog_string1 = count_string(string1, value3)
                # Цикл подбора второй строки
                while True:
                    # Проверка наличия более 1 словосочетания в строке
                    if value3 > 1:
                        # Цикл заполнения второй строки (кроме последнего элемента)
                        for y2 in range(0, (value3-1)):
                            # Хранит рандомные словосочетания разных типов для заполнения
                            list_category2 = [gen_block_words(WORDS_, ACTIVE_), gen_block_words(ADJECTIVE_, WORDS_),
                                              gen_block_words(NAME_, ACTIVE_), gen_block_words(NAME_, ADJECTIVE_)]
                            # Заполнение элемента строки
                            string2.append(choice(list_category2))
                    # Заполнение последнего элемента при помощи функции подбора рифмы
                    string2.append(gen_block_words(ADJECTIVE_, search_rhyme_verse(string1, WORDS_)))
                    # Хранит кол-во слогов во второй строке
                    slog_string2 = count_string(string2, value3)
                    # Проверка соответствия размера строк между собой
                    if -1 <= slog_string1-slog_string2 <= 1:
                        break
                    else:
                        string2 = []
                # Проверка соответствия общего размера строк директивному
                if slog_block == slog_string1:
                    break
                elif slog_block == 0:
                    break
            # Переназначение директивного размера (по умолчанию - 0)
            slog_block = slog_string1
            # Вывод подходящих строк
            exit_text(string1, string2, complete)
        # Проверка на прямое исполнение. Выведет enter, при прямом исполнении
        if __name__ == '__main__':
            print('\n')
        # записать enter между куплетами в итоговый файл
        complete.write('\n')
    complete.close()


def chorus(value1, value2):  # Функция для припева
    """
    Функция для генерации припева из одиночных слов.
    Делает вывод в .txt файл

    :param value1: кол-во ПАР строк в припеве (строка-рифма)
    :param value2: кол-во слов в строке припева
    :return: -
    """
    # Хранит в коде файл в который осуществляется дозапись готового текста
    complete = open('COMPLETE_TEXT.txt', 'a')
    # Хранит директивное кол-во слогов одной строки
    slog_block = 0
    # Запись маркера припева в файл
    complete.write('Припев:\n')
    # Цикл воспроизводства строк
    for i in range(0, value1):
        # Цикл поиска подходящей пары строк
        while True:
            # Хранят первую и вторую строки соответственно (обнуляют их при каждой итерации)
            string1 = []
            string2 = []
            # Проверка наличия более 1 слова в строке
            if value2 > 1:
                # Цикл заполнения первой строки (кроме последнего слова)
                for y1 in range(0, (value2-1)):
                    # Хранит рандомные слова разных типов для заполнения
                    list_category1 = [words_chorus[randint(0, (len(words_chorus)-1))],
                                      active_chorus[randint(0, (len(active_chorus)-1))],
                                      name_chorus[randint(0, (len(name_chorus)-1))],
                                      adjective_chorus[randint(0, (len(adjective_chorus)-1))]]
                    # Заполнение элемента строки
                    string1.append(choice(list_category1))
            # Обновление рандомных слов для заполнения последнего слова
            list_category1 = [words_chorus[randint(0, (len(words_chorus) - 1))],
                              active_chorus[randint(0, (len(active_chorus) - 1))],
                              name_chorus[randint(0, (len(name_chorus) - 1))],
                              adjective_chorus[randint(0, (len(adjective_chorus) - 1))]]
            # Заполнение последнего элемента строки
            string1.append(choice(list_category1))
            # Хранит кол-во слогов в первой строке (становится директивным на весь текст)
            slog_string1 = count_string(string1, value2)
            # Цикл подбора второй строки
            while True:
                # Проверка наличия более 1 слова в строке
                if value2 > 1:
                    # Цикл заполнения второй строки (кроме последнего слова)
                    for y2 in range(0, (value2 - 1)):
                        # Хранит рандомные слова разных типов для заполнения
                        list_category2 = [words_chorus[randint(0, (len(words_chorus)-1))],
                                          active_chorus[randint(0, (len(active_chorus)-1))],
                                          name_chorus[randint(0, (len(name_chorus)-1))],
                                          adjective_chorus[randint(0, (len(adjective_chorus)-1))]]
                        # Заполнение элемента строки
                        string2.append(choice(list_category2))
                # Заполнение последнего слова при помощи функции подбора рифмы
                string2.append(choice(search_rhyme_chorus(string1, (
                        words_chorus + active_chorus + name_chorus + adjective_chorus)))
                               )
                # Хранит кол-во слогов во второй строке
                slog_string2 = count_string(string2, value2)
                # Проверка соответствия размера строк между собой
                if -1 <= slog_string1 - slog_string2 <= 1:
                    break
                else:
                    string2 = []
            # Проверка соответствия общего размера строк директивному
            if slog_block == slog_string1:
                break
            elif slog_block == 0:
                break
        # Переназначение директивного размера (по умолчанию - 0)
        slog_block = slog_string1
        # Вывод подходящих строк
        exit_text(string1, string2, complete)
    # Проверка на прямое исполнение. Выведет enter, при прямом исполнении
    if __name__ == '__main__':
        print('\n')
    # записать enter между куплетами в итоговый файл
    complete.write('\n')
    complete.close()


# Фильтрация словарных баз с помощью соответствующей функции
WORDS_ = filtration(codecs.open('words.txt', 'r', 'ANSI'), 4, 5)
ACTIVE_ = filtration(codecs.open('active.txt', 'r', 'ANSI'), 4, 5)
NAME_ = filtration(codecs.open('name.txt', 'r', 'UTF-8'), 4, 5)
ADJECTIVE_ = filtration(codecs.open('adjective.txt', 'r', 'ANSI'), 4, 5)
words_chorus = filtration(codecs.open('words.txt', 'r', 'ANSI'), 3, 3)
active_chorus = filtration(codecs.open('active.txt', 'r', 'ANSI'), 3, 3)
name_chorus = filtration(codecs.open('name.txt', 'r', 'UTF-8'), 3, 3)
adjective_chorus = filtration(codecs.open('adjective.txt', 'r', 'ANSI'), 3, 3)

# Проверка на прямое исполнение. Выполнит программу
if __name__ == '__main__':
    # Сбор данных о структуре текста
    how_much1 = int(input('Введите кол-во рифмованных строк(две строки с рифмами)...'))
    how_much2 = int(input('Введите кол-во куплетов...'))
    how_much3 = int(input('Введите кол-во словосочетаний в строке...'))
    how_much_chorus1 = int(input('Введите кол-во пар строк в припеве...'))
    how_much_chorus2 = int(input('Введите кол-во слов в строке припева...'))
    # Выбор типа рифмы
    WHAT_VERSE = input('Введите \'1\' для перекрестной рифмы и введите \'2\' для последовательной рифмы')
    # Реализация программы в зависимости от выбранного типа рифмы
    if WHAT_VERSE == '1':
        verse_cross(how_much1, how_much2, how_much3)
        chorus(how_much_chorus1, how_much_chorus2)
    elif WHAT_VERSE == '2':
        verse_stream(how_much1, how_much2, how_much3)
        chorus(how_much_chorus1, how_much_chorus2)
