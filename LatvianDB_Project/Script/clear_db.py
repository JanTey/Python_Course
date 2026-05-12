import sqlite3
import os

# Укажи путь к твоей базе данных
DB_PATH = 'LatvianDB_Project/Data/latvian_master.db'

def clear_database():
    if not os.path.exists(DB_PATH):
        print(f"❌ Файл базы данных не найден по пути: {DB_PATH}")
        return

    confirm = input("⚠️ Ты уверен, что хочешь ПОЛНОСТЬЮ очистить базу? (y/n): ")
    
    if confirm.lower() == 'y':
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            # Очищаем таблицы
            cursor.execute("DELETE FROM word_forms;")
            cursor.execute("DELETE FROM words;")
            
            # Сбрасываем счетчики ID, чтобы начать с 1
            cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('words', 'word_forms');")
            
            conn.commit()
            conn.close()
            print("✅ База успешно очищена! Теперь она пустая и готова к новому импорту.")
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")
    else:
        print("Отмена операции.")

if __name__ == "__main__":
    clear_database()