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
<img src="./test/GETUserRole.jpg" alt="GET: Отримати список всіх зв'язків користувач-роль" width="100%"/>

### POST: Створити зв'язок "користувач-роль"
<img src="./test/POSTUserRole.jpg" alt="POST: Створити зв'язок користувач-роль" width="100%"/>

### GET: Отримати конкретний зв'язок "користувач-роль" за Profile ID та Role ID
<img src="./test/GETUserRoleID.jpg" alt="Отримати конкретний зв'язок користувач-роль за Profile ID та Role ID" width="100%"/>

### DELETE: Видалити зв'язок "користувач-роль"
<img src="./test/DELETEUserRole.jpg" alt="DELETE: Видалити зв'язок користувач-роль" width="100%"/>

### GET: Отримати список всіх профілів
<img src="./test/GETProfile.jpg" alt="GET: Отримати список всіх профілів" width="100%"/>

### POST: Створити новий профіль
<img src="./test/POSTProfile.jpg" alt="POST: Створити новий профіль" width="100%"/>

### GET: Отримати профіль за ID
<img src="./test/GETProfileID.jpg" alt="GET: Отримати профіль за ID" width="100%"/>

### PUT: Оновити профіль за ID
<img src="./test/PUTProfileID.jpg" alt="PUT: Оновити профіль за ID" width="100%"/>

### DELETE: Видалити профіль за ID
<img src="./test/DELETEProfileID.jpg" alt="Видалити профіль за ID" width="100%"/>
