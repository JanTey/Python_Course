import sqlite3
import os

# Путь к твоей базе (проверь, чтобы совпадал)
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_SCRIPT_DIR)
DB_PATH = os.path.join(BASE_DIR, "Data", "latvian_master.db")

def fix_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 1. Исправляем слово Lūdzu (убираем кириллическую 'з' и 'у')
        # 2. Ставим статус 'new', чтобы основной скрипт его переработал
        sql = "UPDATE words SET word = 'Lūdzu', status = 'completed' WHERE id = 99"
        
        cursor.execute(sql)
        conn.commit()
        
        if cursor.rowcount > 0:
            print("✅ Успешно! Слово исправлено, статус сброшен.")
        else:
            print("❓ Строка с id=99 не найдена или уже исправлена.")
            
        conn.close()
    except Exception as e:
        print(f"❌ Ошибка при работе с базой: {e}")

if __name__ == "__main__":
    fix_data()