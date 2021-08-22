"""Этот код предназначен для подбора рифм. В качестве исходных данных принимает слово
и базу слов, в которой необходимо найти рифмы. Код используется в качестве стороннего
модуля для основного внутреннего кода генератора песенных текстов."""

# Проверка на прямое исполнение
if __name__ == '__main__':
    import codecs  # Используется для корректного чтения словарных баз
    from random import choice  # Используется для получения рандомного слова из списка рифм


def rhyme(word, *args):  # Функция подбора рифмы
    """
    Функция подбора рифмы

    :param word: Слово, которому нужно подобрать рифму
    :param args: любое кол-во словарных баз (будут сложены)
    :return: список с рифмами
    """
    # Вырезает, при наличии, из базового слова символы новой строки
    word = word.replace('\r', '')
    word = word.replace('\n', '')
    # Хранит совмещенную словарную базу
    base_list = []
    # Хранит список с рифмами
    rhymes_list = []
    # Цикл заполнения совмещенной словарной базы
    for i in args:
        base_list += i
    # Хранит базовое слово в формате списка (каждый элемент это подобие слогов)
    base_word_in_list = []
    # Цикл разложения базового слова на элементы, состоящие из гласных и согласных звуков
    for i in word:
        # Условие для идентификации гласных в слове
        if i in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
            base_word_in_list.append(i)
        # Условие для идентификации согласных в слове
        if i in 'бвгджзклмнпрстфхцчшщйьъБВГДЖЗКЛМНПРСТФХЦЧШЩЙЬЪ':
            # Проверка пустоты списка (начало разложения)
            if not base_word_in_list:
                # Добавление согласной новым элементом списка
                base_word_in_list.append(i)
            else:
                # Добавление согласной к последнему элементу списка
                base_word_in_list[len(base_word_in_list)-1] += i
    # Проверка на прямое исполнение
    if __name__ == '__main__':
        # Вывод базового слова в формате списка
        print(base_word_in_list)
    # Цикл перебирающий словарную базу на наличие рифм
    for w in base_list:
        # Хранит элемент базы в формате списка
        word_in_list = []
        # Хранит копию элемента базы и далее вырезает из него символы новой строки
        y = w
        y = y.replace('\r', '')
        y = y.replace('\n', '')
        # Проверка, исключающая попадание введенного пользователем слова в список с рифмами
        if y == word:
            continue
        # Цикл разложения слова на элементы, состоящие из гласных и согласных звуков
        for i in y:
            # Условие для идентификации гласных в слове
            if i in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
                word_in_list.append(i)
            # Условие для идентификации согласных в слове
            if i in 'бвгджзклмнпрстфхцчшщйьъБВГДЖЗКЛМНПРСТФХЦЧШЩЙЬЪ':
                # Проверка пустоты списка (начало разложения)
                if not word_in_list:
                    # Добавление согласной новым элементом списка
                    word_in_list.append(i)
                else:
                    # Добавление согласной к последнему элементу списка
                    word_in_list[len(word_in_list)-1] += i
        # Проверка кол-ва слогов в базовом слове
        if len(base_word_in_list) == 2:
            # Блок try/except для перехвата IndexError, возникающего при оценке слишком коротких слов
            try:
                # Проверка соответствия последних слогов (при базовом слове не больше 2х слогов)
                if base_word_in_list[-1] == word_in_list[-1] and word[-2] == y[-2]:
                    # Добавление рифмы в список
                    rhymes_list.append(w)
            except IndexError:
                continue
        elif len(base_word_in_list) == 1:
            # Блок try/except для перехвата IndexError, возникающего при оценке слишком коротких слов
            try:
                # Проверка соответствия последних слогов (при базовом слове не больше 2х слогов)
                if base_word_in_list[-1] == word_in_list[-1]:
                    # Добавление рифмы в список
                    rhymes_list.append(w)
            except IndexError:
                continue
        elif len(base_word_in_list) == 3 and len(word) <= 5:
            # Блок try/except для перехвата IndexError, возникающего при оценке слишком коротких слов
            try:
                # Сравнение последних двух слогов
                if base_word_in_list[-1] == word_in_list[-1] and base_word_in_list[-2] == word_in_list[-2]:
                    # Добавление рифмы в список
                    rhymes_list.append(w)
                else:
                    # Сравнение последнего слога и двух предпоследних букв
                    if base_word_in_list[-1] == word_in_list[-1]:
                        # Добавление рифмы в список
                        rhymes_list.append(w)
            except IndexError:
                continue
        else:
            # Блок try/except для перехвата IndexError, возникающего при оценке слишком коротких слов
            try:
                # Сравнение последних двух слогов
                if base_word_in_list[-1] == word_in_list[-1] and base_word_in_list[-2] == word_in_list[-2]:
                    # Добавление рифмы в список
                    rhymes_list.append(w)
                else:
                    # Сравнение последнего слога и двух предпоследних букв
                    if base_word_in_list[-1] == word_in_list[-1] and word[-2] == y[-2] and word[-3] == y[-3]:
                        # Добавление рифмы в список
                        rhymes_list.append(w)
                # Блок сработает при пустом списке рифм
                if not rhymes_list:
                    # Сравнение 4х последних букв
                    if word[-1] == y[-1] and word[-2] == y[-2] and word[-3] == y[-3] and word[-4] == y[-4]:
                        # Добавление рифмы в список
                        rhymes_list.append(w)
                # Блок сработает при пустом списке рифм
                if not rhymes_list:
                    # Сравнение 3х последних букв
                    if word[-1] == y[-1] and word[-2] == y[-2] and word[-3] == y[-3]:
                        # Добавление рифмы в список
                        rhymes_list.append(w)
            except IndexError:
                continue
    # Проверка на прямое исполнение
    if __name__ == '__main__':
        # Проверка на пустоту списка рифм
        if rhymes_list:
            # Результат функции - случайная рифма
            return choice(rhymes_list)
        else:
            return 'не нашел=('
    else:
        # Результат функции - список с рифмами
        return rhymes_list


# Проверка на прямое исполнение
if __name__ == '__main__':
    # Открытие словарных баз
    WORDS_ = codecs.open('words.txt', 'r', 'ANSI')
    ACTIVE_ = codecs.open('active.txt', 'r', 'ANSI')
    NAME_ = codecs.open('name.txt', 'r', 'UTF-8')
    ADJECTIVE_ = codecs.open('adjective.txt', 'r', 'ANSI')
    # Хранит введенное пользователем слово (для подбора рифмы)
    input_word = input('введите слово для рифмовки')
    # Вывод случайной рифмы
    print(rhyme(input_word, WORDS_, ACTIVE_, NAME_, ADJECTIVE_))
    # Закрытие файлов со словарными базами
    WORDS_.close()
    ACTIVE_.close()
    NAME_.close()
    ADJECTIVE_.close()
