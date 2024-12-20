## REST API магазина продуктов.

### API предоставляет возможность для управления пользователями, продуктами, их категорий и подкатегорий а так же корзиной товаров, которая доступна только авторизованым пользователям

## Инструкция по запуску:

### Клонирование репозитория

Для начала клонируйте репозиторий:

```
git clone https://github.com/JosepfVas/product_shop.git
```

Установка и настройка
Для установки проекта локально выполните следующие шаги:

1. Переход в директорию проекта и создание виртуального окружения
   Перейдите в директорию проекта и создайте виртуальное окружение:

```
cd product_shop
```

```
python -m venv venv
```

2. Активация виртуального окружения
   Активируйте виртуальное окружение:
   На Windows:

```
venv\Scripts\activate
```

На Unix или MacOS:

```
source venv/bin/activate
```

3. Установка зависимостей с помощью pip:

```
pip install -r requirements.txt
```

4. Установка зависимостей с помощью Poetry:

```
poetry install
```

5. Настройка переменных окружения
   Создайте файл .env по образцу .env.sample и заполните необходимыми значениями.

6. Выполнение миграций базы данных
   Выполните миграции:

```
python manage.py migrate
```

7. Запуск сервера разработки

```
python manage.py runserver
```

Теперь проект должен быть успешно установлен и запущен.


