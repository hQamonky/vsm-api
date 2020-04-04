import markdown
import os

# Import the framework
from flask import Flask
from flask_restful import Resource, Api
from src.controller import Controller

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)


@app.route('/')
def index():
    # Open README file
    # return "Hello world !"
    with open(os.path.dirname(app.root_path) + '/../README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


class Sinks(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': Controller.get_sinks()}, 200


class Sources(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': Controller.get_sources()}, 200


api.add_resource(Sinks, '/sinks')
api.add_resource(Sources, '/sources')
