from flask_restplus import Resource

class Stock(Resource):
  def get(self):
    return "Yee stock!"

  def post(self):
    return "Added me stock here"