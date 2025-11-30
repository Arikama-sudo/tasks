import random

def inputlist(prompt):
    s = input(prompt).strip()
    if s == '':
        return []
    try:
        return [int(x) for x in s.split()]
    except ValueError:
        print("Ошибка: вводите целые числа через пробел.")
        return inputlist(prompt)

def preparefourlists():
    print("Ввод четырёх списков. Для использования примера оставьте строку пустой и нажмите Enter.")
    lists = []
    for i in range(1, 5):
        lst = inputlist(f"List {i} (числа через пробел, пустая строка = пример): ")
        if not lst:
            lst = [random.randint(0, 20) for i in range(random.randint(3, 7))]
            print(f"  -> Используется пример: {lst}")
        lists.append(lst)
    return lists

def mergeall(lists):
    res = []
    for lst in lists:
        res.extend(lst)
    return res

def linearsearch(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

def uniqueelementsacrosslists(lists):
    sets = [set(lst) for lst in lists]
    counts = {}
    for s in sets:
        for v in s:
            counts[v] = counts.get(v, 0) + 1
    return [v for v, c in counts.items() if c == 1]

def binarysearch(lst, value):
    n = len(lst)
    if n == 0:
        return -1
    asc = True
    if n > 1:
        asc = lst[0] <= lst[-1]
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == value:
            return mid
        if asc:
            if value < lst[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if value > lst[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1

def asksortorder():
    while True:
        s = input("Сортировать по возрастанию? (Y/N) [Y]: ").strip().upper()
        if s == '' or s == 'Y':
            return True
        if s == 'N':
            return False
        print("Введите Y или N.")

def task1():
    print("\n--- Задание 1: объединить 4 списка, сортировка, линейный поиск ---")
    lists = preparefourlists()
    print("\nИсходные списки:")
    for i, lst in enumerate(lists, 1):
        print(f" List{i}: {lst}")
    merged = mergeall(lists)
    print("\nОбъединённый (до сортировки):", merged)
    asc = asksortorder()
    merged.sort(reverse=not asc)
    print("Объединённый (после сортировки):", merged)
    try:
        v = int(input("Введите целое значение для линейного поиска: ").strip())
    except ValueError:
        print("Неверный ввод, отменено.")
        return
    idxs = linearsearch(merged, v)
    if idxs:
        print(f"Найдено {len(idxs)} вхождений. Индексы (0-based): {idxs}")
    else:
        print("Значение не найдено.")

def task2():
    print("\n--- Задание 2: уникальные элементы (присутствуют ровно в одном списке), сортировка, бинарный поиск ---")
    lists = preparefourlists()
    print("\nИсходные списки:")
    for i, lst in enumerate(lists, 1):
        print(f" List{i}: {lst}")
    uniques = uniqueelementsacrosslists(lists)
    print("\nЭлементы, присутствующие ровно в одном списке (без повторов):", uniques)
    asc = asksortorder()
    uniques.sort(reverse=not asc)
    print("Результирующий список после сортировки:", uniques)
    try:
        v = int(input("Введите целое значение для бинарного поиска: ").strip())
    except ValueError:
        print("Неверный ввод, отменено.")
        return
    pos = binarysearch(uniques, v)
    if pos != -1:
        print(f"Значение найдено в позиции {pos} (0-based).")
    else:
        print("Значение не найдено.")

def main():
    while True:
        print("\nГлавное меню:")
        print(" 1 - Задание 1")
        print(" 2 - Задание 2")
        print(" 0 - Выход")
        c = input("> ").strip()
        if c == '0':
            break
        if c == '1':
            task1()
        elif c == '2':
            task2()
        else:
            print("Выберите 0, 1 или 2.")

if __name__ == "__main__":
    main()