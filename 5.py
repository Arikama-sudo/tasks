# #Практика 1
# #1
# import random
# from typing import List, Optional
#
# class Number:
#     def __init__(self, n: int, low: int = -10, high: int = 10, seed: Optional[int] = None, nums: Optional[List[int]] = None):
#         if nums is not None:
#             self.nums = list(nums)
#         else:
#             if seed is not None:
#                 random.seed(seed)
#             self.nums = [random.randint(low, high) for i in range(n)]
#
#     def processed(self) -> List[int]:
#         a = self.nums[:]
#         n = len(a)
#         if n == 0:
#             return a
#         mean = sum(a) / n
#         if mean > 0:
#             k = (2 * n) // 3
#         else:
#             k = n // 3
#         prefix = a[:k]
#         rest = a[k:]
#         prefix ,i, sorted = sorted(prefix)
#         rest ,i, reversed = rest[::-1]
#         return prefix ,i, sorted + rest_reversed
#
#     def __str__(self):
#         return str(self.nums)
#
# if __name__ == "__main__":
#     obj = Number(n=10, low=-5, high=10, seed=1)
#     print("Исходный список:", obj)
#     result = obj.processed()
#     print("Обработанный список:", result)
# #2
# def input_grade(prompt="Введите оценку (1..12): "):
#     while True:
#         try:
#             v = int(input(prompt))
#             if 1 <= v <= 12:
#                 return v
#             else:
#                 print("Оценка должна быть от 1 до 12.")
#         except ValueError:
#             print("Нужно ввести целое число.")
#
#
# def main_academic():
#     print("Вводите 10 оценок студента (от 1 до 12).")
#     grades = []
#     for i in range(10):
#         g = input_grade(f"Оценка #{i + 1}: ")
#         grades.append(g)
#
#     while True:
#         print("\nМеню:")
#         print("1. Вывести оценки")
#         print("2. Пересдача (заменить оценку)")
#         print("3. Проверить, выходит ли стипендия (avg >= 10.7)")
#         print("4. Вывести отсортированный список оценок")
#         print("5. Выход")
#         choice = input("Выберите пункт: ").strip()
#         if choice == "1":
#             print("Оценки:", grades)
#         elif choice == "2":
#             try:
#                 idx = int(input("Введите номер оценки для замены (1..10): "))
#             except ValueError:
#                 print("Неверный ввод.")
#                 continue
# if not (1 <= idx <= 10):
#     print("Номер должен быть от 1 до 10.")
# newg = input_grade("Новая оценка (1..12): ")
# grades[idx - 1] = newg
# print("Оценка заменена.")
# if choice == "3":
#  avg = sum(grades) / len(grades)
# print(f"Средний балл = {avg:.2f}")
# if avg >= 10.7:
#     print("Стипендия выходит.")
# else:
#     print("Стипендия не выходит.")
# if choice == "4":
#    order = input("По возрастанию (a) или убыванию (d)? [a/d]: ").strip().lower()
# if order == "d":
#     print("Оценки (убывание):", sorted(grades, reverse=True))
# else:
#     print("Оценки (возрастание):", sorted(grades))
# if choice == "5":
#     print("Выход.")
# else:
#     print("Неверный пункт меню.")
#
# if __name__ == "__main__":
#     mainacademic()
# #3
# from typing import List, Tuple
#
# def improvedbubblesort(arr: List[int]) -> Tuple[List[int], int]:
#     a = arr[:]
#     n = len(a)
#     passes = 0
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#                 swapped = True
#         passes += 1
#         if not swapped:
#             break
#     return a, passes
#
# if __name__ == "__main__":
#     data = [5, 1, 4, 2, 8, 0, -1, 3]
#     print("Исходный:", data)
#     sorteddata, passes = improvedbubblesort(data)
#     print("Отсортированный:", sorteddata)
#     print("Проходов выполнено:", passes)
# #Практика2
# #1
# import random
#
# def generate i ,sample</i>directory(n=6, seed=None):
#     if seed is not None:
#         random.seed(seed)
#     ids = [random.randint(1000, 9999) for <i> in range(n)]
#     phones = [random.randint(7000000000, 7999999999) for </i> in range(n)]  # пример 10-значных номеров
#     return ids, phones
#
# def print<i>directory(ids, phones):
#     print("\nСправочник (индекс: ID -> Телефон):")
#     for i, (idd, ph) in enumerate(zip(ids, phones), 1):
#         print(f"{i}: {idd} -> {ph}")
#     print()
#
# def sort</i>by<i>ids(ids, phones, reverse=False):
#     pairs = list(zip(ids, phones))
#     pairs.sort(key=lambda x: x[0], reverse=reverse)
#     ids</i>sorted, phones<i>sorted = zip(<i>pairs) if pairs else ([], [])
#     return list(ids</i>sorted), list(phones<i>sorted)
#
# def sort</i>by<i>phones(ids, phones, reverse=False):
#     pairs = list(zip(ids, phones))
#     pairs.sort(key=lambda x: x[1], reverse=reverse)
#     ids</i>sorted, phones<i>sorted = zip(</i>pairs) if pairs else ([], [])
#     return list(ids</i>sorted), list(phones<i>sorted)
#
# def run</i>directory():
#     ids, phones = generate<i>sample</i>directory(n=6, seed=1)
#     while True:
#         print("Меню — Справочник:")
#         print("1. Отсортировать по идентификационным кодам (по возрастанию)")
#         print("2. Отсортировать по номерам телефона (по возрастанию)")
#         print("3. Вывести список пользователей с кодами и телефонами")
#         print("4. Выход")
#         choice = input("Выберите пункт: ").strip()
#         if choice == "1":
#             ids, phones = sort<i>by</i>ids(ids, phones)
#             print("Отсортировано по идентификаторам.")
#             print<i>directory(ids, phones)
#         elif choice == "2":
#             ids, phones = sort</i>by<i>phones(ids, phones)
#             print("Отсортировано по номерам телефона.")
#             print</i>directory(ids, phones)
#         elif choice == "3":
#             print_directory(ids, phones)
#         elif choice == "4":
#             print("Выход из справочника.")
#             break
#         else:
#             print("Неверный выбор. Повторите.")
#
# if __name__ == "__main__":
#     run<i>directory()
#2
# def samplebooks():
#     titles = [
#         "Война и мир",
#         "Мастер и Маргарита",
#         "Преступление и наказание",
#         "Отцы и дети",
#         "Евгений Онегин"
#     ]
#     years = [1869, 1967, 1866, 1862, 1833]
#     return titles, years
#
#
# def printbooks(titles, years):
#     print("\nСписок книг (индекс: Название — Год):")
#     for i, (t, y) in enumerate(zip(titles, years), 1):
#         print(f"{i}: «{t}» — {y}")
#     print()
#
#
# def sortby_title(titles, years, reverse=False):
#     pairs = list(zip(titles, years))
#
# pairs.sort(key=lambda x: x[0].lower(), reverse=reverse)
# titless, yearss = zip(pairs) if pairs else ([], [])
# return list(titles), list(years)
#
#
# def sortbyyear(titles, years, reverse=False):
#     pairs = list(zip(titles, years))
#     pairs.sort(key=lambda x: x[1], reverse=reverse)
#     titless, yearss = zip(pairs) if pairs else ([], [])
#     return list(titless), list(yearss)
#
#
# def runbooks():
#     titles, years = samplebooks()
#     while True:
#         print("Меню — Книги:")
#         print("1. Отсортировать по названию книг (А→Я)")
#         print("2. Отсортировать по годам выпуска (по возрастанию)")
#         print("3. Вывести список книг с названиями и годами выпуска")
#         print("4. Выход")
#         choice = input("Выберите пункт: ").strip()
#         if choice == "1":
#             titles, years = sortbytitle(titles, years)
#             print("Отсортировано по названию.")
#             printbooks(titles, years)
#         elif choice == "2":
#             titles, years = sortbyyear(titles, years)
#             print("Отсортировано по годам выпуска.")
#             printbooks(titles, years)
#         elif choice == "3":
#             print_books(titles, years)
#         elif choice == "4":
#             print("Выход из меню книг.")
#             break
#         else:
#             print("Неверный выбор. Повторите.")
#
#
# if __name__ == "__main__":
#     run_books()
#Практика3
#1
# def task1merge(lists: List[List[int]]) -> List[int]:
#     merged = []
#     for lst in lists:
#         merged.extend(lst)
#     return merged
#
# def linearsearch(arr: List[int], value: int) -> List[int]:
#     return [i for i, x in enumerate(arr) if x == value]
#
# def runtask1(lists: List[List[int]]):
#     print("== Задание 1: объединение и линейный поиск ==")
#     printlists(lists)
#     merged = task1merge(lists)
#     print("\nПятый (объединённый) список (до сортировки):")
#     print(merged)
#
#     choice = input("\nСортировать по возрастанию или убыванию? [a/u] (по умолчанию a): ").strip().lower()
#     if choice == 'u':
#         merged.sort(reverse=True)
#         order = "убывание"
#     else:
#         merged.sort()
#         order = "возрастание"
#     print(f"\nПятый список после сортировки ({order}):")
#     print(merged)
#     while True:
#         s = input("\nВведите целое значение для поиска (или пустая строка для возврата в меню): ").strip()
#         if s == "":
#             break
#         try:
#             val = int(s)
#         except ValueError:
#             print("Нужно ввести целое число.")
#             continue
#         indices = linearsearch(merged, val)
#         if indices:
#             print(f"Значение {val} найдено в {len(indices)} позициях (0-based индексы): {indices}")
#         else:
#             print(f"Значение {val} в списке не найдено.")
#2

# def uniqueacross_lists(lists: List[List[int]]) -> List[i]:
# sets = [set(lst) for lst in lists]
# allcandidates = set().union(*sets)
# uniqueelements = []
# for x in allcandidates:
#     countpresence = sum(1 for s in sets if x in s)
#     if countpresence == 1:
#         uniqueelements.append(x)
# return uniqueelements
#
#
# def binarysearch(arr: List[int], target: int, ascending: bool = True) -> int:
#     lo, hi = 0, len(arr) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         mid_val = arr[mid]
#         if mid_val == target:
#             return mid
#         if ascending:
#             if mid_val < target:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         else:
#             if mid_val > target:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#     return -1
#
#
# def runtask2(lists: List[List[int]]):
#     print("== Задание 2: уникальные элементы между списками и бинарный поиск ==")
#     printlists(lists)
#     uniqueelems = uniqueacrosslists(lists)
#     print("\nЭлементы, уникальные для одного списка (до сортировки):")
#     print(uniqueelems)
#     choice = input("\nСортировать по возрастанию или убыванию? [a/u] (по умолчанию a): ").strip().lower()
#     if choice == 'u':
#         uniqueelems.sort(reverse=True)
#         ascending = False
#         order = "убывание"
#     else:
#         uniqueelems.sort()
#         ascending = True
#         order = "возрастание"
#     print(f"\nРезультирующий пятый список после сортировки ({order}):")
#     print(uniqueelems)
#
#     while True:
#         s = input("\nВведите целое значение для бинарного поиска (или пустая строка для возврата в меню): ").strip()
#         if s == "":
#             break
#         try:
#             val = int(s)
#         except ValueError:
#             print("Нужно ввести целое число.")
#             continue
#         idx = binarysearch(uniqueelems, val, ascending=ascending)
#         if idx != -1:
#             print(f"Значение {val} найдено в позиции (0-based): {idx}")
#         else:
#             print(f"Значение {val} в списке не найдено.")
#
#
# def mainmenu():
#     lists = generatesamplelists(n=8, low=-5, high=15, seed=42)
#     while True:
#         print("\n=== Практика 3: меню ===")
#         print("1. Задание 1 — объединение 4 списков, сортировка, линейный поиск")
#         print("2. Задание 2 — уникальные элементы между списками, сортировка, бинарный поиск")
#         print("3. Показать текущие четыре списка")
#         print("4. Сгенерировать новые случайные списки")
#         print("5. Выйти")
# choice = input("Выберите пункт: ").strip()
# if choice == '1':
#     runtask1(lists)
# elif choice == '2':
#     runtask2(lists)
# elif choice == '3':
#     printlists(lists)
# elif choice == '4':
#     seedinput = input("Введите целое seed (или пустая строка для случайного): ").strip()
#     seed = None
#     if seedinput != "":
#         try:
#             seed = int(seedinput)
#         except ValueError:
#             print("Некорректный seed, будет использован None.")
#             seed = None
#     lists = generatesamplelists(n=8, low=-5, high=15, seed=seed)
#     print("Сгенерированы новые списки.")
# elif choice == '5':
#     print("Выход.")
#     break
# else:
#     print("Неверный выбор. Попробуйте ещё раз.")
#
# if __name__ == "__main__":
#     main_menu()
#Практика4
# import random
# from typing import List, Optional
#
#
# def bubblesort(arr: List[int]) -> List[int]:
#     a = arr[:]
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
#
#
# def insertionsort(arr: List[int]) -> List[int]:
#     a = arr[:]
#     for i in range(1, len(a)):
#         key = a[i]
#         j = i - 1
#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j + 1] = key
#     return a
#
#
# def halfsort(arr: List[int]) -> List[int]:
#     n = len(arr)
#     k = n // 2
#     first = sorted(arr[:k], reverse=True)
#     second = sorted(arr[k:])
#     return first + second
#
#
# def mergesort(arr: List[int]) -> List[int]:
#     if len(arr) <= 1:
#         return arr[:]
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return _merge(left, right)
#
#
# def _merge(left: List[int], right: List[int]) -> List[int]:
#     res = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             res.append(left[i]);
#             i += 1
#         else:
#             res.append(right[j]);
#             j += 1
#     if i < len(left):
#         res.extend(left[i:])
#     if j < len(right):
#         res.extend(right[j:])
#     return res
#
#
# def parse_input_list(s: str) -> Optional[List[int]]:
#     s = s.strip()
#     if not s:
#         return None
#     parts = [p for p in s.replace(',', ' ').split()]
#     try:
#         return [int(p) for p in parts]
#     except ValueError:
#         return None
#
#
# def inputlistinteractive() -> List[int]:
#     while True:
#         s = input(
#             "Введите список целых (через пробел или запятую), или оставьте пустым для генерации случайного: ").strip()
#         if s == "":
#             n = input("Длина случайного списка (по умолчанию 10): ").strip()
#             try:
#                 n = int(n) if n else 10
#             except ValueError:
#                 n = 10
#             low = input("Минимальное значение (по умолчанию -20): ").strip()
#             high = input("Максимальное значение (по умолчанию 20): ").strip()
#             try:
#                 low = int(low) if low else -20
#
#
# high = int(high) if high else 20
# except ValueError:
# low, high = -20, 20
# seed = input("Seed для генерации (целое или пусто): ").strip()
# try:
#     seedval = int(seed) if seed else None
# except ValueError:
#     seedval = None
# if seedval is not None:
#     random.seed(seedval)
# return [random.randint(low, high) for in range(max(0, n))]
# else:
# lst = parseinputlist(s)
# if lst is None:
#     print("Неверный ввод. Введите целые числа через пробел или запятую.")
#     continue
# return lst
#
# def mainmenu():
#     print("Практика 4 — выбор задания")
#     while True:
#         print("\nВыберите задание:")
#         print("1. Пузырьковая сортировка")
#         print("2. Сортировка вставками")
#         print("3. Первая половина по убыванию, вторая по возрастанию")
#         print("4. Сортировка слиянием")
#         print("5. Выход")
#         choice = input("Пункт: ").strip()
#         if choice == '5':
#             print("Выход.")
#             break
#         if choice not in {'1', '2', '3', '4'}:
#             print("Неверный выбор.")
#             continue
#
#         arr = inputlistinteractive()
#         print("\nИсходный список:", arr)
#
#         if choice == '1':
#             sortedarr = bubblesort(arr)
#             print("После пузырьковой сортировки:", sortedarr)
#         elif choice == '2':
#             sortedarr = insertionsort(arr)
#             print("После сортировки вставками:", sortedarr)
#         elif choice == '3':
#             result = halfsort(arr)
#             print("После обработки (первая половина убывание, вторая — возрастание):", result)
#         elif choice == '4':
#             sortedarr = mergesort(arr)
#             print("После сортировки слиянием:", sortedarr)
#
#
# if __name__ == "__main__":
#     main_menu()
#Практика5
#1
# def shell<i>sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr
# #2
# def heapify(arr, n, i):
#     largest = i
#     l = 2 <i> i + 1
#     r = 2 </i> i + 2
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
# def heap<i>sort(arr):
#     n = len(arr)
#     # build max heap
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     # extract elements
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return arr
# #3
# import random
#
# def quick<i>sort(arr, lo=0, hi=None):
#     if hi is None:
#         hi = len(arr) - 1
#     if lo < hi:
#         p = random.randint(lo, hi)
#         arr[p], arr[hi] = arr[hi], arr[p]
#         pivot = arr[hi]
#         i = lo
#         for j in range(lo, hi):
#             if arr[j] <= pivot:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
#         arr[i], arr[hi] = arr[hi], arr[i]
#         quick_sort(arr, lo, i - 1)
#         quick_sort(arr, i + 1, hi)
#     return arr
# #4
# def flip(arr, k):
#     arr[:k] = arr[:k][::-1]
#
# def pancake<i>sort(arr):
#     n = len(arr)
#     flips = []
#     for curr</i>size in range(n, 1, -1):
#         max</i>idx = max(range(curr<i>size), key=lambda i: arr[i])
#         if max</i>idx == curr<i>size - 1:
#             continue
#         if max</i>idx != 0:
#             flip(arr, max<i>idx + 1)
#             flips.append(max</i>idx + 1)
#         flip(arr, curr<i>size)
#         flips.append(curr</i>size)
#     return flips, arr
#Практика6
# #1
# import random
#
# def linear<i>search(arr, target</i>str):
#     if not isinstance(target<i>str, str):
#         return "Требуется строка в качестве ввода."
#     try:
#         target = int(target</i>str)
#     except ValueError:
#         return "Строка не содержит целое число."
#     for i, v in enumerate(arr):
#         if v == target:
#             return f"Найдено на позиции {i} (индексация с 0)."
#     return "Не найдено."
#
# #2
# def binary<i>search(arr, target</i>str):
#     if not isinstance(target<i>str, str):
#         return "Требуется строка в качестве ввода."
#     try:
#         target = int(target</i>str)
#     except ValueError:
#         return "Строка не содержит целое число."
#     lo, hi = 0, len(arr) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if arr[mid] == target:
#             return f"Найдено на позиции {mid} (индексация с 0)."
#         elif arr[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return "Не найдено."
#
# #3
# class Soda:
#     def __init__(self, addition=None):
#         self.addition = addition
#
#     def show<i>my</i>drink(self):
#         if self.addition:
#             print(f"Газировка и {self.addition}")
#         else:
#             print("Обычная газировка")
#4
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def istriangle(self):
#         if not all(isinstance(x, (int, float)) for x in (self.a, self.b, self.c)):
#             return "Нужно вводить только числа!"
#         if not all(x > 0 for x in (self.a, self.b, self.c)):
#             return "С отрицательными числами ничего не выйдет!"
#         a, b, c = self.a, self.b, self.c
#         if a + b > c and a + c > b and b + c > a:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
#Практика7
#1
# class Animal:
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def __str__(self):
#         return f"{self.__class__.__name__} {self.nickname}"
#
# class Cat(Animal):
#     def voice(self):
#         print(f"{self.nickname}: Мяу!")
#
#     def run(self):
#         print("Побежали!")
#
# class Parrot(Animal):
#     def voice(self):
#         print(f"{self.nickname}: Привет!")
#
#     def fly(self):
#         print("Полетели!")
#2
# class Message:
#     def __init__(self, sender, recipient):
#         self.sender = sender
#         self.recipient = recipient
#
#     def showHeader(self):
#         print(f"От: {self.sender} -> Кому: {self.recipient}")
#
# class TextMessage(Message):
#     def __init__(self, sender, recipient, text):
#         super().__init__(sender, recipient)
#         self.text = text
#
#     def send(self):
#         self.showHeader()
#         print(self.text)
#
# class StickerMessage(Message):
#     def __init__(self, sender, recipient, sticker):
#         super().__init__(sender, recipient)
#         self.sticker = sticker
#         self.count = 1
#
#     def send(self):
#         self.showHeader()
#         print(f"{self.sticker} (отправлено: {self.count})")
#         self.count += 1
#
# stickers = [
#     "(‌ ◉‌‿◉ ‌)",
#     "ʕ •‌ ᴥ •‌ ʔっ",
#     "(ง︡‘-’ ︠ )ง",
#     "( ‌ •  ‌ʖ   ‌ •)",
#     "( ─‿‿─)"
# ]
# #3
# import random
#
# class MSDice:
#     def __init__(self, sides):
#         if sides < 1:
#             raise ValueError("Количество граней должно быть >= 1")
#         self.sides = sides
#         self.value = None
#
#     def roll(self):
#         self.value = random.randint(1, self.sides)
#         return self.value
#
#     def __str__(self):
#         return f"D{self.sides} (текущее значение: {self.value})"
#
# class D4(MSDice):
#     def __init__(self):
#         super().__init__(4)
#
# class D6(MSDice):
#     def __init__(self):
#         super().__init__(6)
#
# class D10(MSDice):
#     def __init__(self):
#         super().__init__(10)
#
# class D20(MSDice):
#     def __init__(self):
#         super().__init__(20)

#4
# class Player:
#     def __init__(self, nickname):
#         self.nickname = nickname
#         self.exp_points = 0
#         self.inventory = []
#
#     def __str__(self):
#         return f"{self.nickname}: {self.exp_points} очков опыта. Инвентарь: {self.inventory}"
#
#     def addExp(self, exp):
#         if not isinstance(exp, int):
#             raise ValueError("Очки опыта должны быть целым числом")
#         if exp < 0:
#             raise ValueError("Нельзя добавить отрицательный опыт")
#         self.exp_points += exp
#
#     def addItem(self, item):
#         self.inventory.append(item)
#
#     def removeItem(self, item):
#         try:
#             self.inventory.remove(item)
#         except ValueError:
#             pass
#5
#
# class resistors:
#     @staticmethod
#     def parallel(r1, r2):
#         if not (isinstance(r1, (int, float)) and isinstance(r2, (int, float))):
#             raise ValueError("Сопротивления должны быть числами")
#         if r1 <= 0 or r2 <= 0:
#             raise ValueError("Сопротивления должны быть положительными")
#         return 1 / (1 / r1 + 1 / r2)
#
#     @staticmethod
#     def consec(rlist):
#         if not isinstance(rlist, (list, tuple)):
#             raise ValueError("Ожидается список сопротивлений")
#         total = 0.0
#         for r in r_list:
#             if not isinstance(r, (int, float)):
#                 raise ValueError("Все элементы списка должны быть числами")
#             total += r
#         return total
#Практика8
#1
# from collections import Counter
# import math
# import statistics
#
# class SimpleStatistics:
#     def __init__(self, data):
#         if not isinstance(data, (list, tuple)):
#             raise ValueError("Ожидается список чисел")
#         self.data = list(data)
#         if len(self.data) == 0:
#             raise ValueError("Данные не должны быть пустыми")
#         if not all(isinstance(x, (int, float)) for x in self.data):
#             raise ValueError("Все элементы должны быть числами")
#
#     def mean(self):
#         return sum(self.data) / len(self.data)
#
#     def median(self):
#         return statistics.median(self.data)
#
#     def mode(self):
#         c = Counter(self.data)
#         maxfreq = max(c.values())
#         modes = [k for k,v in c.items() if v == maxfreq]
#         return modes if len(modes) > 1 else modes[0]
#
#     def range(self):
#         return max(self.data) - min(self.data)
#
#     def variance(self):
#         n = len(self.data)
#         if n < 2:
#             return 0.0
#         m = self.mean()
#         return sum((x - m)**2 for x in self.data) / (n - 1)
#
#     def standard_deviation(self):
#         return math.sqrt(self.variance())
#
# class FrequencyDistribution:
#     def __init__(self, data):
#         if not isinstance(data, (list, tuple)):
#             raise ValueError("Ожидается список данных")
#         self.data = list(data)
#         self.frequencies = None
#
#     def calculate_frequencies(self):
#         self.frequencies = dict(Counter(self.data))
#         return self.frequencies
#
#     def display_frequency_table(self):
#         if self.frequencies is None:
#             self.calculate_frequencies()
#         print("Элемент : Частота")
#         for item, freq in sorted(self.frequencies.items(), key=lambda kv: (-kv[1], str(kv[0]))):
#             print(f"{item} : {freq}")
#
#     def get_most_frequent(self):
#         if self.frequencies is None:
#             self.calculate_frequencies()
#         maxfreq = max(self.frequencies.values()) if self.frequencies else None
#         return [k for k,v in self.frequencies.items() if v == maxfreq] if maxfreq is not None else []
#2
# import numpy as np
# try:
#     from scipy import stats
# except Exception as e:
#     stats = None
#
# import matplotlib.pyplot as plt
#
# class Correlation:
#     def __init__(self, x, y):
#         if len(x) != len(y):
#             raise ValueError("Списки X и Y должны иметь одинаковую длину")
#         if len(x) < 2:
#             raise ValueError("Должно быть по крайней мере 2 наблюдения")
#         self.x = np.array(x, dtype=float)
#         self.y = np.array(y, dtype=float)
#
#     def pearson_correlation(self):
#         if stats is None:
#             raise ImportError("scipy is required for pearson_correlation")
#         r, p = stats.pearsonr(self.x, self.y)
#         return {"r": r, "p_value": p}
#
#     def spearman_correlation(self):
#         if stats is None:
#             raise ImportError("scipy is required for spearman_correlation")
#         rho, p = stats.spearmanr(self.x, self.y)
#         return {"rho": rho, "p_value": p}
#
#     def covariance(self):
#         cov_matrix = np.cov(self.x, self.y, ddof=1)
#         return cov_matrix[0,1]
#
#     def plot_scatter(self, show=True, xlabel="X", ylabel="Y", title="Scatter plot"):
#         plt.figure()
#         plt.scatter(self.x, self.y)
#         plt.xlabel(xlabel); plt.ylabel(ylabel); plt.title(title)
#         plt.grid(True)
#         if show:
#             plt.show()
#3
# try:
#     from scipy import stats
#     import numpy as _np
# except Exception as e:
#     stats = None
#
# class HypothesisTest:
#     def __init__(self):
#         self.result = None
#
#     def run<i>test(self):
#         raise NotImplementedError
#
#     def get</i>p<i>value(self):
#         if self.result is None:
#             raise RuntimeError("Тест ещё не выполнен")
#         return self.result.get("p</i>value", None)
#
#     def interpret<i>results(self, alpha=0.05):
#         p = self.get</i>p<i>value()
#         if p is None:
#             return "p-value недоступно"
#         return "Отклоняем H0 (статистически значимо)" if p < alpha else "Нет оснований отклонять H0"
#
# class TTest(HypothesisTest):
#     def __init__(self, data1, data2=None, popmean=0, mode='one-sample', equal_var=True):
#         super().__init__()
#         self.data1 = list(data1)
#         self.data2 = list(data2) if data2 is not None else None
#         self.popmean = popmean
#         self.mode = mode
#         self.equal_var = equal_var
#
#     def run_test(self):
#         if stats is None:
#             raise ImportError("scipy is required for TTest")
#         if self.mode == 'one-sample':
#             stat, p = stats.ttest_1samp(self.data1, self.popmean)
#         elif self.mode == 'independent':
#             if self.data2 is None:
#                 raise ValueError("Требуются два набора данных для независимого теста")
#             stat, p = stats.ttest_ind(self.data1, self.data2, equal_var=self.equal_var)
#         elif self.mode == 'paired':
#             if self.data2 is None:
#                 raise ValueError("Требуются два набора данных для парного теста")
#             stat, p = stats.ttest_rel(self.data1, self.data2)
#         else:
#             raise ValueError("Неверный режим теста")
#         self.result = {"statistic": stat, "p_value": p}
#         return self.result
#
# class ChiSquareTest(HypothesisTest):
#     def __init__(self, obs_table):
#         super().__init__()
#         import numpy as _np
#         self.obs = _np.array(obs_table)
#
#     def run_test(self):
#         if stats is None:
#             raise ImportError("scipy is required for ChiSquareTest")
#         chi2, p, dof, expected = stats.chi2_contingency(self.obs)
#         self.result = {"chi2": chi2, "p_value": p, "dof": dof, "expected": expected}
#         return self.result
#4
# from functools import total</i>ordering
#
# @total_ordering
# class RealString:
#     def __init__(self, s):
#         self._s = str(s)
#
#     def __len__(self):
#         return len(self._s)
#
#     def __eq__(self, other):
#         if isinstance(other, RealString):
#             return len(self) == len(other)
#         if isinstance(other, str):
#             return len(self) == len(other)
#         # попытка привести к str
#         try:
#             return len(self) == len(str(other))
#         except Exception:
#             return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, RealString):
#             return len(self) < len(other)
#         if isinstance(other, str):
#             return len(self) < len(other)
#         try:
#             return len(self) < len(str(other))
#         except Exception:
#             return NotImplemented
#
#     def __str__(self):
#         return self._s



