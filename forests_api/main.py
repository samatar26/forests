from fastapi import Depends, FastAPI

from forests_api.dependencies import get_session
from models.forests import ForestsModel

app = FastAPI()


@app.get("/")
def read_root(db_session=Depends(get_session)):
    forests = db_session.query(ForestsModel).all()
    return forests
