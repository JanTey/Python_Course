def check_movies(movie_list, favorite):
    for movie in movie_list:
        if movie == favorite:
            print(f"✅ {movie} — это мой фаворит!")
        else:
            print(f"🎬 Фильм: {movie}")

my_movies = ["Интерстеллар", "Начало", "Гладиатор"]
my_fav = "Интерстеллар"

check_movies(my_movies, my_fav)
# =================================================================================
# Переменные - это просто имена для объектов
name = "Zhan"
age = 63
is_learning = True

# Современный стандарт вывода - f-строки
print(f"Привет, меня зовут {name}, мне {age} год. Учусь? {is_learning}")
# =================================================================================
sity = "Daugavpilī"
temperature = 5

# Современный стандарт вывода - f-строки
print(f"Es dzivoju {sity}. Šodien ārā ir {temperature} grādi.")