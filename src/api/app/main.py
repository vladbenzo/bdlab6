from fastapi import FastAPI, Depends, HTTPException, status
from . import database, crud, schemas
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

# --- UserRole Endpoints (для зв'язуючої таблиці Profile-Role) ---

# POST: Додати роль користувачу
@app.post("/user-roles/", response_model=schemas.UserRoleAssociationInDB, status_code=status.HTTP_201_CREATED)
async def create_user_role_association(user_role: schemas.UserRoleAssociationCreate):
    try:
        return await crud.create_user_role(user_role)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) # Conflict if user already has role

# GET: Отримати всі зв'язки користувач-роль
@app.get("/user-roles/", response_model=List[schemas.UserRoleAssociationInDB])
async def list_user_roles_associations():
    return await crud.get_user_roles_association()

# GET: Отримати конкретний зв'язок за profile_id та role_id
@app.get("/user-roles/{profile_id}/{role_id}", response_model=schemas.UserRoleAssociationInDB)
async def get_specific_user_role_association(profile_id: int, role_id: int):
    user_role = await crud.get_user_role_by_profile_and_role_id(profile_id, role_id)
    if not user_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserRole association not found")
    return user_role

# DELETE: Видалити роль у користувача
@app.delete("/user-roles/{profile_id}/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_role_association(profile_id: int, role_id: int):
    deleted = await crud.delete_user_role(profile_id, role_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserRole association not found")
    return {"message": "UserRole association deleted successfully"}

# --- Profile Endpoints ---

# POST: Створити новий профіль
@app.post("/profiles/", response_model=schemas.ProfileInDB, status_code=status.HTTP_201_CREATED)
async def create_profile(profile: schemas.ProfileCreate):
    return await crud.create_profile(profile)

# GET: Отримати всі профілі
@app.get("/profiles/", response_model=List[schemas.ProfileInDB])
async def list_profiles():
    return await crud.get_profiles()

# GET: Отримати профіль за ID
@app.get("/profiles/{profile_id}", response_model=schemas.ProfileInDB)
async def get_profile(profile_id: int):
    profile = await crud.get_profile_by_id(profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile

# PUT: Оновити профіль за ID (повне оновлення)
@app.put("/profiles/{profile_id}", response_model=schemas.ProfileInDB)
async def update_profile(profile_id: int, profile: schemas.ProfileUpdate):
    updated_profile = await crud.update_profile(profile_id, profile)
    if not updated_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return updated_profile

# DELETE: Видалити профіль за ID
@app.delete("/profiles/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(profile_id: int):
    deleted = await crud.delete_profile(profile_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return {"message": "Profile deleted successfully"}