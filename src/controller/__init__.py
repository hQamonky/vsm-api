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
    def get_sink_inputs():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "sink-inputs"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        sink_inputs = process.stdout.split('\n')
        for sink_input in sink_inputs:
            sink_input_array = sink_input.split('\t')
            if len(sink_input_array) == 5:
                data.append({
                    'id': sink_input_array[0],
                    'sink': sink_input_array[1],
                    'client': sink_input_array[2],
                    'driver': sink_input_array[3],
                    'sample_specification': sink_input_array[4]
                })
        return data

    @staticmethod
    def get_sources():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "sources"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        sources = process.stdout.split('\n')
        for source in sources:
            source_array = source.split('\t')
            if len(source_array) == 5:
                data.append({
                    'id': source_array[0],
                    'name': source_array[1],
                    'driver': source_array[2],
                    'sample_specification': source_array[3],
                    'state': source_array[4]
                })
        return data

    @staticmethod
    def get_source_outputs():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "source-outputs"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        source_outputs = process.stdout.split('\n')
        for source_output in source_outputs:
            source_output_array = source_output.split('\t')
            if len(source_output_array) == 5:
                data.append({
                    'id': source_output_array[0],
                    'source': source_output_array[1],
                    'client': source_output_array[2],
                    'driver': source_output_array[3],
                    'sample_specification': source_output_array[4]
                })
        return data

    @staticmethod
    def get_cards():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "cards"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        cards = process.stdout.split('\n')
        for card in cards:
            card_array = card.split('\t')
            if len(card_array) == 3:
                data.append({
                    'id': card_array[0],
                    'name': card_array[1],
                    'driver': card_array[2]
                })
        return data

    @staticmethod
    def get_clients():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "clients"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        clients = process.stdout.split('\n')
        for client in clients:
            client_array = client.split('\t')
            if len(client_array) == 3:
                data.append({
                    'id': client_array[0],
                    'driver': client_array[1],
                    'application': client_array[2]
                })
        return data

    @staticmethod
    def get_modules():
        import subprocess
        process = subprocess.run(["pactl", "list", "short", "modules"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        modules = process.stdout.split('\n')
        for module in modules:
            module_array = module.split('\t')
            if len(module_array) == 4:
                data.append({
                    'id': module_array[0],
                    'name': module_array[1],
                    'argument': module_array[2],
                    'unknown': module_array[3]
                })
        return data
