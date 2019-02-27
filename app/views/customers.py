from flask_restplus import Resource

class Customers(Resource):
  def get(self):
    return "Yee customers!"

  def post(self):
    return "Added me customer here"