# 12.45. Формирование строки из заданного количества одинаковых символов
def task_12_45():
    symbol = input("Введите символ: ")
    count = int(input("Введите количество символов: "))
    result = symbol * count
    print("Результат:", result)

# 12.46. Добавить к слову в начале четыре '+' и в конце пять '-'
def task_12_46():
    word = input("Введите слово: ")
    result = '++++' + word + '-----'
    print("Результат:", result)

# 12.47. Добавить к слову столько '*' в начале и конце, сколько букв в слове
def task_12_47():
    word = input("Введите слово: ")
    stars = '*' * len(word)
    result = stars + word + stars
    print("Результат:", result)

# 12.48. Заменить соответствующее количество символов во втором слове на первое слово
def task_12_48():
    word1 = input("Введите первое слово (длиннее второго): ")
    word2 = input("Введите второе слово: ")
    length = len(word1)
    if len(word2) >= length:
        result = word1 + word2[length:]
    else:
        # Если второе слово короче, заменяем всё и дописываем остаток
        result = word1 + ''
    print("Результат:", result)

# 12.49. Вывести все буквы 'и' в предложении
def task_12_49():
    sentence = input("Введите предложение: ")
    letters_i = [ch for ch in sentence if ch == 'и']
    print("Все 'и':", ''.join(letters_i))

# 12.50. Вывести символы предложения по одному, если символ - определенный (например, 'а')
def task_12_50():
    sentence = input("Введите предложение: ")
    symbol = input("Введите символ для поиска: ")
    for ch in sentence:
        if ch == symbol:
            print(ch)

# 12.51. Вывести третий, шестой и т. д. символы
def task_12_51():
    sentence = input("Введите предложение: ")
    for i in range(2, len(sentence), 3):
        print(sentence[i])

# 12.52. Вывести все буквы 'м' и 'н'
def task_12_52():
    sentence = input("Введите предложение: ")
    result = [ch for ch in sentence if ch in ('м', 'н')]
    print("М и н:", ''.join(result))

# 12.53. В предложении найти все вхождения двух символов
def task_12_53():
    sentence = input("Введите предложение: ")
    ch1 = input("Введите первый символ: ")
    ch2 = input("Введите второй символ: ")
    positions_ch1 = [i for i, ch in enumerate(sentence) if ch == ch1]
    positions_ch2 = [i for i, ch in enumerate(sentence) if ch == ch2]
    print(f"Позиции '{ch1}':", positions_ch1)
    print(f"Позиции '{ch2}':", positions_ch2)

# 12.54. Вывести все вхождения 'нн'
def task_12_54():
    sentence = input("Введите предложение: ")
    count = 0
    start = 0
    while True:
        idx = sentence.find('нн', start)
        if idx == -1:
            break
        print(f"вхождение на позиции {idx}")
        start = idx + 1
        count +=1
    if count == 0:
        print("Нет вхождений 'нн'.")

# 12.55. Вывести каждый второй символ (на чётных позициях)
def task_12_55():
    sentence = input("Введите предложение: ")
    for i in range(1, len(sentence), 2):
        print(sentence[i])

# 12.56. Вывести символы по указанным номерам
def task_12_56():
    sentence = input("Введите предложение: ")
    indices = [1, 2, 5, 6, 9, 10]
    for i in indices:
        if i - 1 < len(sentence):
            print(sentence[i - 1])

# 12.57. Подсчитать количество букв 'о'
def task_12_57():
    sentence = input("Введите предложение: ")
    count = sum(1 for ch in sentence if ch == 'о')
    print("Количество 'о':", count)

# 12.58. Посчитать пробелы
def task_12_58():
    sentence = input("Введите предложение: ")
    count = sentence.count(' ')
    print("Количество пробелов:", count)

# 12.59. Подсчитать вхождения символа
def task_12_59():
    sentence = input("Введите предложение: ")
    symbol = input("Введите символ для подсчёта: ")
    count = sentence.count(symbol)
    print(f"Вхождения '{symbol}':", count)

# 12.60. Вычислить долю (в %) букв 'а'
def task_12_60():
    sentence = input("Введите предложение: ")
    total_letters = sum(1 for ch in sentence if ch.isalpha())
    count_a = sum(1 for ch in sentence if ch == 'а')
    if total_letters > 0:
        percentage = (count_a / total_letters) * 100
        print(f"Доля 'а': {percentage:.2f}%")
    else:
        print("В предложении нет букв.")

# 12.61. Подсчитать встречания '+' и '*'
def task_12_61():
    text = input("Введите текст: ")
    count_plus = text.count('+')
    count_star = text.count('*')
    print(f" '+' встречается {count_plus} раз(а).")
    print(f" '*' встречается {count_star} раз(а).")

# 12.62. Посчитать соседние одинаковые буквы
def task_12_62():
    sentence = input("Введите предложение: ")
    count = sum(1 for i in range(len(sentence)-1) if sentence[i] == sentence[i+1])
    print("Количество соседних одинаковых букв:", count)

# 12.63. Вхождения определенных буквосочетаний
def task_12_63():
    sentence = input("Введите предложение: ")
    substr1 = "ро"
    substr2 = input("Введите буквосочетание для второго варианта: ")
    substr3 = input("Введите третье буквосочетание: ")
    count1 = sentence.count(substr1)
    count2 = sentence.count(substr2)
    count3 = sentence.count(substr3)
    print(f"Вхождения '{substr1}':", count1)
    print(f"Вхождения '{substr2}':", count2)
    print(f"Вхождения '{substr3}':", count3)

# 12.64. Подсـчет слов, разделённых одним пробелом
def task_12_64():
    sentence = input("Введите предложение: ").strip()
    if sentence:
        words = sentence.split()
        print("Количество слов:", len(words))
    else:
        print("Нет слов.")

# 12.65. Подсчет слов, разделённых пробелами (с учётом начальных и конечных пробелов)
def task_12_65():
    sentence = input("Введите предложение: ")
    words = sentence.strip().split()
    print("Количество слов:", len(words))

# 12.66. Количество вхождений '+' и '-' в текст
def task_12_66():
    text = input("Введите текст: ")
    count_plus = text.count('+')
    count_minus = text.count('-')
    print(f" '+' встречается {count_plus} раз(а).")
    print(f" '-' встречается {count_minus} раз(а).")

# 12.67. Количество предложений в тексте (по точкам)
def task_12_67():
    text = input("Введите текст: ")
    sentences = [s for s in text.split('.') if s.strip()]
    print("Количество предложений:", len(sentences))

# 12.68. Определить количество гласных буквы в предложении
def count_vowels(sentence):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(ch in vowels for ch in sentence)

# 12.69. Определить, какая буква встречается чаще – о или а
def compare_o_a(sentence):
    o_count = sentence.lower().count('о')
    a_count = sentence.lower().count('а')
    if o_count > a_count:
        return 'о'
    elif a_count > o_count:
        return 'а'
    else:
        return 'равно'

# 12.70. Проверить наличие запятых в предложении
def has_commas(sentence):
    return ',' in sentence

# 12.71. Проверить, больше ли слов чем три
def more_than_three_words(sentence):
    words = sentence.strip().split()
    return len(words) > 3

# 12.72. Определить, какая буква – с или т – встречается позже
def last_c_or_t(sentence):
    words = sentence.split()
    last_c = -1
    last_t = -1
    for idx, word in enumerate(words):
        for ch_idx, ch in enumerate(word):
            if ch.lower() == 'с':
                last_c = idx
            elif ch.lower() == 'т':
                last_t = idx
    if last_c > last_t:
        return 'с'
    elif last_t > last_c:
        return 'т'
    else:
        return 'равно'  # или тоже, если ни одной буквы не найдена

# 12.73. Проверить, есть ли пять идущих подряд одинаковых символов
def five_consecutive_chars(text):
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

# 12.74. Напечатать символы перед первой запятой
def chars_before_comma(sentence, comma_exists=True):
    if comma_exists:
        index = sentence.find(',')
        if index != -1:
            return sentence[:index]
        else:
            return ''
    else:
        return sentence

# 12.75. Первое слово при двух пробелах между словами
def first_word_double_space(sentence):
    words = sentence.split('  ')  # двойной пробел
    return words[0] if words else ''

# 12.76. Последнее слово
def last_word(sentence):
    words = sentence.strip().split()
    return words[-1] if words else ''

# 12.77. Первое, второе и третье слова при двух пробелах
def first_three_words(sentence):
    words = sentence.split('  ')  # двойной пробел
    return words[:3]

# 12.78. два последних слова
def last_two_words(sentence):
    words = sentence.split()
    return words[-2:] if len(words) >= 2 else []

# 12.79. первые 6 слов с использованием цикла
def first_six_words(sentence):
    words = sentence.split()
    return words[:6]

# 12.80. Разобрать путь файла по символу '\'
def split_path(path):
    parts = path.split('\\')
    return parts

def main():
    print("Введите все задачи по порядку:")

    # 12.68
    sentence = input("Задача 12.68: Введите предложение: ")
    print("Количество гласных:", count_vowels(sentence))

    # 12.69
    sentence = input("Задача 12.69: Введите предложение: ")
    print("Больше встречается буква:", compare_o_a(sentence))

    # 12.70
    sentence = input("Задача 12.70: Введите предложение: ")
    print("Присутствуют запятые?" , "Да" if has_commas(sentence) else "Нет")

    # 12.71
    sentence = input("Задача 12.71: Введите предложение: ")
    print("Больше трех слов:" , "Да" if more_than_three_words(sentence) else "Нет")

    # 12.72
    sentence = input("Задача 12.72: Введите предложение: ")
    print("Лучшая буква:", last_c_or_t(sentence))

    # 12.73
    text = input("Задача 12.73: Введите текст: ")
    print("Есть пять подряд одинаковых символов?", "Да" if five_consecutive_chars(text) else "Нет")

    # 12.74
    sentence = input("Задача 12.74: Введите предложение: ")
    # Предполагаем, что запятые есть
    print("Символы перед первой запятой:", chars_before_comma(sentence, True))
    # Если запятых нет, выдаст пустую строку
    # Можно проверить наличие запятых
    if has_commas(sentence):
        print("Символы перед первой запятой:", chars_before_comma(sentence))
    else:
        print("Запятых в предложении нет.")

    # 12.75
    sentence = input("Задача 12.75: Введите предложение с двойными пробелами: ")
    print("Первое слово:", first_word_double_space(sentence))

    # 12.76
    sentence = input("Задача 12.76: Введите предложение: ")
    print("Последнее слово:", last_word(sentence))

    # 12.77
    sentence = input("Задача 12.77: Введите предложение с не менее четырьмя словами, разделенными двумя пробелами: ")
    print("первое, второе и третье слова:", first_three_words(sentence))

    # 12.78
    sentence = input("Задача 12.78: Введите предложение: ")
    print("Два последних слова:", last_two_words(sentence))

    # 12.79
    sentence = input("Задача 12.79: Введите предложение с не менее семью словами: ")
    print("Первые 6 слов:", first_six_words(sentence))

    # 12.80
    path = input("Задача 12.80: Введите полный путь файла: ")
    parts = split_path(path)
    print("Разделенные части:")
    for part in parts:
        print(part)

if __name__ == "__main__":
    main()