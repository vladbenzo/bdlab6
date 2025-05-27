from .database import database
from . import schemas
from asyncpg.exceptions import UniqueViolationError
from typing import Optional # <--- Додайте цей рядок


# --- UserRole (як зв'язуюча таблиця Profile та Role) ---
async def create_user_role(user_role: schemas.UserRoleAssociationCreate) -> schemas.UserRoleAssociationInDB:
    query = """
    INSERT INTO UserRole (profile_id, role_id)
    VALUES (:profile_id, :role_id)
    RETURNING profile_id, role_id
    """
    try:
        row = await database.fetch_one(query, values=user_role.dict())
        return schemas.UserRoleAssociationInDB(**row)
    except UniqueViolationError:
        raise ValueError("This user already has this role.")

async def get_user_roles_association() -> list[schemas.UserRoleAssociationInDB]:
    query = "SELECT profile_id, role_id FROM UserRole"
    rows = await database.fetch_all(query)
    return [schemas.UserRoleAssociationInDB(**r) for r in rows]

async def get_user_role_by_profile_and_role_id(profile_id: int, role_id: int) -> Optional[schemas.UserRoleAssociationInDB]:
    query = "SELECT profile_id, role_id FROM UserRole WHERE profile_id = :profile_id AND role_id = :role_id"
    row = await database.fetch_one(query, values={"profile_id": profile_id, "role_id": role_id})
    if row:
        return schemas.UserRoleAssociationInDB(**row)
    return None

async def delete_user_role(profile_id: int, role_id: int):
    query = "DELETE FROM UserRole WHERE profile_id = :profile_id AND role_id = :role_id RETURNING profile_id"
    row = await database.fetch_one(query, values={"profile_id": profile_id, "role_id": role_id})
    return row is not None

# --- Profile ---
async def create_profile(profile: schemas.ProfileCreate) -> schemas.ProfileInDB:
    query = """
    INSERT INTO Profile (first_name, last_name, email, password)
    VALUES (:first_name, :last_name, :email, :password)
    RETURNING id, first_name, last_name, email, password
    """
    row = await database.fetch_one(query, values=profile.dict())
    return schemas.ProfileInDB(**row)

async def get_profiles() -> list[schemas.ProfileInDB]:
    query = "SELECT id, first_name, last_name, email, password FROM Profile"
    rows = await database.fetch_all(query)
    return [schemas.ProfileInDB(**r) for r in rows]

async def get_profile_by_id(profile_id: int) -> Optional[schemas.ProfileInDB]:
    query = "SELECT id, first_name, last_name, email, password FROM Profile WHERE id = :id"
    row = await database.fetch_one(query, values={"id": profile_id})
    if row:
        return schemas.ProfileInDB(**row)
    return None

async def update_profile(profile_id: int, profile: schemas.ProfileUpdate) -> Optional[schemas.ProfileInDB]:
    update_data = {k: v for k, v in profile.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        return await get_profile_by_id(profile_id)

    set_clauses = ", ".join([f"{key} = :{key}" for key in update_data.keys()])
    query = f"""
    UPDATE Profile
    SET {set_clauses}
    WHERE id = :id
    RETURNING id, first_name, last_name, email, password
    """
    values = {"id": profile_id, **update_data}
    row = await database.fetch_one(query, values=values)
    if row:
        return schemas.ProfileInDB(**row)
    return None

async def delete_profile(profile_id: int) -> bool:
    query = "DELETE FROM Profile WHERE id = :id RETURNING id"
    row = await database.fetch_one(query, values={"id": profile_id})
    return row is not None