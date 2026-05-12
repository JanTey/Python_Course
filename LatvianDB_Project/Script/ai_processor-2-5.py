import google.generativeai as genai
import sqlite3
import os
import json
import time
from dotenv import load_dotenv

# --- ПУТИ ---
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_SCRIPT_DIR)
DB_PATH = os.path.join(BASE_DIR, "Data", "latvian_master.db")
ENV_PATH = os.path.join(BASE_DIR, ".env")

# --- ЗАГРУЗКА И КОНФИГУРАЦИЯ ---
load_dotenv(ENV_PATH)
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Твоя проверенная модель
MODEL_NAME = "gemini-3.1-flash-lite"

# Настройки безопасности
safety = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(model_name=MODEL_NAME, safety_settings=safety)


def get_db_connection():
    return sqlite3.connect(DB_PATH, timeout=20)


def process_word(word_id, word, category):
    # Приводим к нижнему регистру для надежности поиска подстрок
    cat_l = category.lower()
    
    # --- ЛОГИКА ИНСТРУКЦИЙ (с учетом уточнений по глаголам) ---
    if "darbības vārds" in cat_l:
        info = ""
        if "1. grupa" in cat_l: info = "1st conjugation (short/stem-changing)."
        elif "2. grupa" in cat_l: info = "2nd conjugation (-āt, -ot, -īt)."
        elif "3. grupa" in cat_l: info = "3rd conjugation (-ēt, -īt)."
        elif "irregular" in cat_l: info = "IRREGULAR verb."
        
        refl = " This is a REFLEXIVE verb (atgriezeniskais)." if "atgriezenisks" in cat_l else ""
        
        task = f"conjugation in Present, Past, Future (1st, 2nd, 3rd person, sing. and plur.). {info}{refl}"
        
    elif "īpašības vārds" in cat_l:
        task = "declension in 7 cases, singular and plural, Masculine Indefinite."
    elif "lietvārds" in cat_l:
        task = "declension in 7 cases, singular and plural."
    else:
        task = "no changes, just return the word as a 'fixed' form."

    prompt = f"""
    Return ONLY a JSON object for the Latvian word '{word}' ({category}).
    Task: {task}
    Format: {{"forms": [{{"t": "type_of_form", "n": "sing_or_plur", "v": "value"}}]}}
    No markdown, no talk.
    """

    try:
        response = model.generate_content(prompt)
        if not response.text:
            raise ValueError("Empty response (check safety settings)")

        raw_text = (
            response.text.strip().replace("```json", "").replace("```", "").strip()
        )
        data = json.loads(raw_text)

        conn = get_db_connection()
        cursor = conn.cursor()

        if "forms" in data:
            for item in data["forms"]:
                cursor.execute(
                    """
                    INSERT INTO word_forms (word_id, case_name, number, form_value)
                    VALUES (?, ?, ?, ?)
                """,
                    (word_id, item.get("t"), item.get("n"), item.get("v")),
                )

            cursor.execute(
                "UPDATE words SET status = 'completed' WHERE id = ?", (word_id,)
            )
            conn.commit()
            print(f"✅ {word} ({category})")

        conn.close()
        return True

    except Exception as e:
        print(f"❌ {word}: {e}")
        try:
            c = get_db_connection()
            c.execute("UPDATE words SET status = 'error' WHERE id = ?", (word_id,))
            c.commit()
            c.close()
        except:
            pass
        return False


if __name__ == "__main__":
    print(f"🚀 Запуск на {MODEL_NAME}...")

    while True:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Изменил выборку: берем 'new' и пробуем переделать 'error'
        cursor.execute(
            "SELECT id, word, category FROM words WHERE status IN ('new', 'error') LIMIT 1"
        )
        row = cursor.fetchone()
        conn.close()

        if not row:
            print("🏁 Готово!")
            break

        process_word(row[0], row[1], row[2])
        # Небольшая задержка, чтобы не спамить API
        time.sleep(2)