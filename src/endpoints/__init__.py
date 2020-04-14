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


class LoadModules(Resource):
    @staticmethod
    def post(name):
        # Testing command : pactl load-module module-loopback latency_msec=1
        # source=alsa_input.pci-0000_00_1f.3.analog-stereo sink=alsa_output.pci-0000_00_1f.3.analog-stereo

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


class SetCardProfile(Resource):
    @staticmethod
    def get(card, profile):
        return {'message': 'Success', 'data': con.set_card_profile(card, profile)}, 200


class SetDefaultSink(Resource):
    @staticmethod
    def get(sink):
        return {'message': 'Success', 'data': con.set_default_sink(sink)}, 200


class SetSinkPort(Resource):
    @staticmethod
    def get(sink, port):
        return {'message': 'Success', 'data': con.set_sink_port(sink, port)}, 200


class SetSinkVolumePercentage(Resource):
    @staticmethod
    def get(sink, volume):
        return {'message': 'Success', 'data': con.set_sink_volume_percentage(sink, volume)}, 200


class SetSinkInputVolumePercentage(Resource):
    @staticmethod
    def get(sink_input, volume):
        return {'message': 'Success', 'data': con.set_sink_input_volume_percentage(sink_input, volume)}, 200


class SetSinkMute(Resource):
    @staticmethod
    def get(sink, mute):
        if mute == 'true':
            mute = 1
        elif mute == 'false':
            mute = 0
        elif mute == 'toggle':
            mute = mute
        else:
            return {'message': "Wrong mute value. Must be 'true', 'false' or 'toggle'.", 'data': 'error'}, 404
        return {'message': 'Success', 'data': con.set_sink_mute(sink, mute)}, 200


class SetSinkInputMute(Resource):
    @staticmethod
    def get(sink_input, mute):
        if mute == 'true':
            mute = 1
        elif mute == 'false':
            mute = 0
        elif mute == 'toggle':
            mute = mute
        else:
            return {'message': "Wrong mute value. Must be 'true', 'false' or 'toggle'.", 'data': 'error'}, 404
        return {'message': 'Success', 'data': con.set_sink_input_mute(sink_input, mute)}, 200


class SetDefaultSource(Resource):
    @staticmethod
    def get(source):
        return {'message': 'Success', 'data': con.set_default_source(source)}, 200


class SetSourcePort(Resource):
    @staticmethod
    def get(source, port):
        return {'message': 'Success', 'data': con.set_source_port(source, port)}, 200


class SetSourceVolumePercentage(Resource):
    @staticmethod
    def get(source, volume):
        return {'message': 'Success', 'data': con.set_source_volume_percentage(source, volume)}, 200


class SetSourceOutputVolumePercentage(Resource):
    @staticmethod
    def get(source_output, volume):
        return {'message': 'Success', 'data': con.set_source_output_volume_percentage(source_output, volume)}, 200


class SetSourceMute(Resource):
    @staticmethod
    def get(source, mute):
        if mute == 'true':
            mute = 1
        elif mute == 'false':
            mute = 0
        elif mute == 'toggle':
            mute = mute
        else:
            return {'message': "Wrong mute value. Must be 'true', 'false' or 'toggle'.", 'data': 'error'}, 404
        return {'message': 'Success', 'data': con.set_source_mute(source, mute)}, 200


class SetSourceOutputMute(Resource):
    @staticmethod
    def get(source_output, mute):
        if mute == 'true':
            mute = 1
        elif mute == 'false':
            mute = 0
        elif mute == 'toggle':
            mute = mute
        else:
            return {'message': "Wrong mute value. Must be 'true', 'false' or 'toggle'.", 'data': 'error'}, 404
        return {'message': 'Success', 'data': con.set_source_output_mute(source_output, mute)}, 200


api.add_resource(Cards, '/cards')
api.add_resource(SetCardProfile, '/card/<string:card>/set-profile/<string:profile>')

api.add_resource(LoadModules, '/load-module/<string:name>')
api.add_resource(UnloadModules, '/unload-module/<string:identifier>')

api.add_resource(Sinks, '/sinks')
api.add_resource(SetDefaultSink, '/sink/<string:sink>/set-default')
api.add_resource(SetSinkPort, '/sink/<string:sink>/set-port/<string:port>')
api.add_resource(SetSinkVolumePercentage, '/sink/<string:sink>/set-volume-percentage/<string:volume>')
api.add_resource(SetSinkMute, '/sink/<string:sink>/set-mute/<string:mute>')

api.add_resource(SetSinkInputVolumePercentage, '/sink-input/<string:sink_input>/set-volume-percentage/<string:volume>')
api.add_resource(SetSinkInputMute, '/sink-input/<string:sink_input>/set-mute/<string:mute>')

api.add_resource(Sources, '/sources')
api.add_resource(SetDefaultSource, '/source/<string:source>/set-default')
api.add_resource(SetSourcePort, '/source/<string:source>/set-port/<string:port>')
api.add_resource(SetSourceVolumePercentage, '/source/<string:source>/set-volume-percentage/<string:volume>')
api.add_resource(SetSourceMute, '/source/<string:source>/set-mute/<string:mute>')

api.add_resource(SetSourceOutputVolumePercentage, '/source-output/<string:source_output>/set-volume-percentage'
                                                  '/<string:volume>')
api.add_resource(SetSourceOutputMute, '/source-output/<string:source_output>/set-mute/<string:mute>')

api.add_resource(Clients, '/clients')


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
