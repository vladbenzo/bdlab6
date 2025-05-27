from pydantic import BaseModel, Field
from typing import Optional


class UserRoleBase(BaseModel):
       name: str = Field(..., max_length=255) 

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleUpdate(UserRoleBase):
    name: Optional[str] = Field(None, max_length=255)

class UserRoleInDB(UserRoleBase):
    id: int 

class RoleBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str = Field(..., max_length=255)

class RoleInDB(RoleBase):
    id: int


class UserRoleAssociationBase(BaseModel):
    profile_id: int
    role_id: int

class UserRoleAssociationCreate(UserRoleAssociationBase):
    pass

class UserRoleAssociationInDB(UserRoleAssociationBase):
    pass


class ProfileBase(BaseModel):
    first_name: str = Field(..., max_length=255)
    last_name: str = Field(..., max_length=255)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255) 

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    first_name: Optional[str] = Field(None, max_length=255)
    last_name: Optional[str] = Field(None, max_length=255)
    email: Optional[str] = Field(None, max_length=255)
    password: Optional[str] = Field(None, max_length=255)

class ProfileInDB(ProfileBase):
    id: int