import pytest
from classes.class_data import Data

data = Data()


class TestData:

    def test_get_load_comments(self):
        assert type(data.get_load_comments()) == list, "Ошибка загрузки файла"

    def test_get_load_posts(self):
        assert type(data.get_load_posts()) == list, "Ошибка загрузки файла"

    def test_counter_com(self):
        assert data.counter_com(1) == 4, True

    def test_add_counter(self):
        assert type(data.add_counter()) == list, True

    def test_get_posts_by_user(self):
        assert type(data.get_posts_by_user("leo")) == list, True

    def test_search_for_posts(self):
        assert type(data.search_for_posts("еда")) == list, True

    def test_get_post_by_pk(self):
        assert type(data.get_post_by_pk(1)) == dict, True