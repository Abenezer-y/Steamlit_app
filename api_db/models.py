from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.base import ImmutableColumnCollection
from datetime import date
from database import Base

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    band = Column(Boolean, default=True)
    sex = Column(String)
    age = Column(Integer)
    email = Column(String, index=True, unique=True)
    phone = Column(Integer, index=True) 

    
    # fb_profiel = relationship("Facebook", back_populates="artist")
    # twitter_profile = relationship("Tiwtter", back_populates="artist")
    # instagram_profile = relationship("Instagram", back_populates="artist")

class Youtube(Base):
    __tablename__ = "youtube"

    id = Column(Integer, primary_key=True, index=True)
    posted_date = Column(Date, index=True)
    channel = Column(String, index=True)
    artist = Column(String, index=True)
    title = Column(String, index=True)
    duration = Column(String, index=True)
    views = Column(Integer, index=True)
    likes = Column(Integer, index=True)
    link = Column(String)
    collection_date = Column(Date, index=True, default=date.today())

    # comments = relationship("Comment", back_populates="yt_posts")
   

# class Comment(Base):
#     __tablename__ = "comments"

#     id = Column(Integer, primary_key=True, index=True)
#     comment = Column(String, index=True, default="No Comment collected yet.")
#     youtube_id = Column(Integer, ForeignKey("youtube.id"))

#     yt_posts = relationship('Youtube', back_populates='comments')

# class Facebook(Base):
#     __tablename__ = "facebook"

#     id = Column(Integer, primary_key=True, index=True)
#     handel = Column(String, index=True)
#     artist_id = Column(Integer, ForeignKey("artists.id"))
    
#     artist = relationship('Artist', back_populates='fb_profiel')

# class Twitter(Base):
#     __tablename__ = "twitter"

#     id = Column(Integer, primary_key=True, index=True)
#     handel = Column(String, index=True)
#     artist_id = Column(Integer, ForeignKey("artists.id"))
    
#     artist = relationship('Artist', back_populates='twitter_profile')

# class Instagram(Base):
#     __tablename__ = "instagram"

#     id = Column(Integer, primary_key=True, index=True)
#     handel = Column(String, index=True)
#     artist_id = Column(Integer, ForeignKey("artists.id"))
    
#     artist = relationship('Artist', back_populates='instagram_profile')
