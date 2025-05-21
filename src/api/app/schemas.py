from pydantic import BaseModel, Field, AliasChoices
from typing import Optional, List
from datetime import date

# --- Схеми MediaContent ---
class MediaContentBase(BaseModel):
    title: str = Field(..., max_length=100, description="Заголовок медіаконтенту")
    description: Optional[str] = Field(None, description="Опис медіаконтенту")
    body: str = Field(..., description="Тіло медіаконтенту")
    content_type: str = Field(..., max_length=255, description="Тип контенту (стаття, відео тощо)")
    profile_id: int = Field(..., description="ID профілю автора")
    created_at: Optional[date] = Field(default_factory=date.today, description="Дата створення")

class MediaContentCreate(MediaContentBase):
    """Схема для створення MediaContent."""
    pass

class MediaContentUpdate(BaseModel):
    """Схема для оновлення MediaContent. Усі поля опціональні."""
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    body: Optional[str] = None
    content_type: Optional[str] = Field(None, max_length=255)
    profile_id: Optional[int] = None
    created_at: Optional[date] = None

class MediaContentInDB(MediaContentBase):
    """Схема для представлення MediaContent з бази даних, включаючи ID."""
    id: int

    class Config:
        from_attributes = True

# --- Схеми MediaContentTag ---
class MediaContentTagBase(BaseModel):
    tag_id: int = Field(..., description="ID тегу")
    mediaContent_id: int = Field(..., validation_alias=AliasChoices('mediaContent_id', 'mediacontent_id'), description="ID медіаконтенту")

class MediaContentTagCreate(MediaContentTagBase):
    """Схема для створення зв'язку MediaContentTag."""
    pass

class MediaContentTagInDB(MediaContentTagBase):
    """Схема для представлення MediaContentTag з бази даних."""
    class Config:
        from_attributes = True

# --- Схема Tag (для можливого використання у відповідях) ---
class Tag(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# --- Складена схема для MediaContent з тегами ---
class MediaContentWithTags(MediaContentInDB):
    """Схема MediaContent з включеним списком його тегів."""
    tags: List[Tag] = []