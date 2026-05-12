import sqlite3
import os

# Путь к твоей базе (проверь, чтобы совпадал)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Data/latvian_master.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. Полностью очищаем таблицу с падежами
cursor.execute("DELETE FROM word_forms")

# 2. Сбрасываем все слова обратно в статус 'new'
cursor.execute("UPDATE words SET status = 'new'")

conn.commit()
conn.close()
print("База очищена! Теперь запускай основной скрипт ai_processor.py")