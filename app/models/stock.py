from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.application import db

class Stock(db.Model):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    stock_type = Column(Integer)
    quantity = Column(Integer)
    price = Column(Integer)
    quanlity = Column(String(30))
    description = Column(Text())
    stock_image_url = Column(Text())

    color = relationship('Color')
    designer = relationship('Designer')
    size = relationship('Size')
    fabric = relationship('Fabric')

    order = relationship('Order', back_populates='stock', uselist=False)


'''one to many relationship Stock-Color'''
class Color(db.Model):
    __tablename__ = 'color'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    color = Column(String(50))

    def __repr__(self):
        return '<Color %r>' % self.color


'''one to many relationship Stock-Designer'''
class Designer(db.Model):
    __tablename__ = 'designer'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    designer = Column(String(50))

    def __repr__(self):
        return '<Designer %r>' % self.designer


'''one to many relationship Stock-Size'''
class Size(db.Model):
    __tablename__ = 'size'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    size = Column(String(50))

    def __repr__(self):
        return '<Size %r>' % self.size


'''one to many relationship Stock-Fabric'''
class Fabric(db.Model):
    __tablename__ = 'fabric'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    fabric = Column(String(50))

    def __repr__(self):
        return '<Fabric %r>' % self.fabric
