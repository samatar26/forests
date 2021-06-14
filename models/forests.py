import sqlalchemy as db

from models import Base


class ForestsModel(Base):
    __tablename__ = "forests"

    name = db.Column(db.String, primary_key=True)
    type = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    country = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    long_description = db.Column(db.String, nullable=False)
    carbon_stored = db.Column(db.Integer, nullable=False)
    carbon_stored_delta = db.Column(db.Integer, nullable=False)
