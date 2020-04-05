class PythonBashInterface:
    # pactl stat
    @staticmethod
    def get_stats():
        import subprocess
        process = subprocess.run(["pactl", "stat"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        stats = process.stdout.split('\n')
        for stat in stats:
            data.append(stat)
        return data

    # pactl info
    @staticmethod
    def get_info():
        import subprocess
        process = subprocess.run(["pactl", "info"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        info = process.stdout.split('\n')
        for element in info:
            data.append(element)
        return data

    # pactl list short sinks
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

    # pactl list sinks
    @staticmethod
    def get_full_sinks():
        import subprocess
        pbi = PythonBashInterface
        process = subprocess.run(["pactl", "list", "sinks"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        sinks = process.stdout.split('\n\n')
        for sink in sinks:
            lines = sink.split('\n')
            sink_data = pbi.lines_to_object(lines)
            data.append(sink_data)
        return data

    # pactl list short sink-inputs
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

    # pactl list short sources
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

    # pactl list short source-outputs
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

    # pactl list short cards
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

    # pactl list cards
    @staticmethod
    def get_full_cards():
        import subprocess
        pbi = PythonBashInterface
        process = subprocess.run(["pactl", "list", "cards"], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        data = []
        cards = process.stdout.split('\n\n')
        for card in cards:
            lines = card.split('\n')
            card_data = pbi.lines_to_object(lines)
            data.append(card_data)
        return data

    @staticmethod
    def get_layer(line):
        count = 0
        while line.startswith('\t'):
            count += 1
            line = line[1:]
        return count

    # pactl list short clients
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

    # pactl list short modules
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

    @staticmethod
    def lines_to_object(lines):
        pbi = PythonBashInterface
        lines = lines[:-1]
        final_string = "{"
        i = 0
        current_layer = 0
        indexes = [0]
        handling_error = False
        error_layer = 0
        for line in lines:
            line = line[current_layer:]
            if line.endswith(':'):
                line = line[:-1]
            if i+1 < len(lines):
                next_layer = pbi.get_layer(lines[i+1])
                if next_layer-current_layer == 0:
                    line = str(indexes[current_layer]) + ":'" + line + "',"
                    indexes[current_layer] += 1
                elif next_layer-current_layer == 1:
                    line = "'" + line + "':{"
                    if current_layer+1 >= len(indexes):
                        indexes.append(0)
                elif next_layer-current_layer == -1:
                    line = str(indexes[current_layer]) + ":'" + line + "'},"
                    indexes[current_layer] = 0
                else:
                    print('ERROR: next_layer-current_layer = ' + str(next_layer-current_layer) + " - line = " + line)
                    if not handling_error:
                        if pbi.get_layer(lines[i+2]) == 1:
                            line = "'" + line
                            if current_layer + 1 >= len(indexes):
                                indexes.append(0)
                        else:
                            line = str(indexes[current_layer]) + ":'" + line
                        error_layer = next_layer - current_layer
                    else:
                        error_layer = next_layer - abs(error_layer)
                        if error_layer == 0:
                            line = line + "',"
                            indexes[current_layer] += 1
                        elif error_layer == 1:
                            line = line + "':{"
                            if current_layer+1 >= len(indexes):
                                indexes.append(0)
                        elif error_layer == -1:
                            line = line + "'},"
                            indexes[current_layer] = 0

                    handling_error = not handling_error

                final_string = final_string + line
                current_layer = next_layer
                i += 1
            else:
                final_string = final_string + str(indexes[current_layer]) + ":'" + line + "'"\
                               + ("}" * (current_layer+1))
        return eval(final_string)
