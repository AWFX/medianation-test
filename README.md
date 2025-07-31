## Описание API

Получение постов.
```bash
curl http://localhost:8080/posts

[{"id": 1,"title": "first","content": "first"},{"id": 2,"title": "second","content": "second"},{"id": 3,"title": "third","content": "third"},{"id": 4,"title": "Moscow","content": "MSU"},{"id": 5,"title": "Tyumen","content": "UTMN"}]
```

Создание поста.
```bash
curl -X POST http://localhost:8080/posts -H "Content-Type: application/json" -d '{"title":"Los","content":"Angeles"}'

{"id":6,"title":"Moscow","content":"City"}
```

Проверка.

```bash
curl http://localhost:8080/health
{"message":"API is runnning"}
```
## **Технологии**

- Docker / Docker Compose
- PostgreSQL
- Python 3.12 / FastAPI

Хост для тестов:
- 2GB RAM
- 2 cores
- OS: Almalinux 9

## Сборка проект локально.

Необходимо прописать переменные в файле .env для работы с БД.

```bash
git clone https://github.com/AWFX/medianation-test.git
cd medianation-test

echo 'POSTGRES_USER=postgres\n'\
'POSTGRES_PASSWORD=1234\n'\
'POSTGRES_DB=posts\n'\
'POSTGRES_PORT=5432'\
>> .env

sudo docker-compose up -d                                                                
```

### Smoke-test

```bash                          
curl http://localhost:8080/health

{                                   
        "message": "API is runnning"
}            
