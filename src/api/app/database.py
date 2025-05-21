import asyncpg
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Глобальна змінна для зберігання пулу з'єднань
pool = None

async def init_db_pool():
    """Ініціалізує пул з'єднань з базою даних."""
    global pool
    if DATABASE_URL is None:
        raise ValueError("Змінна середовища DATABASE_URL не встановлена.")
    try:
        pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=10)
        print("Пул з'єднань з базою даних успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні пулу з'єднань з базою даних: {e}")
        pool = None

async def close_db_pool():
    """Закриває пул з'єднань з базою даних."""
    global pool
    if pool:
        await pool.close()
        print("Пул з'єднань з базою даних закрито.")

@asynccontextmanager
async def get_db_connection():
    """Контекстний менеджер для отримання з'єднання з пулу."""
    if pool is None:
        raise RuntimeError("Пул бази даних не ініціалізовано. Спочатку викличте init_db_pool().")
    conn = None
    try:
        conn = await pool.acquire()
        yield conn
    finally:
        if conn:
            await pool.release(conn)