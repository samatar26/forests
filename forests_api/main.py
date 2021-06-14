from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from forests_api.dependencies import get_session
from models.forests import ForestsModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Forest(BaseModel):
    name: str
    type: str
    thumbnail: str
    description: str

    country: str
    latitude: int
    longitude: int
    area: int
    long_description: str
    carbon_stored: int
    carbon_stored_delta: int
    cover: str

    class Config:
        orm_mode = True


@app.get("/", response_model=List[Forest])
def read_root(db_session=Depends(get_session)):
    forests = db_session.query(ForestsModel).all()
    return forests
