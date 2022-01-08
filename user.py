from db import get_db
from json import dumps


class User:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.username = kwargs["username"]

    @classmethod
    @property
    def db(cls):
        return get_db()

    @classmethod
    def create_user(cls, username):
        query = """
            INSERT INTO user (username) VALUES (?);
        """
        try:
            id = cls.db.execute(query, (username,)).lastrowid
            cls.db.commit()
        except cls.db.IntegrityError as err:
            return { "message": err }
        return cls(id=id, username=username)

    @classmethod
    def delete_user_by_id(cls, id):
        query = """
            DELETE FROM user WHERE id = ?;
        """
        cls.db.execute(query, (id,))
        cls.db.commit()
        return { "message": f"User with id {id} deleted" }

    @classmethod
    def delete_user_by_username(cls, username):
        query = """
            DELETE FROM user WHERE username = ?;
        """
        cls.db.execute(query, (username,))
        cls.db.commit()
        return { "message": f"User with username {username} deleted" }

    @classmethod
    def load_all_users(cls):
        query = """
            SELECT * FROM user;
        """
        return [User(**row) for row in cls.db.execute(query).fetchall()]

    @classmethod
    def load_user_by_username(cls, username):
        query = """
            SELECT * FROM user WHERE username = ?;
        """
        return [User(**row) for row in cls.db.execute(query, (username,)).fetchall()]

    @classmethod
    def load_user_by_id(cls, id):
        query = """
            SELECT * FROM user WHERE id = ?;
        """
        return [User(**row) for row in cls.db.execute(query, (id,)).fetchall()]

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, indent=4)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"
