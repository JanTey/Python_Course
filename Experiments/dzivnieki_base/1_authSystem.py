import sqlite3
import hashlib
import os

class AuthSystem:
    def __init__(self, db_name="users.db"):
        # 1. Определяем путь один раз при запуске
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_name)
        
        self._init_db()

    def _init_db(self):
        # 2. Используем self.db_path здесь
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password_hash TEXT
                )
            """)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        hashed = self._hash_password(password)
        try:
            # 3. И здесь используем self.db_path
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                             (username, hashed))
                return True, "Регистрация успешна!"
        except sqlite3.IntegrityError:
            return False, "Логин уже занят!"

    def authenticate(self, username, password):
        hashed = self._hash_password(password)
        # 4. И здесь обязательно self.db_path
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row and row[0] == hashed:
                return True
        return False