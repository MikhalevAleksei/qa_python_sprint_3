import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('list_books_names',
                             [
                                 'Гордость и предубеждение и зомби',
                                 'Что делать, если ваш кот хочет вас убить'
                             ]
                             )
    def test_add_new_book_add_two_books(self, collector, list_books_names):
        collector.add_new_book(list_books_names)
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_to_genre(self, collector):
        name = 'Зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert genre == collector.books_genre.get(name)

    def test_add_new_book(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_set_book_genre(self, collector):
        name = 'Колобок'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre(name) == genre

    def test_adult_books_not_in_children_books(self, collector):
        name = 'Зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_books_genre(name, genre)
        assert name not in collector.get_books_for_children()

    def test_get_books_with_specific_genre(self, collector):
        name = 'Зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_books_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    def test_get_books_genre(self, collector):
        name = 'Зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_books_genre(name, genre)
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children(self, collector):
        name = 'Колобок'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_for_children()

    def test_add_book_in_favorite(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        assert len(collector.add_book_in_favorites(name)) > 0

    def test_delete_book_from_favorites(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.add_book_in_favorites(name)) == 0

    def test_get_list_of_favorites_books(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert [name] == collector.get_list_of_favorites_books()
