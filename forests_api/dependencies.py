from forests_api.db import Session


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
