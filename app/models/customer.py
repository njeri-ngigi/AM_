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
    balance = Column(Integer)

    sizes = relationship('Sizes', uselist=False, back_populates="customer")
    colors = relationship('Colors')
    fabrics = relationship('Fabrics')
    designer = relationship('Designers')

    def __repr__(self):
        return '<User %r>' % self.name

class Sizes(db.Model):
    __tablename__ = 'sizes'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="sizes")

    trousers = Column(Float)
    blazers = Column(Float)
    shirts = Column(Float)
    shoes = Column(Float)
    jackets = Column(Float)

    def __repr__(self):
        return '<Sizes %r>' % self.id


class Colors(db.Model):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    
    color = Column(String(50))

    def __repr__(self):
        return '<Colors %r>' % self.color


class Fabrics(db.Model):
    __tablename__ = 'fabrics'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    
    fabric = Column(String(50))

    def __repr__(self):
        return '<Fabrics %r>' % self.fabric


class Designers(db.Model):
    __tablename__ = 'designers'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    
    designer = Column(String(50))

    def __repr__(self):
        return '<Designers %r>' % self.designer
