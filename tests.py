import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2
    
    def test_add_new_book_add_one_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трех тел')
        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трех тел')
        assert 'Задача трех тел' in collector.books_genre.keys()

    def test_add_new_book_add_book_not_added_name_more_41(self):
        collector = BooksCollector()
        collector.add_new_book('Жизнь, необыкновенные и удивительные приключения Робинзона Крузо')
        assert len(collector.books_genre) == 0    

    def test_add_new_book_add_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трех тел')
        assert collector.books_genre['Задача трех тел'] == ''
    
    def test_set_book_genre_for_genre_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трех тел')
        collector.set_book_genre('Задача трех тел', 'Фантастика')
        assert collector.books_genre['Задача трех тел'] == 'Фантастика'

    def test_get_book_genre_with_genre_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        assert collector.get_book_genre('Испытание зверя') == 'Детективы'

    def test_get_books_with_specific_genre_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_genre_for_genre_not_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Конек-горбунок')
        collector.set_book_genre('Конек-горбунок', 'Сказка')
        assert collector.get_books_genre() == {'Конек-горбунок': ''}

    def test_get_books_for_children_only_book_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_for_children() == ['Дюна']

    @pytest.mark.parametrize('name, genre', [['Испытание зверя','Детективы'], ['Десять негритят', 'Детективы'], ['Зов Ктулху', 'Ужасы']])
    def test_get_books_for_children_no_books_for_adults(self,name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name  not in collector.get_books_for_children()
    
    def test_add_book_in_favorites_for_book_not_in_fav_added(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        collector.add_book_in_favorites('Испытание зверя') 
        assert collector.favorites == ['Испытание зверя']

    def test_add_book_in_favorites_for_book_in_fav_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детектив')
        collector.add_book_in_favorites('Испытание зверя')
        collector.add_book_in_favorites('Испытание зверя') 
        assert collector.favorites == ['Испытание зверя']

    def test_delete_book_from_favorites_one_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        collector.add_book_in_favorites('Испытание зверя')
        collector.delete_book_from_favorites('Испытание зверя')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Испытание зверя')
        collector.set_book_genre('Испытание зверя', 'Детективы')
        collector.add_book_in_favorites('Испытание зверя')
        assert collector.get_list_of_favorites_books() == ['Испытание зверя']
