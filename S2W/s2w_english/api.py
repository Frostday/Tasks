from flask import Flask
from flask_restful import Resource, Api, reqparse
from s2w import convert_s2w

app = Flask(__name__)
api = Api(app)

class spoken_to_written(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True)
        args = parser.parse_args()
        return convert_s2w(args['text'])

api.add_resource(spoken_to_written, '/spoken_to_written')

app.run()
