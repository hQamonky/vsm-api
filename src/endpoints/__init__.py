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
con = Controller


@app.route('/')
def index():
    # Open README file
    # return "Hello world !"
    with open(os.path.dirname(app.root_path) + '/../README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


class Stats(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_stats()}, 200


class Info(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_info()}, 200


class Sinks(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_sinks()}, 200


class SinkInputs(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_sink_inputs()}, 200


class Sources(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_sources()}, 200


class SourceOutputs(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_source_outputs()}, 200


class Cards(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_cards()}, 200


class Clients(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_clients()}, 200


class Modules(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_modules()}, 200


api.add_resource(Stats, '/stats')
api.add_resource(Info, '/info')
api.add_resource(Sinks, '/sinks')
api.add_resource(SinkInputs, '/sink-inputs')
api.add_resource(Sources, '/sources')
api.add_resource(SourceOutputs, '/source-outputs')
api.add_resource(Cards, '/cards')
api.add_resource(Clients, '/clients')
api.add_resource(Modules, '/modules')
