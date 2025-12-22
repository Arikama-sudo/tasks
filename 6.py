#1
# def basketball_players():
#     players = {}
#
#     def add_player():
#         name = input("Введите ФИО баскетболиста: ")
#         height = input("Введите рост баскетболиста (в см): ")
#         players[name] = height
#         print(f"Баскетболист {name} добавлен.")
#
#     def delete_player():
#         name = input("Введите ФИО баскетболиста для удаления: ")
#         if name in players:
#             del players[name]
#             print(f"Баскетболист {name} удален.")
#         else:
#             print(f"Баскетболист {name} не найден.")
#
#     def search_player():
#         name = input("Введите ФИО баскетболиста для поиска: ")
#         if name in players:
#             print(f"ФИО: {name}, Рост: {players[name]} см")
#         else:
#             print(f"Баскетболист {name} не найден.")
#
#     def update_player():
#         name = input("Введите ФИО баскетболиста для изменения: ")
#         if name in players:
#             new_height = input("Введите новый рост (в см): ")
#             players[name] = new_height
#             print(f"Данные баскетболиста {name} обновлены.")
#         else:
#             print(f"Баскетболист {name} не найден.")
#
#     def show_all():
#         if players:
#             print("\nСписок всех баскетболистов:")
#             for name, height in players.items():
#                 print(f"ФИО: {name}, Рост: {height} см")
#         else:
#             print("Список баскетболистов пуст.")
#
#     while True:
#         print("\n--- Управление базой баскетболистов ---")
#         print("1. Добавить баскетболиста")
#         print("2. Удалить баскетболиста")
#         print("3. Найти баскетболиста")
#         print("4. Изменить данные баскетболиста")
#         print("5. Показать всех баскетболистов")
#         print("6. Выход")
#
#         choice = input("Выберите действие (1-6): ")
#
#         if choice == '1':
#             add_player()
#         elif choice == '2':
#             delete_player()
#         elif choice == '3':
#             search_player()
#         elif choice == '4':
#             update_player()
#         elif choice == '5':
#             show_all()
#         elif choice == '6':
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#2
# def english_french_dictionary():
#     dictionary = {}
#
#     def add_word():
#         english = input("Введите слово на английском: ").lower()
#         french = input("Введите перевод на французский: ").lower()
#         dictionary[english] = french
#         print(f"Слово '{english}' добавлено.")
#
#     def delete_word():
#         english = input("Введите английское слово для удаления: ").lower()
#         if english in dictionary:
#             del dictionary[english]
#             print(f"Слово '{english}' удалено.")
#         else:
#             print(f"Слово '{english}' не найдено.")
#
#     def search_word():
#         word = input("Введите слово для поиска: ").lower()
#         if word in dictionary:
#             print(f"Английский: {word}, Французский: {dictionary[word]}")
#         else:
#             print(f"Слово '{word}' не найдено.")
#
#     def update_word():
#         english = input("Введите английское слово для изменения: ").lower()
#         if english in dictionary:
#             new_french = input("Введите новый перевод на французский: ").lower()
#             dictionary[english] = new_french
#             print(f"Перевод слова '{english}' обновлен.")
#         else:
#             print(f"Слово '{english}' не найдено.")
#
#     def show_all():
#         if dictionary:
#             print("\nВесь словарь:")
#             for english, french in sorted(dictionary.items()):
#                 print(f"{english} -> {french}")
#         else:
#             print("Словарь пуст.")
#
#     while True:
#         print("\n--- Англо-французский словарь ---")
#         print("1. Добавить слово")
#         print("2. Удалить слово")
#         print("3. Найти слово")
#         print("4. Изменить перевод")
#         print("5. Показать весь словарь")
#         print("6. Выход")
#
#         choice = input("Выберите действие (1-6): ")
#
#         if choice == '1':
#             add_word()
#         elif choice == '2':
#             delete_word()
#         elif choice == '3':
#             search_word()
#         elif choice == '4':
#             update_word()
#         elif choice == '5':
#             show_all()
#         elif choice == '6':
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#3
# def company_employees():
#     employees = {}
#     employee_id = 1
#
#     def add_employee():
#         nonlocal employee_id
#         print(f"\nДобавление сотрудника (ID: {employee_id})")
#         full_name = input("Введите ФИО: ")
#         phone = input("Введите телефон: ")
#         email = input("Введите рабочий email: ")
#         position = input("Введите должность: ")
#         office = input("Введите номер кабинета: ")
#         skype = input("Введите Skype: ")
#
#         employees[employee_id] = {
#             'ФИО': full_name,
#             'Телефон': phone,
#             'Email': email,
#             'Должность': position,
#             'Кабинет': office,
#             'Skype': skype
#         }
#         print(f"Сотрудник {full_name} добавлен с ID {employee_id}")
#         employee_id += 1
#
#     def delete_employee():
#         emp_id = int(input("Введите ID сотрудника для удаления: "))
#         if emp_id in employees:
#             name = employees[emp_id]['ФИО']
#             del employees[emp_id]
#             print(f"Сотрудник {name} (ID: {emp_id}) удален.")
#         else:
#             print(f"Сотрудник с ID {emp_id} не найден.")
#
#     def search_employee():
#         search_by = input("Искать по (1 - ID, 2 - ФИО, 3 - Должности): ")
#
#         if search_by == '1':
#             emp_id = int(input("Введите ID сотрудника: "))
#             if emp_id in employees:
#                 print_employee_info(emp_id)
#             else:
#                 print("Сотрудник не найден.")
#
#         elif search_by == '2':
#             name = input("Введите ФИО или часть ФИО: ").lower()
#             found = False
#             for emp_id, data in employees.items():
#                 if name in data['ФИО'].lower():
#                     print_employee_info(emp_id)
#                     found = True
#             if not found:
#                 print("Сотрудники не найдены.")
#
#         elif search_by == '3':
#             position = input("Введите должность: ").lower()
#             found = False
#             for emp_id, data in employees.items():
#                 if position in data['Должность'].lower():
#                     print_employee_info(emp_id)
#                     found = True
#             if not found:
#                 print("Сотрудники не найдены.")
#
#     def update_employee():
#         emp_id = int(input("Введите ID сотрудника для изменения: "))
#         if emp_id in employees:
#             print(f"\nТекущие данные сотрудника ID {emp_id}:")
#             print_employee_info(emp_id)
#
#             print("\nКакое поле изменить?")
#             print("1. ФИО")
#             print("2. Телефон")
#             print("3. Email")
#             print("4. Должность")
#             print("5. Кабинет")
#             print("6. Skype")
#
#             field_choice = input("Выберите поле (1-6): ")
#             fields = ['', 'ФИО', 'Телефон', 'Email', 'Должность', 'Кабинет', 'Skype']
#
#             if field_choice in ['1', '2', '3', '4', '5', '6']:
#                 new_value = input(f"Введите новое значение для {fields[int(field_choice)]}: ")
#                 employees[emp_id][fields[int(field_choice)]] = new_value
#                 print("Данные обновлены.")
#             else:
#                 print("Неверный выбор.")
#         else:
#             print("Сотрудник не найден.")
#
#     def print_employee_info(emp_id):
#         data = employees[emp_id]
#         print(f"\nID: {emp_id}")
#         for key, value in data.items():
#             print(f"{key}: {value}")
#
#     def show_all():
#         if employees:
#             print("\nВсе сотрудники фирмы:")
#             for emp_id in sorted(employees.keys()):
#                 print_employee_info(emp_id)
#         else:
#             print("В фирме нет сотрудников.")
#
#     while True:
#         print("\n--- Управление базой сотрудников фирмы ---")
#         print("1. Добавить сотрудника")
#         print("2. Удалить сотрудника")
#         print("3. Найти сотрудника")
#         print("4. Изменить данные сотрудника")
#         print("5. Показать всех сотрудников")
#         print("6. Выход")
#
#         choice = input("Выберите действие (1-6): ")
#
#         if choice == '1':
#             add_employee()
#         elif choice == '2':
#             delete_employee()
#         elif choice == '3':
#             search_employee()
#         elif choice == '4':
#             update_employee()
#         elif choice == '5':
#             show_all()
#         elif choice == '6':
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#4
# def book_collection():
#     books = {}
#     book_id = 1
#
#     def add_book():
#         nonlocal book_id
#         print(f"\nДобавление книги (ID: {book_id})")
#         author = input("Введите автора: ")
#         title = input("Введите название книги: ")
#         genre = input("Введите жанр: ")
#         year = input("Введите год выпуска: ")
#         pages = input("Введите количество страниц: ")
#         publisher = input("Введите издательство: ")
#
#         books[book_id] = {
#             'Автор': author,
#             'Название': title,
#             'Жанр': genre,
#             'Год': year,
#             'Страницы': pages,
#             'Издательство': publisher
#         }
#         print(f"Книга '{title}' добавлена с ID {book_id}")
#         book_id += 1
#
#     def delete_book():
#         b_id = int(input("Введите ID книги для удаления: "))
#         if b_id in books:
#             title = books[b_id]['Название']
#             del books[b_id]
#             print(f"Книга '{title}' (ID: {b_id}) удалена.")
#         else:
#             print(f"Книга с ID {b_id} не найдена.")
#
#     def search_book():
#         print("Искать по:")
#         print("1. Названию")
#         print("2. Автору")
#         print("3. Жанру")
#         print("4. Году издания")
#
#         search_by = input("Выберите критерий поиска (1-4): ")
#         search_term = input("Введите поисковый запрос: ").lower()
#
#         found = False
#         for b_id, data in books.items():
#             if search_by == '1' and search_term in data['Название'].lower():
#                 found = True
#             elif search_by == '2' and search_term in data['Автор'].lower():
#                 found = True
#             elif search_by == '3' and search_term in data['Жанр'].lower():
#                 found = True
#             elif search_by == '4' and search_term in data['Год']:
#                 found = True
#             else:
#                 continue
#
#             if found:
#                 print_book_info(b_id)
#                 found = True
#
#         if not found:
#             print("Книги не найдены.")
#
#     def update_book():
#         b_id = int(input("Введите ID книги для изменения: "))
#         if b_id in books:
#             print(f"\nТекущие данные книги ID {b_id}:")
#             print_book_info(b_id)
#
#             print("\nКакое поле изменить?")
#             print("1. Автор")
#             print("2. Название")
#             print("3. Жанр")
#             print("4. Год выпуска")
#             print("5. Количество страниц")
#             print("6. Издательство")
#
#             field_choice = input("Выберите поле (1-6): ")
#             fields = ['', 'Автор', 'Название', 'Жанр', 'Год', 'Страницы', 'Издательство']
#
#             if field_choice in ['1', '2', '3', '4', '5', '6']:
#                 new_value = input(f"Введите новое значение для {fields[int(field_choice)]}: ")
#                 books[b_id][fields[int(field_choice)]] = new_value
#                 print("Данные обновлены.")
#             else:
#                 print("Неверный выбор.")
#         else:
#             print("Книга не найдена.")
#
#     def print_book_info(b_id):
#         data = books[b_id]
#         print(f"\nID: {b_id}")
#         for key, value in data.items():
#             print(f"{key}: {value}")
#         print("-" * 30)
#
#     def show_all():
#         if books:
#             print("\nВся книжная коллекция:")
#             for b_id in sorted(books.keys()):
#                 print_book_info(b_id)
#         else:
#             print("Коллекция пуста.")
#
#     def statistics():
#         if not books:
#             print("Коллекция пуста.")
#             return
#
#         total_books = len(books)
#         total_pages = sum(int(book['Страницы']) for book in books.values() if book['Страницы'].isdigit())
#
#         # Статистика по авторам
#         authors = {}
#         for book in books.values():
#             author = book['Автор']
#             authors[author] = authors.get(author, 0) + 1
#
#         # Статистика по жанрам
#         genres = {}
#         for book in books.values():
#             genre = book['Жанр']
#             genres[genre] = genres.get(genre, 0) + 1
#
#         print("\nСтатистика книжной коллекции:")
#         print(f"Всего книг: {total_books}")
#         print(f"Общее количество страниц: {total_pages}")
#
#         print("\nКниг по авторам:")
#         for author, count in sorted(authors.items()):
#             print(f"  {author}: {count} книг(и)")
#
#         print("\nКниг по жанрам:")
#         for genre, count in sorted(genres.items()):
#             print(f"  {genre}: {count} книг(и)")
#
#     while True:
#         print("\n--- Управление книжной коллекцией ---")
#         print("1. Добавить книгу")
#         print("2. Удалить книгу")
#         print("3. Найти книгу")
#         print("4. Изменить данные о книге")
#         print("5. Показать всю коллекцию")
#         print("6. Статистика коллекции")
#         print("7. Выход")
#
#         choice = input("Выберите действие (1-7): ")
#
#         if choice == '1':
#             add_book()
#         elif choice == '2':
#             delete_book()
#         elif choice == '3':
#             search_book()
#         elif choice == '4':
#             update_book()
#         elif choice == '5':
#             show_all()
#         elif choice == '6':
#             statistics()
#         elif choice == '7':
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")