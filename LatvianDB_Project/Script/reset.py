import sqlite3
import os

# Путь к твоей базе
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'Data', 'latvian_master.db')

conn = sqlite3.connect(DB_PATH)
# Возвращаем все 'error' в состояние 'new', чтобы скрипт их подхватил
conn.execute("UPDATE words SET status = 'new' WHERE status = 'error'")
conn.commit()
conn.close()
print("✅ Статусы сброшены! Теперь слова снова 'новые'.")