# **Описание тестов**
## Тесты на добавление книг
* test_add_new_book_add_two_books_added - проверка добавления двух книг
* test_add_new_book_add_one_book_added - проверка добавления одной книги   
* test_add_new_book_add_book_added - проверка того, что книга добавлена
* test_add_new_book_add_book_not_added_name_more_41 - проверка невозможности добавления книги с названием больше 41 знака
* test_add_new_book_add_book_has_no_genre - проверка отсутствия жанра при добавлении книги
## Тесты на добавление жанра
* test_set_book_genre_for_genre_from_list - проверка добавления жанра из списка жанров
## Тесты на получение жанра
* test_get_book_genre_with_genre_from_list - проверка получения жанра книги по её имени при внесенном жанре из списка жанров
## Тесты на получение списка книг с определенным жанром
* test_get_books_with_specific_genre_one_book - проверка вывода списка книг с определённым жанром для одной книги
* test_get_books_genre_for_genre_not_from_list - проверка получения словаря с книгами и жанрами для книги с жанром не из списка
## Тесты на получение списка книг для детей
* test_get_books_for_children_only_book_for_children - проверка получения списка книг, подходящих детям  
* test_get_books_for_children_no_books_for_adults - проверка списка книг, подходящих детям, на оттсутствие книг, не подходящих детям
## Тесты на добавление книги в Избранное
* test_add_book_in_favorites_for_book_not_in_fav_added - проверка добавления книги в Избранное для книги не в Избранном
* test_add_book_in_favorites_for_book_in_fav_not_added - проверка невозможности повторного добавления книги в Избранное для книги уже в Избранном
## Тесты на удаление книги из Избранного
* test_delete_book_from_favorites_one_book_deleted - Проверка удаления одной книги из Избранного
## Тесты на получение списка Избранного
* test_get_list_of_favorites_books_one_book - проверка Избранного после добавления одной книги
