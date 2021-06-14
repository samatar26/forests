from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from forests_api.dependencies import get_session
from models.forests import ForestsModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(db_session=Depends(get_session)):
    forests = db_session.query(ForestsModel).all()
    return forests
