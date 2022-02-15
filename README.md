# Описание проекта
##  веб-сервис для обработки данных.

### Стек технологий
- Django
- Celery
- PostgreSQL
- Docker

### Установка
Перед запуском проекта убедитесь, что у вас установлен python, docker и docker-compose.

```bash
python --version
```

```
docker --version
```

```
docker-compose --version
```
Переходим в рабочую директорию и клонируем проект.

```bash
git clone https://github.com/Timur-Razzakov/Welltory_test_project
```

Установливаем зависимости.

```
pip install -r requirements.txt
```

Создаём .env файл и добавляем следующие настройки

- Настройки сервера
  - `SERVER_HOST=`... (поумолчанию 0.0.0.0)
  - `SERVER_PORT=`... (поумолчанию 8000)
  
- Настройки базы данных 
  - `POSTGRES_HOST=`... (поумолчанию 0.0.0.0)
  - `POSTGRES_PORT=`... (поумолчанию 5432)
  - `POSTGRES_DB=`... (обязательное поле)
  - `POSTGRES_USER=`... (обязательное поле)
  - `POSTGRES_PASSWORD=`... (обязательное поле)
 
- Настройка REDIS 
  - `REDIS_HOST=`... (поумолчанию 127.0.0.1)
  - `RADIS_PORT=`... (поумолчанию 6379)

- Секретный ключ
  - `SECRET_KEY=`... (обязательное поле)

Запускаем проект на компьютере

```
python manage.py runserver
```

Запускаем проект в docker (но для этого обязательно укажите в вашем env-файле: **POSTGRES_HOST=db**)

```
docker-compose up
```

# Внешний вид проекта

![image](https://user-images.githubusercontent.com/75569467/151605486-6491c606-9a7c-467a-8433-85acf9afaaf1.png)


![image](https://user-images.githubusercontent.com/75569467/151606307-d6707918-fe96-444d-ab71-b8e1305ddec0.png)

