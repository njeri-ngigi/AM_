from app.application import api
from app.views import Customers, Home, Stock

api.add_resource(Home, '/')
api.add_resource(Customers, '/api/v1/am/customers')
api.add_resource(Stock, '/api/v1/am/stock')
