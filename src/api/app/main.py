from fastapi import FastAPI, HTTPException, Depends, Query
from typing import List, Optional
from contextlib import asynccontextmanager

from . import crud, schemas, database  # Використовуємо відносні імпорти


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, що виконується при запуску застосунку
    await database.init_db_pool()
    yield
    # Код, що виконується при зупинці застосунку
    await database.close_db_pool()


app = FastAPI(lifespan=lifespan, title="API Медіаконтенту", version="0.1.0")


# --- Ендпоінти для MediaContent ---

@app.post("/media-content/", response_model=schemas.MediaContentInDB, status_code=201, tags=["Медіаконтент"])
async def create_new_media_content(mc: schemas.MediaContentCreate):
    """
    Створити новий медіаконтент.
    `profile_id` має посилатися на існуючий Профіль.
    `created_at` за замовчуванням встановлюється на сьогодні, якщо не надано.
    """
    created_mc = await crud.create_media_content(mc=mc)
    if not created_mc:
        # Можлива причина: profile_id не існує (якщо є FOREIGN KEY constraint)
        # Або інша помилка бази даних при вставці.
        # Розгляньте додавання більш специфічної обробки помилок тут,
        # наприклад, перехоплення asyncpg.exceptions.ForeignKeyViolationError
        raise HTTPException(status_code=400,
                            detail="Не вдалося створити медіаконтент. Можливо, вказано неіснуючий profile_id або інша помилка.")
    return created_mc


@app.get("/media-content/{media_content_id}", response_model=schemas.MediaContentWithTags, tags=["Медіаконтент"])
async def read_media_content_by_id(media_content_id: int):
    """
    Отримати медіаконтент за його ID, включаючи пов'язані теги.
    """
    db_mc = await crud.get_media_content(mc_id=media_content_id)  # Повертає schemas.MediaContentInDB або None
    if db_mc is None:
        raise HTTPException(status_code=404, detail="Медіаконтент не знайдено")

    tags = await crud.get_tags_for_media_content(mc_id=media_content_id)  # Повертає List[schemas.Tag]

    media_content_data = db_mc.model_dump()
    media_content_data['tags'] = tags

    mc_with_tags = schemas.MediaContentWithTags.model_validate(media_content_data)
    return mc_with_tags


@app.get("/media-content/", response_model=List[schemas.MediaContentInDB], tags=["Медіаконтент"])
async def read_all_media_content(skip: int = 0, limit: int = Query(default=100, le=200,
                                                                   description="Кількість записів для пропуску та максимальна кількість записів.")):
    """
    Отримати список усіх елементів медіаконтенту.
    """
    media_contents = await crud.get_all_media_content(skip=skip, limit=limit)
    return media_contents


@app.put("/media-content/{media_content_id}", response_model=schemas.MediaContentInDB, tags=["Медіаконтент"])
async def update_existing_media_content(media_content_id: int, mc_update: schemas.MediaContentUpdate):
    """
    Оновити існуючий медіаконтент. Будуть оновлені тільки надані поля.
    """
    # Перевірка, чи існує profile_id, якщо він надається в оновленні
    if mc_update.profile_id is not None:
        async with database.get_db_connection() as conn:
            profile_exists = await conn.fetchval("SELECT EXISTS(SELECT 1 FROM Profile WHERE id = $1)",
                                                 mc_update.profile_id)
        if not profile_exists:
            raise HTTPException(status_code=400, detail=f"Профіль з ID {mc_update.profile_id} для оновлення не існує.")

    updated_mc = await crud.update_media_content(mc_id=media_content_id, mc_update=mc_update)
    if updated_mc is None:
        raise HTTPException(status_code=404, detail="Медіаконтент не знайдено або оновлення не виконано")
    return updated_mc


@app.delete("/media-content/{media_content_id}", response_model=schemas.MediaContentInDB, tags=["Медіаконтент"])
async def remove_media_content(media_content_id: int):
    """
    Видалити медіаконтент за його ID.
    """
    deleted_mc = await crud.delete_media_content(mc_id=media_content_id)
    if deleted_mc is None:
        raise HTTPException(status_code=404, detail="Медіаконтент не знайдено")
    return deleted_mc


# --- Ендпоінти для MediaContentTag ---

@app.post("/media-content-tags/", response_model=schemas.MediaContentTagInDB, status_code=201,
          tags=["Теги Медіаконтенту"])
async def create_new_media_content_tag_link(mct: schemas.MediaContentTagCreate):
    """
    Зв'язати Тег з елементом Медіаконтенту.
    `tag_id` має посилатися на існуючий Тег.
    `mediaContent_id` має посилатися на існуючий Медіаконтент.
    """
    # Додаткова перевірка існування сутностей перед створенням зв'язку
    async with database.get_db_connection() as conn:
        tag_exists = await conn.fetchval("SELECT EXISTS(SELECT 1 FROM Tag WHERE id = $1)", mct.tag_id)
        if not tag_exists:
            raise HTTPException(status_code=404, detail=f"Тег з ID {mct.tag_id} не знайдено.")

        mc_exists = await conn.fetchval("SELECT EXISTS(SELECT 1 FROM MediaContent WHERE id = $1)", mct.mediaContent_id)
        if not mc_exists:
            raise HTTPException(status_code=404, detail=f"Медіаконтент з ID {mct.mediaContent_id} не знайдено.")

    created_mct = await crud.create_media_content_tag(mct=mct)
    if not created_mct:
        existing_link = await crud.get_media_content_tag(tag_id=mct.tag_id, mc_id=mct.mediaContent_id)
        if existing_link:
            raise HTTPException(status_code=409, detail="Зв'язок MediaContentTag вже існує.")
        raise HTTPException(status_code=500, detail="Не вдалося створити зв'язок MediaContentTag з невідомої причини.")
    return created_mct


@app.get("/media-content-tags/", response_model=List[schemas.MediaContentTagInDB], tags=["Теги Медіаконтенту"])
async def read_all_media_content_tag_links(skip: int = 0, limit: int = Query(default=100, le=200)):
    """
    Отримати всі зв'язки між Медіаконтентом та Тегами.
    """
    mct_links = await crud.get_all_media_content_tags(skip=skip, limit=limit)
    return mct_links


@app.get("/media-content/{media_content_id}/tags", response_model=List[schemas.Tag], tags=["Теги Медіаконтенту"])
async def read_tags_for_media_content(media_content_id: int):
    """
    Отримати всі теги, пов'язані з конкретним елементом Медіаконтенту.
    """
    db_mc = await crud.get_media_content(mc_id=media_content_id)
    if db_mc is None:
        raise HTTPException(status_code=404, detail="Медіаконтент не знайдено")

    tags = await crud.get_tags_for_media_content(mc_id=media_content_id)
    return tags


@app.delete("/media-content-tags/media/{media_content_id}/tag/{tag_id}", response_model=schemas.MediaContentTagInDB,
            tags=["Теги Медіаконтенту"])
async def remove_media_content_tag_link(media_content_id: int, tag_id: int):
    """
    Видалити конкретний зв'язок між елементом Медіаконтенту та Тегом.
    """
    deleted_mct = await crud.delete_media_content_tag(tag_id=tag_id, mc_id=media_content_id)
    if deleted_mct is None:
        raise HTTPException(status_code=404, detail="Зв'язок MediaContentTag не знайдено")
    return deleted_mct