class Controller:
    @staticmethod
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

    @staticmethod
    def get_sources():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "sources"], check=True, stdout=subprocess.PIPE,
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
