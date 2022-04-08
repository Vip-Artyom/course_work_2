import json  # импортируем json

Data_Path = "data/data.json"
Comments_Path = "data/comments.json"

# Создаем класс с данными
class Data:

    def get_load_comments(self):
        """возвращает все комментарии"""
        with open(Comments_Path, "r", encoding="utf-8") as file:
            comments_data = json.load(file)
        return comments_data

    def get_load_posts(self):
        """возвращает все посты"""
        with open(Data_Path, "r", encoding="utf-8") as file:
            posts_data = json.load(file)
        return posts_data

    def counter_com(self, id):
        """считает сколько комментариев по ID"""
        counter = 0
        comments = self.get_load_comments()
        for comment in comments:
            if comment["post_id"] == id:
                counter += 1
        return counter

    def add_counter(self):
        """добавляет в список данные с количеством комментариев"""
        counter_list = []
        posts = self.get_load_posts()
        for post in posts:
            counter = self.counter_com(post["pk"])
            post['comments_count'] = counter
            counter_list.append(post)
        return counter_list

    def get_comments_by_post_id(self, post_id):
        """ возвращает комментарии определенного поста"""
        comments_list = []
        comment_all = self.get_load_comments()
        for comment in comment_all:
            if comment['post_id'] == post_id:
                comments_list.append(comment)
        return comments_list

    def get_posts_by_user(self, user_name):
        """  возвращает посты определенного пользователя """
        user_posts_list = []
        post_list = self.get_load_posts()
        for post in post_list:
            if post['poster_name'] == user_name:
                user_posts_list.append(post)
        return user_posts_list

    def search_for_posts(self, query):
        """ возвращает список постов по ключевому слову"""
        post_list = []
        posts = self.get_load_posts()
        for post in posts:
            if query.lower() in post['content'].lower():
                post_list.append(post)
        return post_list

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору"""
        posts = self.get_load_posts()
        find_post = None
        for post in posts:
            if post['pk'] == pk:
                find_post = post
        return find_post

