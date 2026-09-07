# goit-pythonweb-hw-06

Домашнє завдання з Python Web Development: робота з PostgreSQL, SQLAlchemy, Alembic, Poetry та Docker.

## Опис

У проєкті реалізовано базу даних для навчального процесу з такими сутностями:
- студенти;
- групи;
- викладачі;
- предмети;
- оцінки студентів із датою отримання.

Проєкт містить:
- SQLAlchemy-моделі;
- міграції Alembic;
- скрипт заповнення бази випадковими даними через Faker;
- набір SQLAlchemy-запитів для вибірок;
- тестовий `main.py` для перевірки запитів.

## Структура проєкту

```text
goit-pythonweb-hw-06/
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── .gitignore
├── alembic.ini
├── database.py
├── docker-compose.yaml
├── main.py
├── models.py
├── my_select.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── seed.py
```

## Використані технології

- Python
- Poetry
- PostgreSQL
- Docker
- SQLAlchemy
- Alembic
- Faker

## Встановлення та запуск

### 1. Клонування репозиторію

```bash
git clone <URL_репозиторію>
cd goit-pythonweb-hw-06
```

### 2. Встановлення залежностей

```bash
poetry install
```

### 3. Запуск PostgreSQL у Docker

```bash
docker compose up -d
```

### 4. Створення та застосування міграцій

```bash
poetry run alembic revision --autogenerate -m "Init"
poetry run alembic upgrade head
```

### 5. Заповнення бази тестовими даними

```bash
poetry run python seed.py
```

### 6. Перевірка запитів

```bash
poetry run python main.py
```

## Реалізовані запити

У файлі `my_select.py` реалізовано 10 функцій:
- `select_1` — 5 студентів із найбільшим середнім балом;
- `select_2` — студент із найвищим середнім балом з певного предмета;
- `select_3` — середній бал у групах з певного предмета;
- `select_4` — середній бал на потоці;
- `select_5` — курси, які читає певний викладач;
- `select_6` — список студентів у певній групі;
- `select_7` — оцінки студентів у групі з певного предмета;
- `select_8` — середній бал, який ставить певний викладач;
- `select_9` — курси, які відвідує певний студент;
- `select_10` — курси, які певному студентові читає певний викладач.
