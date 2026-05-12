import sqlite3
import csv
import os

# Настраиваем пути с учетом твоей структуры
# Скрипт лежит в LatvianDB_Project/Script/import_csv.py
# Нам нужно попасть в LatvianDB_Project/Data/dictionary.csv

# Получаем путь к папке, где лежит этот скрипт (Script)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Поднимаемся на уровень выше в папку LatvianDB_Project
project_root = os.path.dirname(current_dir)

# Формируем точные пути к файлам
# Внимание: использую 'Data' и 'dictionare.csv' как на твоем скриншоте
DB_PATH = os.path.join(project_root, 'Data', 'latvian_master.db')
CSV_PATH = os.path.join(project_root, 'Data', 'dictionary.csv')

def get_db_stats():
    """Показывает состояние базы данных"""
    if not os.path.exists(DB_PATH):
        print(f"Файл базы данных не найден по пути: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        total = cursor.execute("SELECT COUNT(*) FROM words").fetchone()[0]
        new_words = cursor.execute("SELECT COUNT(*) FROM words WHERE status = 'new'").fetchone()[0]
        completed = cursor.execute("SELECT COUNT(*) FROM words WHERE status = 'completed'").fetchone()[0]
        
        print("\n--- СТАТИСТИКА БАЗЫ ДАННЫХ ---")
        print(f"Всего слов загружено: {total}")
        print(f"Ожидают обработки:    {new_words}")
        print(f"Готово (с формами):   {completed}")
        print("-----------------------------\n")
    except sqlite3.OperationsError:
        print("Таблица 'words' еще не создана.")
    finally:
        conn.close()

def import_from_csv():
    """Импортирует слова из CSV в базу данных"""
    if not os.path.exists(CSV_PATH):
        print(f"ОШИБКА: Файл не найден!")
        print(f"Искал здесь: {CSV_PATH}")
        print("Проверь название файла (dictionare vs dictionary) и папку.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Создаем таблицу
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE,
            translation TEXT,
            category TEXT,
            is_declinable INTEGER,
            status TEXT DEFAULT 'new'
        )
    ''')
    
    non_declinable = ['Izsauksmes vārds', 'Prievārds', 'Saiklis', 'Apstākļa vārds'] 
    # Примечание: Наречия (Apstākļa vārdi) часто не склоняются, 
    # но могут иметь степени сравнения. Пока пометим как 0 для простоты.

    added_count = 0
    duplicate_count = 0

    try:
        with open(CSV_PATH, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                word = row['Vārds'].strip()
                translation = row['Tulkojums'].strip()
                category = row['Kategorija'].strip()
                
                # Проверяем склоняемость
                is_dec = 0 if category in non_declinable else 1
                
                try:
                    cursor.execute(
                        "INSERT INTO words (word, translation, category, is_declinable) VALUES (?, ?, ?, ?)",
                        (word, translation, category, is_dec)
                    )
                    added_count += 1
                except sqlite3.IntegrityError:
                    duplicate_count += 1
                    continue
                    
        conn.commit()
        print("--- Отчет об импорте ---")
        print(f"Файл: {os.path.basename(CSV_PATH)}")
        print(f"Успешно добавлено: {added_count}")
        print(f"Пропущено дубликатов: {duplicate_count}")

    except Exception as e:
        print(f"Произошла ошибка при чтении: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    import_from_csv()
    get_db_stats()