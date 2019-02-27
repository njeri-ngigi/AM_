from flask_restplus import Resource

class Home(Resource):
  def get(self):
    return "wassup world!"
    