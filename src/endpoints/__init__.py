import markdown
import os

# Import the framework
from flask import Flask
from flask_restful import Resource, Api, reqparse
from src.controller import Controller

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)
con = Controller


# Route shows the README file.
@app.route('/')
def index():
    # Open README file
    # return "Hello world !"
    with open(os.path.dirname(app.root_path) + "/../docs/Api User Guide.md", 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


# Basic endpoints
class Clients(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_clients()}, 200


class Sinks(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_sinks()}, 200


class Sources(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_sources()}, 200


class Cards(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.get_cards()}, 200


api.add_resource(Clients, '/clients')
api.add_resource(Sinks, '/sinks')
api.add_resource(Sources, '/sources')
api.add_resource(Cards, '/cards')


# Contains calls to direct bash commands.
class NativeStats(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_stats()}, 200


class NativeInfo(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_info()}, 200


class NativeSinks(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_sinks()}, 200


class NativeSinksFull(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_full_sinks()}, 200


class NativeSinkInputs(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_sink_inputs()}, 200


class NativeSources(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_sources()}, 200


class NativeSourcesFull(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_full_sources()}, 200


class NativeSourceOutputs(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_source_outputs()}, 200


class NativeCards(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_cards()}, 200


class NativeCardsFull(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_full_cards()}, 200


class NativeClients(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_clients()}, 200


class NativeClientsFull(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_full_clients()}, 200


class NativeModules(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': con.native_get_modules()}, 200


api.add_resource(NativeStats, '/native/stats')
api.add_resource(NativeInfo, '/native/info')

api.add_resource(NativeClients, '/native/clients')
api.add_resource(NativeClientsFull, '/native/clients-full')

api.add_resource(NativeSinks, '/native/sinks')
api.add_resource(NativeSinksFull, '/native/sinks-full')
api.add_resource(NativeSinkInputs, '/native/sink-inputs')

api.add_resource(NativeSources, '/native/sources')
api.add_resource(NativeSourcesFull, '/native/sources-full')
api.add_resource(NativeSourceOutputs, '/native/source-outputs')

api.add_resource(NativeCards, '/native/cards')
api.add_resource(NativeCardsFull, '/native/cards-full')

api.add_resource(NativeModules, '/native/modules')


class LoadModules(Resource):
    @staticmethod
    def post(name):
        # Testing command :
        # pactl load-module module-loopback latency_msec=1 source=alsa_input.pci-0000_00_1f.3.analog-stereo sink=alsa_output.pci-0000_00_1f.3.analog-stereo

        parser = reqparse.RequestParser()

        parser.add_argument('latency_msec', required=True)
        parser.add_argument('source', required=True)
        parser.add_argument('sink', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()
        module_index = con.load_module(name, args)

        return {'message': 'Module loaded.', 'data': module_index}, 201


class UnloadModules(Resource):
    @staticmethod
    def get(identifier):
        # Testing command :
        # pactl unload-module 'index'
        result = con.unload_module(identifier)
        return {'message': 'Module loaded.', 'data': result}, 200


api.add_resource(LoadModules, '/load-module/<string:name>')
api.add_resource(UnloadModules, '/unload-module/<string:identifier>')
