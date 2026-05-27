import sys
import os
import my_lib.terminal_utils as term
print("Пути поиска Python:", sys.path)

try:
    term.clear_screen()

    print("Успех: Модуль найден!")
except ImportError as e:
    print("Ошибка импорта:", e)
