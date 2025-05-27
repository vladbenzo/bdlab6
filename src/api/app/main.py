from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Tag, Source
from sqlalchemy.exc import IntegrityError


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/tags/")
def create_tag(name: str, db: Session = Depends(get_db)):
    existing_tag = db.query(Tag).filter_by(name=name).first()
    if existing_tag:
        return existing_tag
    new_tag = Tag(name=name)
    db.add(new_tag)
    try:
        db.commit()
        db.refresh(new_tag)
        return new_tag
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Tag already exists or ID conflict.")

@app.get("/tags/{tag_id}")
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).get(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@app.get("/tags/")
def read_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()

@app.put("/tags/{tag_id}")
def update_tag(tag_id: int, name: str, db: Session = Depends(get_db)):
    tag = db.query(Tag).get(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag.name = name
    db.commit()
    db.refresh(tag)
    return tag



@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).get(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return tag



@app.post("/sources/")
def create_source(name: str, url: str, db: Session = Depends(get_db)):
    existing = db.query(Source).filter_by(name=name).first()
    if existing:
        return existing
    source = Source(name=name, url=url)
    db.add(source)
    try:
        db.commit()
        db.refresh(source)
        return source
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Source already exists or ID conflict.")

@app.get("/sources/")
def read_sources(db: Session = Depends(get_db)):
    return db.query(Source).all()

@app.get("/sources/{source_id}")
def read_source(source_id: int, db: Session = Depends(get_db)):
    source = db.query(Source).get(source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source


@app.put("/sources/{source_id}")
def update_source(source_id: int, name: str, url: str, db: Session = Depends(get_db)):
    source = db.query(Source).get(source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    source.name = name
    source.url = url
    db.commit()
    db.refresh(source)
    return source


@app.delete("/sources/{source_id}")
def delete_source(source_id: int, db: Session = Depends(get_db)):
    source = db.query(Source).get(source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    db.delete(source)
    db.commit()
    return source



