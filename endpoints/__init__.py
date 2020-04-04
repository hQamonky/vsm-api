import markdown
import os

# Import the framework
from flask import Flask
from flask_restful import Resource, Api

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)


@app.route('/')
def index():
    # Open README file
    # return "Hello world !"
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


def get_sinks():
    import subprocess
    process = subprocess.run(["pactl", "list", "short", "sinks"], check=True, stdout=subprocess.PIPE,
                             universal_newlines=True)
    data = []
    sinks = process.stdout.split('\n')
    for sink in sinks:
        sink_array = sink.split('\t')
        if len(sink_array) == 5:
            data.append({
                'id': sink_array[0],
                'name': sink_array[1],
                'driver': sink_array[2],
                'sample_specification': sink_array[3],
                'state': sink_array[4]
            })
    return data


class Sinks(Resource):
    @staticmethod
    def get():
        return {'message': 'Success', 'data': get_sinks()}, 200


api.add_resource(Sinks, '/sinks')
