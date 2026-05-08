from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Webtoon Community MVP")

class Series(BaseModel):
    id: int
    title: str
    platform: str
    genre: str

class Character(BaseModel):
    id: int
    series_id: int
    name: str
    description: str

class PostCreate(BaseModel):
    title: str
    body: str
    spoiler: bool = False
    series_id: Optional[int] = None
    character_id: Optional[int] = None

class Post(PostCreate):
    id: int

SERIES: List[Series] = [
    Series(id=1, title="전지적 독자 시점", platform="네이버", genre="판타지"),
    Series(id=2, title="나 혼자만 레벨업", platform="카카오", genre="액션"),
]

CHARACTERS: List[Character] = [
    Character(id=1, series_id=1, name="김독자", description="독자이자 주인공"),
    Character(id=2, series_id=2, name="성진우", description="헌터"),
]

POSTS: List[Post] = []
post_seq = 1


@app.get("/")
def root():
    return {
        "message": "웹툰 통합 커뮤니티 MVP API",
        "docs": "/docs",
        "endpoints": ["/series", "/characters", "/posts"],
    }


@app.get("/series", response_model=List[Series])
def list_series(q: Optional[str] = None):
    if not q:
        return SERIES
    return [s for s in SERIES if q.lower() in s.title.lower()]


@app.get("/series/{series_id}", response_model=Series)
def get_series(series_id: int):
    for s in SERIES:
        if s.id == series_id:
            return s
    raise HTTPException(status_code=404, detail="Series not found")


@app.get("/characters", response_model=List[Character])
def list_characters(series_id: Optional[int] = None):
    if series_id is None:
        return CHARACTERS
    return [c for c in CHARACTERS if c.series_id == series_id]


@app.get("/posts", response_model=List[Post])
def list_posts(series_id: Optional[int] = None, character_id: Optional[int] = None):
    result = POSTS
    if series_id is not None:
        result = [p for p in result if p.series_id == series_id]
    if character_id is not None:
        result = [p for p in result if p.character_id == character_id]
    return result


@app.post("/posts", response_model=Post)
def create_post(payload: PostCreate):
    global post_seq
    if payload.series_id is None and payload.character_id is None:
        raise HTTPException(status_code=400, detail="series_id or character_id is required")

    post = Post(id=post_seq, **payload.dict())
    POSTS.append(post)
    post_seq += 1
    return post
