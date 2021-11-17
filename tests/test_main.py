from main import User, Post, Tag


class TestMain:
    def test_create_session(self, db_session):
        assert db_session

    def test_get_users(self, db_session):
        assert len(db_session.query(User).all()) == 3, \
            'Пользователи не создались'

    def test_get_posts(self, db_session):
        assert len(db_session.query(Post).all()) == 2, \
            'Страницы не создались'

    def test_get_tags(self, db_session):
        assert len(db_session.query(Tag).all()) == 4, \
            'Теги не создались'
