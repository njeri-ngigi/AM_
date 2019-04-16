from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.application import db


'''one to many relationship Customer-Orders'''
class Order(db.Model):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    amount_paid = Column(Float)
    balance = Column(Float)
    discount = Column(Float)
    status = Column(Integer)

    customer_id = Column(Integer, ForeignKey('customer.id'))
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = relationship('Stock', back_populates='order')
