from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/artist/", response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = crud.get_artist_by_email(db, email=artist.email)
    if db_artist:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_artist(db=db, artist=artist)

@app.get("/artists/", response_model=list[schemas.Artist])
def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists


@app.get("/artists/{artist_id}", response_model=schemas.Artist)
def read_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_id=artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_artist


@app.post("/yt_post/", response_model=schemas.Youtube)
def create_yt_post(yt_post: schemas.YoutubeCreate, db: Session = Depends(get_db)):
    return crud.create_yt_post(db=db, yt_post=yt_post)


@app.get("/yt_posts/", response_model=list[schemas.Youtube])
def read_yt_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    yt_posts = crud.get_yt_posts(db, skip=skip, limit=limit)
    return yt_posts