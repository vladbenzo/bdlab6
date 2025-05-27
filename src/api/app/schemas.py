from pydantic import BaseModel, Field
from typing import Optional


class UserRoleBase(BaseModel):
    # У вашій схемі UserRole в init.sql немає поля 'name' як такого,
    # є тільки 'id' для зв'язку з таблицею Role.
    # Однак, ви використовували 'name' в crud.py і main.py,
    # що, ймовірно, мало на увазі назву ролі з таблиці Role.
    # Оскільки ви запитували CRUD для UserRole, я припускаю,
    # що ви хочете керувати зв'язком profile_id-role_id.
    # Але для спрощення, і виходячи з вашого поточного коду,
    # де UserRole має 'name', я буду використовувати 'name'
    # як у ваших поточних `schemas.py`, `crud.py` і `main.py`
    # і припускати, що `user_roles` у `crud.py` має мапитись до `UserRole` у `init.sql`.
    # Щоб було коректно, потрібно було б працювати з Role таблицею для назв ролей,
    # а UserRole як зв'язуюча таблиця.
    # Але дотримуюсь вашого наявного підходу поки.
    # Якщо це не те, що ви хотіли, дайте знати.
    name: str = Field(..., max_length=255) # Збільшив max_length до 255 відповідно до Role.name

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleUpdate(UserRoleBase):
    name: Optional[str] = Field(None, max_length=255)

class UserRoleInDB(UserRoleBase):
    id: int # Це поле `id` з таблиці Role, якщо ми працюємо з Role.
            # Якщо це UserRole (профіль-роль), то id тут не буде, а будуть profile_id і role_id.
            # Знову ж таки, виходячи з вашого crud.py, де ви SELECT id, name FROM user_roles,
            # я залишаю id.
            # Однак у вашій `init.sql` таблиця `UserRole` має `profile_id` та `role_id`,
            # але не має `id` чи `name`.
            # Це **дуже важлива розбіжність**.
            # Я **виправлю** схеми, crud та main відповідно до реальної схеми `UserRole`
            # як зв'язуючої таблиці `profile_id` та `role_id`.

class RoleBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str = Field(..., max_length=255)

class RoleInDB(RoleBase):
    id: int

# Corrected UserRole Schemas based on init.sql
class UserRoleAssociationBase(BaseModel):
    profile_id: int
    role_id: int

class UserRoleAssociationCreate(UserRoleAssociationBase):
    pass

class UserRoleAssociationInDB(UserRoleAssociationBase):
    # No 'id' for a composite primary key table
    pass


class ProfileBase(BaseModel):
    first_name: str = Field(..., max_length=255)
    last_name: str = Field(..., max_length=255)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255) # В реальних застосунках паролі ніколи не передаються/зберігаються як plain text!

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    first_name: Optional[str] = Field(None, max_length=255)
    last_name: Optional[str] = Field(None, max_length=255)
    email: Optional[str] = Field(None, max_length=255)
    password: Optional[str] = Field(None, max_length=255)

class ProfileInDB(ProfileBase):
    id: int