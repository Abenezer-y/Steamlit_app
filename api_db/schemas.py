from datetime import date
from typing import Optional
from pydantic import BaseModel

# class CommentBase(BaseModel):
#     comment: Optional[str] = None

# class CommentCreate(CommentBase):
#     pass

# class Comment(CommentBase):
    # id: int
    # youtube_id: int

    # class Config:
    #     orm_mode = True

class YoutubeBase(BaseModel):
    posted_date: date
    channel: str
    artist: str
    title: str
    duration: str
    views: int
    likes: int
    link: str

class YoutubeCreate(YoutubeBase):
    pass

class Youtube(YoutubeBase):
    id: int
    # comments: list[Comment] = []

    class Config:
        orm_mode = True

# class FacebookBase(BaseModel):
#     handel: str

# class FacebookCreate(FacebookBase):
#     pass

# class Facebook(FacebookBase):
#     id: int
#     artist_id: int

#     class Config:
#         orm_mode = True

# class TwitterBase(BaseModel):
#     handel: str

# class TwitterCreate(TwitterBase):
#     pass

# class Twitter(TwitterBase):
#     id: int
#     artist_id: int

#     class Config:
#         orm_mode = True

# class InstagramBase(BaseModel):
#     handel: str

# class InstagramCreate(InstagramBase):
#     pass

# class Instagram(InstagramBase):
#     id: int
#     artist_id: int

#     class Config:
#         orm_mode = True

class ArtistBase(BaseModel):
    name: str
    band: bool
    sex: str
    age:int
    email: str
    phone: int

class ArtistCreate(ArtistBase):
    pass

class Artist(YoutubeBase):
    id: int
    # yt_posts: list[Youtube] = []
    # fb_profiel: list[Facebook] = []
    # twitter_profile: list[Twitter] = []
    # instagram_profile: list[Instagram] = []

    class Config:
        orm_mode = True