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
