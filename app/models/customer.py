from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.application import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True)
    phoneNumber = Column(String(120), unique=True, nullable=False)
    profilePicture = Column(Text())

    order = relationship('Order')

    def __repr__(self):
        return '<User %r>' % self.name
