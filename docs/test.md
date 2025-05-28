# Тестування працездатності системи

*В цьому розділі необхідно вказати засоби тестування, навести вихідні коди тестів та результати тестування.*

## Передумови 

### 1 - Встановити залежності проекту:

```bash
pip install -r requirements.txt
```

### 2 - Запустити сервер:
```bash
uvicorn app.main:app --reload

```

## Тестування функціонування сервісів

## Analysis Reports

### POST /reports/ Create Analysis Report
<img src="./test/POSTreports 1.png" alt="Зображення тестування POST запиту на ендпоінт /reports/ для створення нового звіту аналізу." >

### GET /reports/ Read All Analysis Reports
<img src="./test/GETreports.png" alt="Зображення тестування GET запиту на ендпоінт /reports/ для отримання списку всіх звітів аналізу." >

### GET /reports/{report_id} Read Single Analysis Report
<img src="./test/GETreportsID.png" alt="Зображення тестування GET запиту на ендпоінт /reports/{report_id} для отримання одного звіту аналізу за його ID." >

### PUT /reports/{report_id} Update Analysis Report
<img src="./test/PUTreports 1.png" alt="Зображення тестування PUT запиту на ендпоінт /reports/{report_id} для оновлення існуючого звіту аналізу." >

### DELETE /reports/{report_id} Delete Analysis Report
<img src="./test/DELETEreports.png" alt="Зображення тестування DELETE запиту на ендпоінт /reports/{report_id} для видалення звіту аналізу." >

## Analysis Results

### POST /results/ Create Analysis Result

<img src="./test/IMAGE_FOR_POST_RESULTS.png" alt="Зображення тестування POST запиту на ендпоінт /results/ для створення нового результату аналізу." >

### GET /results/ Read All Analysis Results
<img src="./test/GETresults.png" alt="Зображення тестування GET запиту на ендпоінт /results/ для отримання списку всіх результатів аналізу." >

### GET /results/{result_id} Read Single Analysis Result
<img src="./test/GETresults id.png" alt="Зображення тестування GET запиту на ендпоінт /results/{result_id} для отримання одного результату аналізу за його ID." >

### PUT /results/{result_id} Update Analysis Result
<img src="./test/PUTresults 1.png" alt="Зображення тестування PUT запиту на ендпоінт /results/{result_id} для оновлення існуючого результату аналізу." >

### DELETE /results/{result_id} Delete Analysis Result
<img src="./test/DELETEresults.png" alt="Зображення тестування DELETE запиту на ендпоінт /results/{result_id} для видалення результату аналізу." >
