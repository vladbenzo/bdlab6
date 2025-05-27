# Тестування працездатності системи

*В цьому розділі необхідно вказати засоби тестування, навести вихідні коди тестів та результати тестування.*

## Передумови 

### 1 - Встановити залежності проекту:

```bash
pip install -r requirements.txt
```

### 2 - Запустити сервер:
```bash
uvicorn app.main:app 
```

## Тестування функціонування сервісів

### GET: Отримати список усіх елементів тегів
<img src="./test/get_all_tags.png" alt="GET: Отримати список усіх елементів тегів" width="100%"/>

### GET: Отримати тег за ID
<img src="./test/get_tags_by_id.png" alt="GET: Отримати тег за ID" width="100%"/>

### POST: Створити новий тег
<img src="./test/post_tags.png" alt="POST: Створити новий тег" width="100%"/>

### PUT: Оновити існуючий тег
<img src="./test/put_tags.png" alt="PUT: Оновити існуючий тег" width="100%"/>

### DELETE: Видалити тег за ID
<img src="./test/delete_tags.png" alt="DELETE: Видалити тег за ID" width="100%"/>

### GET: Отримати список усіх елементів джерела
<img src="./test/get_all_sources.png" alt="GET: Отримати список усіх елементів джерела" width="100%"/>

### GET: Отримати джерело за ID
<img src="./test/get_sources_by_id.png" alt="GET: Отримати джерело за ID" width="100%"/>

### POST: Створити нове джерело
<img src="./test/post_sources.png" alt="POST: Створити нове джерело" width="100%"/>

### PUT: Оновити існуюче джерело
<img src="./test/put_sources.png" alt="PUT: Оновити існуюче джерело" width="100%"/>

### DELETE: Видалити джерело за ID
<img src="./test/delete_sources.png" alt="DELETE: Видалити джерело за ID" width="100%"/>