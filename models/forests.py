import sqlalchemy as db

from models import Base


class ForestsModel(Base):
    __tablename__ = "forests"

    name = db.Column(db.String, primary_key=True)
    type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
