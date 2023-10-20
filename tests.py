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

    # check book added to genre
    def test_add_new_book_to_genre(self, collector):
        collector.add_new_book('Зомби')
        assert collector.get_book_genre('Зомби') in collector.genre

    # check book added to books_genre
    def test_add_new_book(self, collector):
        collector.add_new_book('Колобок')
        assert 'Колобок' in collector.books_genre

    # check set genre by name
    def test_set_book_genre(self, collector):
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert collector.books_genre['Колобок'] == 'Мультфильмы'

    # 'Книги с возрастным рейтингом отсутствуют в списке книг для детей.'
    def test_adult_books_not_in_children_books(self, collector):
        collector.add_new_book('Зомби')
        collector.set_books_genre('Зомби', 'Ужасы')
        assert 'Зомби' not in collector.genre_age_rating

    def test_get_books_with_specific_genre(self, collector):
        genre = 'Мультфильмы'
        collector.get_books_with_specific_genre(genre)
        assert genre in collector.books_with_specific_genre

    def test_get_books_genre(self, collector):
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.get_books_for_children()
        assert 'Колобок' in collector.books_for_children

    def test_add_book_in_favorite(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        name = 'Колобок'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == collector.favorites
