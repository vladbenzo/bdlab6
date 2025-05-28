# main.py

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table, Text, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import date
from contextlib import contextmanager

# ------------------ Database Configuration ------------------
DATABASE_URL = 'postgresql://lab6_owner:npg_Eu9gJYCbVf5M@ep-floral-poetry-a8yp58mw-pooler.eastus2.azure.neon.tech/lab6?sslmode=require'

engine = create_engine(DATABASE_URL, echo=False) # Поставьте echo=True для отладки SQL, если проблема останется
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------ Database Session Dependency ------------------
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    with get_db_context() as db:
        yield db

# ------------------ Association Tables ------------------
user_role_association = Table('userrole', Base.metadata,
    Column('profile_id', Integer, ForeignKey('profile.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

role_permission_association = Table('rolepermission', Base.metadata,
    Column('role_id', Integer, ForeignKey('role.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

mediacontent_source_association = Table('mediacontentsource', Base.metadata,
    Column('source_id', Integer, ForeignKey('source.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('mediacontent_id', Integer, ForeignKey('mediacontent.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

mediacontent_tag_association = Table('mediacontenttag', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('mediacontent_id', Integer, ForeignKey('mediacontent.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

source_tag_association = Table('sourcetag', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('source_id', Integer, ForeignKey('source.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

analysisreport_tag_association = Table('analysisreporttag', Base.metadata,
    Column('analysisreport_id', Integer, ForeignKey('analysisreport.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

analysisresult_tag_association = Table('analysisresulttag', Base.metadata,
    Column('analysisresult_id', Integer, ForeignKey('analysisresult.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

mediacontent_analysisresult_association = Table('mediacontentanalysisresult', Base.metadata,
    Column('mediacontent_id', Integer, ForeignKey('mediacontent.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column('analysisresult_id', Integer, ForeignKey('analysisresult.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
)

# ------------------ SQLAlchemy Models ------------------

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=False)

class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)

class Source(Base):
    __tablename__ = 'source'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)

class MediaContent(Base):
    __tablename__ = 'mediacontent'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    body = Column(Text, nullable=False)
    content_type = Column(String(255), nullable=False)
    created_at = Column(Date, default=date.today)
    profile_id = Column(Integer, ForeignKey('profile.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

# --- ИЗМЕНЕННЫЙ ПОРЯДОК И ОПРЕДЕЛЕНИЕ AnalysisResult и AnalysisReport ---
class AnalysisResult(Base):
    __tablename__ = 'analysisresult'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    body = Column(String(255), nullable=False)
    created_at = Column(Date, default=date.today)
    analysisreport_id = Column('analysisreport_id', Integer, ForeignKey('analysisreport.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

class AnalysisReport(Base):
    __tablename__ = 'analysisreport'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    body = Column(String(255), nullable=False)
    created_at = Column(Date, default=date.today)
    profile_id = Column(Integer, ForeignKey('profile.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

# --- Определение Relationships после определения всех основных классов ---
# Profile relationships
Profile.mediacontents = relationship("MediaContent", back_populates="profile", cascade="all, delete-orphan")
Profile.analysis_reports = relationship("AnalysisReport", back_populates="profile", cascade="all, delete-orphan")
Profile.analysis_results_owned = relationship("AnalysisResult", foreign_keys=[AnalysisResult.profile_id], back_populates="owner_profile", cascade="all, delete-orphan")
Profile.roles = relationship("Role", secondary=user_role_association, back_populates="profiles")

# Role relationships
Role.profiles = relationship("Profile", secondary=user_role_association, back_populates="roles")
Role.permissions = relationship("Permission", secondary=role_permission_association, back_populates="roles")

# Permission relationships
Permission.roles = relationship("Role", secondary=role_permission_association, back_populates="permissions")

# Source relationships
Source.mediacontents = relationship("MediaContent", secondary=mediacontent_source_association, back_populates="sources")
Source.tags = relationship("Tag", secondary=source_tag_association, back_populates="sources_associated")

# MediaContent relationships
MediaContent.profile = relationship("Profile", back_populates="mediacontents")
MediaContent.sources = relationship("Source", secondary=mediacontent_source_association, back_populates="mediacontents")
MediaContent.tags = relationship("Tag", secondary=mediacontent_tag_association, back_populates="mediacontents_associated")
MediaContent.analysis_results = relationship("AnalysisResult", secondary=mediacontent_analysisresult_association, back_populates="mediacontents_analyzed")

# AnalysisReport relationships
AnalysisReport.profile = relationship("Profile", back_populates="analysis_reports")
AnalysisReport.results = relationship(
    "AnalysisResult",
    foreign_keys=[AnalysisResult.analysisreport_id], # Прямая ссылка на атрибут
    back_populates="report",
    cascade="all, delete-orphan"
)
AnalysisReport.tags = relationship("Tag", secondary=analysisreport_tag_association, back_populates="analysis_reports_associated")

# AnalysisResult relationships
AnalysisResult.report = relationship("AnalysisReport", back_populates="results") # foreign_keys выводятся из AnalysisReport.results
AnalysisResult.owner_profile = relationship("Profile", foreign_keys=[AnalysisResult.profile_id], back_populates="analysis_results_owned")
AnalysisResult.tags = relationship("Tag", secondary=analysisresult_tag_association, back_populates="analysis_results_associated")
AnalysisResult.mediacontents_analyzed = relationship("MediaContent", secondary=mediacontent_analysisresult_association, back_populates="analysis_results")

# Tag relationships (back_populates)
Tag.sources_associated = relationship("Source", secondary=source_tag_association, back_populates="tags")
Tag.mediacontents_associated = relationship("MediaContent", secondary=mediacontent_tag_association, back_populates="tags")
Tag.analysis_reports_associated = relationship("AnalysisReport", secondary=analysisreport_tag_association, back_populates="tags")
Tag.analysis_results_associated = relationship("AnalysisResult", secondary=analysisresult_tag_association, back_populates="tags")

# ------------------ Pydantic Schemas ------------------
# (Этот блок остается без изменений)
class BaseOrmModel(BaseModel):
    model_config = {"from_attributes": True}

class IdSchema(BaseOrmModel):
    id: int

class TagBase(BaseModel):
    name: str
class TagCreate(TagBase):
    pass
class TagRead(TagBase, BaseOrmModel):
    id: int

class PermissionBase(BaseModel):
    name: str
class PermissionCreate(PermissionBase):
    pass
class PermissionRead(PermissionBase, BaseOrmModel):
    id: int

class RoleBase(BaseModel):
    name: str
    description: str
class RoleCreate(RoleBase):
    permission_ids: Optional[List[int]] = Field(default_factory=list)
class RoleRead(RoleBase, BaseOrmModel):
    id: int
    permissions: List[PermissionRead] = []

class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    email: str
class ProfileCreate(ProfileBase):
    password: str
    role_ids: Optional[List[int]] = Field(default_factory=list)
class ProfileRead(ProfileBase, BaseOrmModel):
    id: int
    roles: List[RoleRead] = []

class SourceBase(BaseModel):
    name: str
    url: str
class SourceCreate(SourceBase):
    tag_ids: Optional[List[int]] = Field(default_factory=list)
class SourceRead(SourceBase, BaseOrmModel):
    id: int
    tags: List[TagRead] = []

class AnalysisResultRead(BaseOrmModel): pass
class AnalysisReportRead(BaseOrmModel): pass

class ProfileReadMinimal(BaseOrmModel):
    id: int
    first_name: str
    last_name: str
    email: str
class AnalysisReportReadMinimal(BaseOrmModel):
    id: int
    title: str
    created_at: date

class MediaContentBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    body: str
    content_type: str
    profile_id: int
class MediaContentCreate(MediaContentBase):
    source_ids: Optional[List[int]] = Field(default_factory=list)
    tag_ids: Optional[List[int]] = Field(default_factory=list)
    analysis_result_ids: Optional[List[int]] = Field(default_factory=list)
class MediaContentRead(MediaContentBase, BaseOrmModel):
    id: int
    created_at: date
    profile: ProfileReadMinimal
    sources: List[SourceRead] = []
    tags: List[TagRead] = []
    analysis_results: List['AnalysisResultRead'] = []

class AnalysisReportBase(BaseModel):
    title: str
    body: str
    profile_id: int
class AnalysisReportCreate(AnalysisReportBase):
    tag_ids: Optional[List[int]] = Field(default_factory=list)
class AnalysisReportRead(AnalysisReportBase, BaseOrmModel):
    id: int
    created_at: date
    profile: ProfileReadMinimal
    tags: List[TagRead] = []
    results: List['AnalysisResultRead'] = []

class AnalysisResultBase(BaseModel):
    title: str
    description: Optional[str] = None
    body: str
    analysisreport_id: int
    profile_id: int
class AnalysisResultCreate(AnalysisResultBase):
    tag_ids: Optional[List[int]] = Field(default_factory=list)
    mediacontent_ids: Optional[List[int]] = Field(default_factory=list)
class AnalysisResultRead(AnalysisResultBase, BaseOrmModel):
    id: int
    created_at: date
    report: Optional[AnalysisReportReadMinimal] = None
    owner_profile: Optional[ProfileReadMinimal] = None
    tags: List[TagRead] = []
    mediacontents_analyzed: List[IdSchema] = []

MediaContentRead.model_rebuild()
AnalysisReportRead.model_rebuild()
AnalysisResultRead.model_rebuild()

# ------------------ FastAPI Application ------------------
# (Этот блок и эндпоинты остаются без изменений)
app = FastAPI(title="Comprehensive Analysis API v3", version="3.0.0")

@app.on_event("startup")
async def on_startup():
    print("Ensure your DDL script has been executed against the database.")
    print("Startup complete.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

def get_profile_or_404(db: Session, profile_id: int) -> Profile:
    item = db.query(Profile).filter(Profile.id == profile_id).first()
    if not item: raise HTTPException(status_code=404, detail=f"Profile with id {profile_id} not found")
    return item

def get_tag_or_404(db: Session, tag_id: int) -> Tag:
    item = db.query(Tag).filter(Tag.id == tag_id).first()
    if not item: raise HTTPException(status_code=404, detail=f"Tag with id {tag_id} not found")
    return item

def get_analysis_report_or_404(db: Session, report_id: int) -> AnalysisReport:
    item = db.query(AnalysisReport).filter(AnalysisReport.id == report_id).first()
    if not item: raise HTTPException(status_code=404, detail=f"AnalysisReport with id {report_id} not found")
    return item

def get_analysis_result_or_404(db: Session, result_id: int) -> AnalysisResult:
    item = db.query(AnalysisResult).filter(AnalysisResult.id == result_id).first()
    if not item: raise HTTPException(status_code=404, detail=f"AnalysisResult with id {result_id} not found")
    return item

def get_mediacontent_or_404(db: Session, mc_id: int) -> MediaContent:
    item = db.query(MediaContent).filter(MediaContent.id == mc_id).first()
    if not item: raise HTTPException(status_code=404, detail=f"MediaContent with id {mc_id} not found")
    return item

@app.post("/reports/", response_model=AnalysisReportRead, status_code=status.HTTP_201_CREATED, tags=["Analysis Reports"])
def create_analysis_report(report_data: AnalysisReportCreate, db: Session = Depends(get_db)):
    get_profile_or_404(db, report_data.profile_id)
    report_dict = report_data.model_dump(exclude={"tag_ids"})
    db_report = AnalysisReport(**report_dict)
    if report_data.tag_ids:
        db_report.tags.extend([get_tag_or_404(db, tag_id) for tag_id in set(report_data.tag_ids)])
    try:
        db.add(db_report); db.commit(); db.refresh(db_report)
        return db_report
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.get("/reports/", response_model=List[AnalysisReportRead], tags=["Analysis Reports"])
def read_all_analysis_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AnalysisReport).order_by(AnalysisReport.id.asc()).offset(skip).limit(limit).all()

@app.get("/reports/{report_id}", response_model=AnalysisReportRead, tags=["Analysis Reports"])
def read_single_analysis_report(report_id: int, db: Session = Depends(get_db)):
    return get_analysis_report_or_404(db, report_id)

@app.put("/reports/{report_id}", response_model=AnalysisReportRead, tags=["Analysis Reports"])
def update_analysis_report(report_id: int, report_update_data: AnalysisReportCreate, db: Session = Depends(get_db)):
    db_report = get_analysis_report_or_404(db, report_id)
    if report_update_data.profile_id != db_report.profile_id:
        get_profile_or_404(db, report_update_data.profile_id)
    update_data = report_update_data.model_dump(exclude_unset=True, exclude={"tag_ids"})
    for key, value in update_data.items(): setattr(db_report, key, value)
    if report_update_data.tag_ids is not None:
        db_report.tags.clear()
        if report_update_data.tag_ids:
            db_report.tags.extend([get_tag_or_404(db, tag_id) for tag_id in set(report_update_data.tag_ids)])
    try:
        db.commit(); db.refresh(db_report)
        return db_report
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.delete("/reports/{report_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Analysis Reports"])
def delete_analysis_report(report_id: int, db: Session = Depends(get_db)):
    db_report = get_analysis_report_or_404(db, report_id)
    try:
        db.delete(db_report); db.commit()
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=f"Error deleting report: {str(e)}")
    return None

@app.post("/results/", response_model=AnalysisResultRead, status_code=status.HTTP_201_CREATED, tags=["Analysis Results"])
def create_analysis_result(result_data: AnalysisResultCreate, db: Session = Depends(get_db)):
    get_profile_or_404(db, result_data.profile_id)
    get_analysis_report_or_404(db, result_data.analysisreport_id)
    result_dict = result_data.model_dump(exclude={"tag_ids", "mediacontent_ids"})
    db_result = AnalysisResult(**result_dict)
    if result_data.tag_ids:
        db_result.tags.extend([get_tag_or_404(db, tag_id) for tag_id in set(result_data.tag_ids)])
    if result_data.mediacontent_ids:
        db_result.mediacontents_analyzed.extend([get_mediacontent_or_404(db, mc_id) for mc_id in set(result_data.mediacontent_ids)])
    try:
        db.add(db_result); db.commit(); db.refresh(db_result)
        return db_result
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.get("/results/", response_model=List[AnalysisResultRead], tags=["Analysis Results"])
def read_all_analysis_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AnalysisResult).order_by(AnalysisResult.id.asc()).offset(skip).limit(limit).all()

@app.get("/results/{result_id}", response_model=AnalysisResultRead, tags=["Analysis Results"])
def read_single_analysis_result(result_id: int, db: Session = Depends(get_db)):
    return get_analysis_result_or_404(db, result_id)

@app.put("/results/{result_id}", response_model=AnalysisResultRead, tags=["Analysis Results"])
def update_analysis_result(result_id: int, result_update_data: AnalysisResultCreate, db: Session = Depends(get_db)):
    db_result = get_analysis_result_or_404(db, result_id)
    if result_update_data.profile_id != db_result.profile_id:
        get_profile_or_404(db, result_update_data.profile_id)
    if result_update_data.analysisreport_id != db_result.analysisreport_id:
        get_analysis_report_or_404(db, result_update_data.analysisreport_id)
    update_data = result_update_data.model_dump(exclude_unset=True, exclude={"tag_ids", "mediacontent_ids"})
    for key, value in update_data.items(): setattr(db_result, key, value)
    if result_update_data.tag_ids is not None:
        db_result.tags.clear()
        if result_update_data.tag_ids:
            db_result.tags.extend([get_tag_or_404(db, tag_id) for tag_id in set(result_update_data.tag_ids)])
    if result_update_data.mediacontent_ids is not None:
        db_result.mediacontents_analyzed.clear()
        if result_update_data.mediacontent_ids:
            db_result.mediacontents_analyzed.extend([get_mediacontent_or_404(db, mc_id) for mc_id in set(result_update_data.mediacontent_ids)])
    try:
        db.commit(); db.refresh(db_result)
        return db_result
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.delete("/results/{result_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Analysis Results"])
def delete_analysis_result(result_id: int, db: Session = Depends(get_db)):
    db_result = get_analysis_result_or_404(db, result_id)
    try:
        db.delete(db_result); db.commit()
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=f"Error deleting result: {str(e)}")
    return None

@app.post("/tags/", response_model=TagRead, status_code=status.HTTP_201_CREATED, tags=["Tags"])
def create_tag_endpoint(tag_data: TagCreate, db: Session = Depends(get_db)):
    if db.query(Tag).filter(Tag.name == tag_data.name).first():
        raise HTTPException(status_code=400, detail="Tag with this name already exists")
    db_tag_obj = Tag(**tag_data.model_dump())
    try:
        db.add(db_tag_obj); db.commit(); db.refresh(db_tag_obj)
        return db_tag_obj
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.get("/tags/", response_model=List[TagRead], tags=["Tags"])
def read_tags_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Tag).offset(skip).limit(limit).all()

@app.post("/profiles/", response_model=ProfileRead, tags=["Profiles"])
def create_profile_endpoint(profile_data: ProfileCreate, db: Session = Depends(get_db)):
    if db.query(Profile).filter(Profile.email == profile_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = profile_data.password + "_hashed_placeholder"
    profile_dict = profile_data.model_dump(exclude={"role_ids", "password"})
    db_profile = Profile(**profile_dict, password=hashed_password)
    if profile_data.role_ids:
        roles = db.query(Role).filter(Role.id.in_(profile_data.role_ids)).all()
        if len(roles) != len(set(profile_data.role_ids)):
            raise HTTPException(status_code=404, detail="One or more roles not found")
        db_profile.roles.extend(roles)
    try:
        db.add(db_profile); db.commit(); db.refresh(db_profile)
        return db_profile
    except IntegrityError as e: db.rollback(); raise HTTPException(status_code=400, detail=f"DB Integrity Error: {e.orig}")
    except Exception as e: db.rollback(); raise HTTPException(status_code=500, detail=str(e))

@app.get("/profiles/{profile_id}", response_model=ProfileRead, tags=["Profiles"])
def read_profile_endpoint(profile_id: int, db: Session = Depends(get_db)):
    return get_profile_or_404(db, profile_id)

if __name__ == "__main__":
    print("Ensure your DDL script has been executed against the database.")
    print(f"Starting Uvicorn server. API will be available at http://127.0.0.1:8000")
    print(f"Interactive API docs at http://127.0.0.1:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)