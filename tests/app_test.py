import pytest

from app import app


def test_app_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, "Ошибка"
    assert type(response.json) == list, "Выведен не список"
    assert response.json[0].keys() == {'content', 'likes_count', 'pic', 'pk', 'poster_avatar',
                                       'poster_name', 'views_count'}, 'Ключи не верные'


def test_app_id():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200, "Ошибка"
    assert type(response.json) == dict, "Выведен не словарь"
    assert response.json.keys() == {'content', 'likes_count', 'pic', 'pk', 'poster_avatar',
                                    'poster_name', 'views_count'}, 'Ключи не верные'
