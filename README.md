# Questions microservice

### Описание:
Приложение для сбора вопросов викторины с внешнего API и загрузки их в локальную базу данных.

### Требования:
* Python 3.10
* Docker/Compose

### Установка:

Сборка приложения
```bash
sudo docker-compose build
```
### Запуск приложения:
```bash
sudo docker-compose up
```

### Пример POST запроса
```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 1}' http://127.0.0.1:8000/questions
```

- Второй вариант это запуск запроса через файл questions_api.http

### Коннект к базе данных

```bash
docker-compose exec db psql -U postgres -d Flask
```