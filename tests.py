import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2 # get_books_rating нет в классе, поменял на get_books_genre чтоб не падал

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

#let's do it
# 1 проверка метода add_new_book и get_book_genre, добавление книги в словарь books_genre без жанра
    def test_add_new_book_one_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')

        assert collector.get_book_genre('Хоббит') == ''

# 2 проверка присвоения жанра книге методом set_book_genre, если она в словаре books_genre, и жанр в списке genre
    @pytest.mark.parametrize('book_name, genre', [
        ('Основание', 'Фантастика'),
        ('Девушка с татуировкой дракона', 'Детективы'),
        ('Зов Ктулху', 'Ужасы')
    ])
    def test_set_book_genre_existing_books_and_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

# 3 проверка метода get_book_genre, возвращает None для книги, которой нет в словаре books_genre
    def test_get_book_genre_for_non_existent_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Война и Мир') is None

# 4 проверка метода get_books_with_specific_genre, выводит список книг с определенным жанром Комедии
    @pytest.mark.parametrize('book_name, genre', [
        ('Горе от ума', 'Комедии'),
        ('Укрощение строптивой', 'Комедии')
    ])
    def test_get_books_with_specific_genre_returns_books_comedy(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_with_specific_genre('Комедии')

# 5 проверка get_books_genre, возвращает книгу и жанр из словаря books_genre
    def test_get_books_genre_return_name_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984','Фантастика')

        assert collector.get_books_genre() == {'1984': 'Фантастика'}

# 6 проверка get_books_for_children что в ответе вернется безопасная книга
    def test_get_books_for_children_safe_book(self):
        collector = BooksCollector()
        collector.add_new_book('Прелюдия к Основанию')
        collector.set_book_genre('Прелюдия к Основанию', 'Фантастика')

        assert 'Прелюдия к Основанию' in collector.get_books_for_children()

# 7 проверка add_book_in_favorites, книга добавляется в список избранных favorites, если она есть в списке books_genre.
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Путь к Основанию')
        collector.set_book_genre('Путь к Основанию', 'Фантастика')
        collector.add_book_in_favorites('Путь к Основанию')

        assert 'Путь к Основанию' in collector.get_list_of_favorites_books()

# 8 проверка delete_book_from_favorites книга удаляется из списка избранных favorites, если она там была.
    def test_delete_book_from_favorites_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book('Основание и Империя')
        collector.add_book_in_favorites('Основание и Империя')
        collector.delete_book_from_favorites('Основание и Империя')

        assert 'Основание и Империя' not in collector.get_list_of_favorites_books()

# 9 проверка get_list_of_favorites_books, метод возвращает список избранных книг из списка favorites
    @pytest.mark.parametrize('book_name, genre', [
        ('Второе Основание', 'Фантастика'),
        ('Кризис Основания', 'Фантастика')
    ])
    def test_get_list_of_favorites_books_return_favorites(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == [book_name]







