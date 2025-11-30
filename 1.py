#1
def readlast(lines, filename):
    try:
        lines = int(lines)
        if lines <= 0:
            print("Аргумент lines должен быть положительным целым числом.")
            return
    except ValueError:
        print("Аргумент lines должен быть целым числом.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден:", filename)
        return

    to_print = all_lines[-lines:] if lines <= len(all_lines) else all_lines
    for line in to_print:
        print(line.rstrip('\n'))


#2
def extract_long_words(src, dst, min_len=7):
    pattern = re.compile(r"[A-Za-zА-Яа-яЁё]+", re.UNICODE)
    try:
        with open(src, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден:", src)
        return

    words = pattern.findall(text)
    longwords = [w for w in words if len(w) >= minlen]
    try:
        with open(dst, 'w', encoding='utf-8') as out:
            for w in longwords:
                out.write(w + '\n')
        print(f"Записано {len(longwords)} слов в файл {dst}.")
    except Exception as e:
        print("Ошибка записи:", e)


#3
def copypreservepositions(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден:", src)
        return

    try:
        with open(dst, 'w', encoding='utf-8') as out:
            out.writelines(lines)
        print(f"Файл {src} скопирован в {dst}.")
    except Exception as e:
        print("Ошибка записи:", e)


# 4
def reversecopy(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден:", src)
        return

    try:
        with open(dst, 'w', encoding='utf-8') as out:
            out.writelines(reversed(lines))
        print(f"Файл {src} записан в {dst} в обратном порядке.")
    except Exception as e:
        print("Ошибка записи:", e)


#5
def insertasterisksafterlastnocomma(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден:", filename)
        return

    lastindex = None
    for i, line in enumerate(lines):
        if ',' not in line:
            lastindex = i

    insertline = '',  12 + '\n'
    if lastindex is None:
        lines.append(insertline)
        msg = "Добавлено в конец файла."
    else:
        lines.insert(lastindex + 1, insertline)
        msg = f"Вставлено после строки {lastindex + 1} (1-based index)."

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(msg)
    except Exception as e:
        print("Ошибка записи:", e)


#6
def countwordsstartingwith(filename, ch):
    if not ch:
        print("Пустой символ.")
        return
    ch = ch[0].lower()
    pattern = re.compile(r"[A-Za-zА-Яа-яЁё]+", re.UNICODE)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден:", filename)
        return
    words = pattern.findall(text)
    count = sum(1 for w in words if w[0].lower() == ch)
    print(f"Слов, начинающихся с '{ch}': {count}")
    return count


#7
def replacestarwithampersand(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл не найден:", src)
        return
    newcontent = content.replace('', '&')
    try:
        with open(dst, 'w', encoding='utf-8') as out:
            out.write(newcontent)
        print(f"Заменено '*' -> '&' и записано в {dst}.")
    except Exception as e:
        print("Ошибка записи:", e)


#8
def writearraytofile(arr, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for item in arr:
                f.write(str(item) + '\n')
        print(f"Записано {len(arr)} строк в {filename}.")
    except Exception as e:
        print("Ошибка записи:", e)


# 9
def count_chars(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл не найден:", filename)
        return
    total = len(content)
    print(f"Количество символов в файле {filename}: {total}")
    return total


# 10
def countlines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            num = sum(1 for i in f)
    except FileNotFoundError:
        print("Файл не найден:", filename)
        return
    print(f"Количество строк в файле {filename}: {num}")
    return num


#11
def menu():
    while True:
        print("\nВыберите задачу (1-10) или 0 для выхода:")
        print("1. readlast(lines, file)")
        print("2. Вытащить слова >=7 букв из файла")
        print("3. Копировать файл (строка в строку)")
        print("4. Копировать файл в обратном порядке")
        print("5. Вставить '************' после последней строки без запятой")
        print("6. Подсчитать слова, начинающиеся с символа")
        print("7. Заменить '*' на '&' при копировании")
        print("8. Записать массив строк в файл")
        print("9. Подсчитать количество символов в файле")
        print("10. Подсчитать количество строк в файле")
        print("0. Выход")
        choice = input("> ").strip()
        if choice == '0':
            print("До свидания.")
            break
        if choice == '1':
            ln = input("Сколько последних строк вывести? ")
            fn = input("Имя файла: ")
            readlast(ln, fn)
        elif choice == '2':
            src = input("Исходный файл: ")
            dst = input("Файл для результата: ")
            extractlongwords(src, dst)
        elif choice == '3':
            src = input("Исходный файл: ")
            dst = input("Файл-приёмник: ")
            copypreservepositions(src, dst)
        elif choice == '4':
            src = input("Исходный файл: ")
            dst = input("Файл-приёмник: ")
            reversecopy(src, dst)
        elif choice == '5':
            fn = input("Имя файла: ")
            insertasterisksafterlastnocomma(fn)
        elif choice == '6':
            fn = input("Имя файла: ")
            ch = input("С каким символом (один символ): ")
            countwordsstartingwith(fn, ch)
        elif choice == '7':
            src = input("Исходный файл: ")
            dst = input("Файл-приёмник: ")
            replacestarwithampersand(src, dst)
        elif choice == '8':
            arrinput = input("Ввод элементов через запятую: ")
            arr = [s.strip() for s in arrinput.split(',')]
            fn = input("Имя файла для записи: ")
            writearraytofile(arr, fn)
        elif choice == '9':
            fn = input("Имя файла: ")
            countchars(fn)
        elif choice == '10':
            fn = input("Имя файла: ")
            count_lines(fn)
        else:
            print("Неверный выбор. Введите число от 0 до 10.")


if __name__ == '__main__':
    menu()