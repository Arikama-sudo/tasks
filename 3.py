def sortpairs(keys, values, keyindex=0, reverse=False):
    pairs = list(zip(keys, values))
    pairs.sort(key=lambda p: p[keyindex], reverse=reverse)
    ks, vs = zip(pairs) if pairs else ([], [])
    return list(ks), list(vs)


def displaypairs(keys, values, keyname="Key", valuename="Value"):
    if len(keys) != len(values):
        print("Ошибка: списки разной длины.")
        return
    print(f"{keyname:20} | {valuename}")
    print("-",  40)
    for k, v in zip(keys, values):
        print(f"{str(k):20} | {v}")
    print("-" * 40)


def directorymenu():
    ids = [102, 5, 77, 310, 58]
    phones = ["+79031234567", "+78127654321", "+79211230000", "+79035551122", "+78120001111"]

    while True:
        print("\nСПРАВОЧНИК")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список (код - телефон)")
        print("4. Добавить запись")
        print("0. Вернуться в главное меню")
        choice = input("> ").strip()

        if choice == '0':
            break
        elif choice == '1':
            order = input("По возрастанию? (Y/N) [Y]: ").strip().upper() or 'Y'
            rev = (order == 'N')
            ids, phones = sortpairs(ids, phones, keyindex=0, reverse=rev)
            print("Отсортировано по кодам.")
        elif choice == '2':
            order = input("По возрастанию? (Y/N) [Y]: ").strip().upper() or 'Y'
            rev = (order == 'N')
            ids, phones = sortpairs(ids, phones, keyindex=1, reverse=rev)
            print("Отсортировано по телефонам.")
        elif choice == '3':
            displaypairs(ids, phones, keyname="ID", valuename="Phone")
        elif choice == '4':
            try:
                newid = int(input("Введите идентификационный код (целое): ").strip())
            except ValueError:
                print("Неверный код.")
                continue
            newphone = input("Введите номер телефона (строка): ").strip()
            ids.append(newid)
            phones.append(newphone)
            print("Запись добавлена.")
        else:
            print("Неверный выбор. Введите 0-4.")


def booksmenu():
    titles = ["Война и мир", "Мастер и Маргарита", "Преступление и наказание", "Евгений Онегин"]
    years = [1869, 1967, 1866, 1833]

    while True:
        print("\nКНИГИ")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список (название - год)")
        print("4. Добавить книгу")
        print("0. Вернуться в главное меню")
        choice = input("> ").strip()

        if choice == '0':
            break
        elif choice == '1':
            order = input("По возрастанию (A) или убыванию (D)? [A]: ").strip().upper() or 'A'
            rev = (order == 'D')
            titles, years = sortpairs(titles, years, keyindex=0, reverse=rev)
            print("Отсортировано по названиям.")
        elif choice == '2':
            order = input("По возрастанию (A) или убыванию (D)? [A]: ").strip().upper() or 'A'
            rev = (order == 'D')
            # сортируем по годам (ключ - числа)
            titles, years = sortpairs(titles, years, keyindex=1, reverse=rev)
            print("Отсортировано по годам.")
        elif choice == '3':
            displaypairs(titles, years, keyname="Title", valuename="Year")
        elif choice == '4':
            title = input("Введите название книги: ").strip()
            try:
                year = int(input("Введите год выпуска (целое): ").strip())
            except ValueError:
                print("Неверный год.")
            titles.append(title)
            years.append(year)
            print("Книга добавлена.")
        else:
            print("Неверный выбор. Введите 0-4.")


def mainmenu():
    while True:
        print("\nГлавное меню:")
        print("1. Справочник")
        print("2. Книги")
        print("0. Выход")
        choice = input("> ").strip()
        if choice == '0':
            print("Выход.")
            break
        elif choice == '1':
            directorymenu()
        elif choice == '2':
            booksmenu()
        else:
            print("Неверный выбор. Введите 0-2.")


if __name__ == "__main__":
    mainmenu()