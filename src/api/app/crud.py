from typing import List, Optional, Dict, Any
from datetime import date
import asyncpg
from . import schemas
from .database import get_db_connection


# --- CRUD для MediaContent ---

async def create_media_content(mc: schemas.MediaContentCreate) -> Optional[schemas.MediaContentInDB]:
    """Створює новий запис MediaContent в базі даних."""
    query = """
    INSERT INTO MediaContent (title, description, body, content_type, profile_id, created_at)
    VALUES ($1, $2, $3, $4, $5, $6)
    RETURNING id, title, description, body, content_type, profile_id, created_at;
    """
    async with get_db_connection() as conn:
        row = await conn.fetchrow(
            query, mc.title, mc.description, mc.body, mc.content_type, mc.profile_id, mc.created_at
        )
    return schemas.MediaContentInDB.model_validate(dict(row)) if row else None


async def get_media_content(mc_id: int) -> Optional[schemas.MediaContentInDB]:
    """Отримує MediaContent за ID."""
    query = "SELECT id, title, description, body, content_type, profile_id, created_at FROM MediaContent WHERE id = $1;"
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, mc_id)
    return schemas.MediaContentInDB.model_validate(dict(row)) if row else None


async def get_all_media_content(skip: int = 0, limit: int = 100) -> List[schemas.MediaContentInDB]:
    """Отримує список усіх MediaContent з пагінацією."""
    query = "SELECT id, title, description, body, content_type, profile_id, created_at FROM MediaContent ORDER BY id OFFSET $1 LIMIT $2;"
    async with get_db_connection() as conn:
        rows = await conn.fetch(query, skip, limit)
    return [schemas.MediaContentInDB.model_validate(dict(row)) for row in rows]


async def update_media_content(mc_id: int, mc_update: schemas.MediaContentUpdate) -> Optional[schemas.MediaContentInDB]:
    """Оновлює існуючий MediaContent. Оновлюються тільки надані поля."""
    current_mc = await get_media_content(mc_id)
    if not current_mc:
        return None

    update_data = mc_update.model_dump(exclude_unset=True)
    if not update_data:
        return current_mc

    set_clauses = []
    values = []
    idx = 1
    for key, value in update_data.items():
        set_clauses.append(f"{key} = ${idx}")
        values.append(value)
        idx += 1

    values.append(mc_id)

    query = f"""
    UPDATE MediaContent
    SET {', '.join(set_clauses)}
    WHERE id = ${idx}
    RETURNING id, title, description, body, content_type, profile_id, created_at;
    """
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, *values)
    return schemas.MediaContentInDB.model_validate(dict(row)) if row else None


async def delete_media_content(mc_id: int) -> Optional[schemas.MediaContentInDB]:
    """Видаляє MediaContent за ID."""
    query = "DELETE FROM MediaContent WHERE id = $1 RETURNING id, title, description, body, content_type, profile_id, created_at;"
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, mc_id)
    return schemas.MediaContentInDB.model_validate(dict(row)) if row else None


# --- CRUD для MediaContentTag ---

async def create_media_content_tag(mct: schemas.MediaContentTagCreate) -> Optional[schemas.MediaContentTagInDB]:
    """Створює зв'язок між MediaContent та Tag."""
    query = """
    INSERT INTO MediaContentTag (tag_id, mediaContent_id)
    VALUES ($1, $2)
    ON CONFLICT (tag_id, mediaContent_id) DO NOTHING
    RETURNING tag_id, mediaContent_id;
    """
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, mct.tag_id, mct.mediaContent_id)
    return schemas.MediaContentTagInDB.model_validate(dict(row)) if row else None


async def get_media_content_tag(tag_id: int, mc_id: int) -> Optional[schemas.MediaContentTagInDB]:
    """Отримує конкретний зв'язок MediaContentTag за ID тегу та ID медіаконтенту."""
    query = "SELECT tag_id, mediaContent_id FROM MediaContentTag WHERE tag_id = $1 AND mediaContent_id = $2;"
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, tag_id, mc_id)
    return schemas.MediaContentTagInDB.model_validate(dict(row)) if row else None


async def get_all_media_content_tags(skip: int = 0, limit: int = 100) -> List[schemas.MediaContentTagInDB]:
    """Отримує список усіх зв'язків MediaContentTag з пагінацією."""
    query = "SELECT tag_id, mediaContent_id FROM MediaContentTag ORDER BY mediaContent_id, tag_id OFFSET $1 LIMIT $2;"
    async with get_db_connection() as conn:
        rows = await conn.fetch(query, skip, limit)
    return [schemas.MediaContentTagInDB.model_validate(dict(row)) for row in rows]


async def get_tags_for_media_content(mc_id: int) -> List[schemas.Tag]:
    """Отримує всі теги, пов'язані з конкретним MediaContent."""
    query = """
    SELECT t.id, t.name
    FROM Tag t
    INNER JOIN MediaContentTag mct ON t.id = mct.tag_id
    WHERE mct.mediaContent_id = $1;
    """
    async with get_db_connection() as conn:
        rows = await conn.fetch(query, mc_id)
    return [schemas.Tag.model_validate(dict(row)) for row in rows]


async def delete_media_content_tag(tag_id: int, mc_id: int) -> Optional[schemas.MediaContentTagInDB]:
    """Видаляє зв'язок між MediaContent та Tag."""
    query = """
    DELETE FROM MediaContentTag
    WHERE tag_id = $1 AND mediaContent_id = $2
    RETURNING tag_id, mediaContent_id;
    """
    async with get_db_connection() as conn:
        row = await conn.fetchrow(query, tag_id, mc_id)
    return schemas.MediaContentTagInDB.model_validate(dict(row)) if row else None