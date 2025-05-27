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

### GET: Отримати список всіх зв'язків користувач-роль
<img src="./test/GETUserRole.png" alt="GET: Отримати список всіх зв'язків користувач-роль" >

### POST: Створити зв'язок "користувач-роль"
<img src="./test/POSTUserRole.jpg" alt="POST: Створити зв'язок користувач-роль" >

### GET: Отримати конкретний зв'язок "користувач-роль" за Profile ID та Role ID
<img src="./test/GETUserRoleID.jpg" alt="Отримати конкретний зв'язок користувач-роль за Profile ID та Role ID" >

### DELETE: Видалити зв'язок "користувач-роль"
<img src="./test/DELETEUserRole.jpg" alt="DELETE: Видалити зв'язок користувач-роль" >

### GET: Отримати список всіх профілів
<img src="./test/GETProfile.jpg" alt="GET: Отримати список всіх профілів" >

### POST: Створити новий профіль
<img src="./test/POSTProfile.jpg" alt="POST: Створити новий профіль" >

### GET: Отримати профіль за ID
<img src="./test/GETProfileID.jpg" alt="GET: Отримати профіль за ID" >

### PUT: Оновити профіль за ID
<img src="./test/PUTProfileID.jpg" alt="PUT: Оновити профіль за ID" >

### DELETE: Видалити профіль за ID
<img src="./test/DELETEProfileID.jpg" alt="Видалити профіль за ID" >
