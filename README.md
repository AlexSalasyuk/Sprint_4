# qa_python
## Sprint_4
### Это проект для тестирования класса `BooksCollector`
1. **test_add_new_book_one_book_without_genre** - проверка метода add_new_book и get_book_genre, добавление книги в словарь books_genre без жанра
2. **test_set_book_genre_existing_books_and_genres** - проверка присвоения жанра книге методом set_book_genre, если она в словаре books_genre, и жанр в списке genre
3. **test_get_book_genre_for_non_existent_book** - проверка метода get_book_genre, возвращает None для книги, которой нет в словаре books_genre
4. **test_get_books_with_specific_genre_returns_books_comedy** - проверка метода get_books_with_specific_genre, выводит список книг с определенным жанром Комедии
5. **test_get_books_genre_return_name_and_genre** - проверка метода get_books_genre, возвращает книгу и жанр из словаря books_genre
6. **test_get_books_for_children_safe_book** - проверка метода get_books_for_children что в ответе вернется безопасная книга
7. **test_add_book_in_favorites_add_book** - проверка метода add_book_in_favorites, книга добавляется в список избранных favorites, если она есть в списке books_genre
8. **test_delete_book_from_favorites_remove_book** - проверка метода delete_book_from_favorites книга удаляется из списка избранных favorites, если она там была
9. **test_get_list_of_favorites_books_return_favorites** - проверка метода get_list_of_favorites_books, метод возвращает список избранных книг из списка favorites
