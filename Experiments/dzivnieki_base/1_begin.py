# СКЕЛЕТ ПРОГРАММЫ (SOLID-структура)

class AuthSystem:
    """Модуль 1: Вход и Регистрация"""
    def __init__(self, db_name="users.db"):
        self.db = db_name
        # Здесь будет инициализация БД

    def register_user(self, username, password):
        # Логика: хэш пароля -> запись в БД
        pass

    def authenticate(self, username, password):
        # Логика: запрос к БД -> проверка хэша -> True/False
        pass

class DataManager:
    """Модуль 2: Управление файлом (запись)"""
    def save_animal(self, animal_data):
        # Логика: запись в dzivnieki.txt
        pass

class ListProvider:
    """Модуль 3: Чтение данных"""
    def get_animals(self):
        # Логика: чтение dzivnieki.txt -> возврат списка
        return []

class AppUI:
    """Модуль 4: Связующее звено (UI)"""
    def __init__(self):
        self.auth = AuthSystem()
        self.data_manager = DataManager()
        self.list_provider = ListProvider()
        
    def start(self):
        # Логика: запуск login_window
        pass

    def run_main_app(self):
        # Логика: запуск основного окна
        pass

# Точка входа
if __name__ == "__main__":
    app = AppUI()
    app.start()