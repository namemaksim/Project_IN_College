import sqlite3 as sq

with sq.connect('saper.db') as con:  # создание таблицы
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

    info_users = [  # задание № 8
        ('Алексей', 1, 22, 1000),
        ('Миша', 1, 19, 800),
        ('Сергей', 1, 19, 900),
        ('Мария', 2, 18, 1500),
        ('Александр', 1, 20, 1100)
    ]
    cur.executemany("INSERT INTO users (name, sex, old, score) "
                    "VALUES ( ?, ?, ?, ?)", info_users)
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    cur.execute("SELECT name FROM users")  # задание № 9 (выбор всех пользователей)
    print(cur.fetchall())

    cur.execute("SELECT name, sex FROM users WHERE sex = 2")  # выбор женщин
    print(cur.fetchall())

    cur.execute("SELECT name, score FROM users WHERE score < 1000")  # игроки с результатом меньше 1000 очков
    print(cur.fetchall())

    cur.execute("SELECT name, score FROM users WHERE score = "  # игрок с наилучшим результатом
                "(SELECT MAX(score) FROM users)")
    print(cur.fetchall())

    cur.execute("SELECT name, old FROM users WHERE old BETWEEN 18 AND 20")  # игроки, возраст которых 18-20 лет
    print(cur.fetchall())

    cur.execute("UPDATE users SET old=20 WHERE old=19")  # Задание № 11 (замена: возраст 19 лет = 20 лет)

    cur.execute("UPDATE users SET score = score+300 WHERE score<1000")  # у кого < 1000 очков, тем +300 очков

    cur.execute("UPDATE users SET score = score+100 WHERE old=20")  # кому 20 лет, тем +100 очков

    cur.execute("DELETE FROM users WHERE score<1000")  # удаление тех игроков, у кого меньше 1000 очков

    cur.execute("SELECT * FROM users")  # вывод данных обновленной таблицы
    print(cur.fetchall())
