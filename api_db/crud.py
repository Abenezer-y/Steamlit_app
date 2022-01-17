from sqlalchemy.orm import Session

import models, schemas


def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()

def get_artist_by_email(db: Session, email: str):
    return db.query(models.Artist).filter(models.Artist.email == email).first()

def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).offset(skip).limit(limit).all()

def create_artist(db: Session, artist: schemas.ArtistCreate):
    db_artist = models.Artist(**artist.dict())  
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_yt_post(db: Session, post_id: int):
    return db.query(models.Youtube).filter(models.Youtube.id == post_id).first()

def get_yt_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Youtube).offset(skip).limit(limit).all()

def create_yt_post(db: Session, yt_post: schemas.YoutubeCreate):
    db_yt_post = models.Youtube(**yt_post.dict())  
    db.add(db_yt_post)
    db.commit()
    db.refresh(db_yt_post)
    return db_yt_post


