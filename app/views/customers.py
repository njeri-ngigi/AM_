from flask_restplus import Resource
from flask import request, jsonify

class Customers(Resource):
  def get(self):
    return "Yee customers!"

  def post(self):
    data = request.json()
    return {"msg": data}
    