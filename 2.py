#1
class Number:
    def __init__(self, size=15, low=-50, high=50, data=None):
        if data is not None:
            self.lst = list(data)
        else:
            if size < 0:
                size = 0
            self.lst = [random.randint(low, high) for _ in range(size)]

    def process(self):
        n = len(self.lst)
        if n == 0:
            return
        avg = sum(self.lst) / n
        if avg > 0:
            k = (2 * n) // 3
        else:
            k = n // 3
        leftsorted = sorted(self.lst[:k])
        rightreversed = list(reversed(self.lst[k:]))
        self.lst = leftsorted + rightreversed
        return avg

    def __repr__(self):
        return f"{self.lst}"

#2
def grades_menu():
    print("Введите 10 оценок студента (целые числа 1..12):")
    grades = []
    while len(grades) < 10:
        try:
            v = int(input(f"Оценка #{len(grades)+1}: ").strip())
            if 1 <= v <= 12:
                grades.append(v)
            else:
                print("Оценка должна быть от 1 до 12.")
        except ValueError:
            print("Введите целое число.")

    while True:
        print("\nМеню:")
        print("1. Вывести оценки")
        print("2. Пересдача (замена оценки по номеру)")
        print("3. Проверить выплату стипендии (ср.балл >= 10.7)")
        print("4. Вывести отсортированный список (возр./уб.)")
        print("0. Выход")
        choice = input("> ").strip()
        if choice == '0':
            break
        elif choice == '1':
            print("Оценки:", grades)
        elif choice == '2':
            try:
                idx = int(input("Номер оценки для замены (1-10): ").strip()) - 1
                if not (0 <= idx < 10):
                    print("Неверный номер.")
                    continue
                new = int(input("Новая оценка (1-12): ").strip())
                if 1 <= new <= 12:
                    grades[idx] = new
                    print("Оценка изменена.")
                else:
                    print("Оценка должна быть 1..12.")
            except ValueError:
                print("Введите целые числа.")
        elif choice == '3':
            avg = sum(grades) / len(grades)
            print(f"Средний балл: {avg:.2f}")
            if avg >= 10.7:
                print("Стипендия положена.")
            else:
                print("Стипендия не положена.")
        elif choice == '4':
            order = input("Введите A для возрастания или D для убывания: ").strip().upper()
            if order == 'A':
                print("Отсортировано (возр.):", sorted(grades))
            elif order == 'D':
                print("Отсортировано (уб.):", sorted(grades, reverse=True))
            else:
                print("Некорректный ввод.")
        else:
            print("Неверный выбор.")


#3
def bubblesortimproved(arr, ascending=True):
    a = list(arr)
    n = len(a)
    passes = 0
    for i in range(n):
        swapped = 0
        for j in range(0, n - i - 1):
            if (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped += 1
        passes += 1
        if swapped == 0:
            break
    return a, passes
