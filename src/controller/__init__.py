from src.pbi import PythonBashInterface

pbi = PythonBashInterface


class Controller:
    @staticmethod
    def get_cards():
        cards = pbi.get_cards()
        sinks = Controller.get_sinks()
        sources = Controller.get_sources()

        data = []
        for card in cards:
            card_sinks = []
            for sink in sinks:
                card_device = card['name'].split('.')[1]
                sink_device = sink['name'].split('.')[1]
                if card_device == sink_device:
                    card_sinks.append(sink)

            card_sources = []
            for source in sources:
                if source['name'].startswith(card['name']):
                    card_sources.append(source)

            data.append({
                'id': card['id'],
                'name': card['name'],
                'driver': card['driver'],
                'sinks': card_sinks,
                'sources': card_sources
            })

        return data

    @staticmethod
    def get_sinks():
        con = Controller
        clients = con.get_clients()
        sink_inputs = pbi.get_sink_inputs()
        native_sinks = pbi.get_full_sinks()

        data = []
        for sink in native_sinks:
            sink_number = con.get_key_names(sink)[0].replace('Sink #', '')
            sink = sink["Sink #" + sink_number]
            sink_clients = []
            for sink_input in sink_inputs:
                if sink_input['sink'] == sink_number:
                    for client in clients:
                        client_id = client["number"]
                        if client_id == sink_input['client']:
                            sink_clients.append(client)

            data.append({
                'number': sink_number,
                'name': sink['Name'],
                'description': sink['Description'],
                'driver': sink['Driver'],
                'state': sink['State'],
                'channel_map': sink['Channel Map'],
                'mute': sink['Mute'],
                'volume': con.parse_volume(sink[8]),
                'balance': sink[9].replace('        balance ', ''),
                'base_volume': con.parse_volume_type(sink['Base Volume']),
                'monitor_source': sink['Monitor Source'],
                'latency': sink['Latency'],
                'ports': sink['Ports'],
                'active_port': sink['Active Port'],
                'applications': sink_clients
            })
        return data

    @staticmethod
    def get_sources():
        con = Controller
        clients = con.get_clients()
        source_outputs = pbi.get_source_outputs()
        native_sources = pbi.get_full_sources()

        data = []
        for source in native_sources:
            source_number = con.get_key_names(source)[0].replace('Source #', '')
            source = source["Source #" + source_number]
            source_clients = []
            for source_output in source_outputs:
                if source_output['source'] == source_number:
                    for client in clients:
                        client_id = client["number"]
                        if client_id == source_output['client']:
                            source_clients.append(client)

            data.append({
                'number': source_number,
                'name': source['Name'],
                'description': source['Description'],
                'driver': source['Driver'],
                'state': source['State'],
                'channel_map': source['Channel Map'],
                'mute': source['Mute'],
                'volume': con.parse_volume(source[8]),
                'balance': source[9].replace('        balance ', ''),
                'base_volume': con.parse_volume_type(source['Base Volume']),
                'monitor_of_sink': source['Monitor of Sink'],
                'latency': source['Latency'],
                'applications': source_clients
            })
        return data

    @staticmethod
    def get_clients():
        con = Controller
        full_clients = pbi.get_full_clients()
        data = []
        for client in full_clients:
            client_number = con.get_key_names(client)[0].replace('Client #', '')
            client = client["Client #" + client_number]
            data.append({
                'number': client_number,
                'driver': client['Driver'],
                'owner_module': client['Owner Module'],
                'properties': client['Properties']
            })
        return data

    @staticmethod
    def native_get_stats():
        return pbi.get_stats()

    @staticmethod
    def native_get_info():
        return pbi.get_info()

    @staticmethod
    def native_get_sinks():
        return pbi.get_sinks()

    @staticmethod
    def native_get_full_sinks():
        return pbi.get_full_sinks()

    @staticmethod
    def native_get_sink_inputs():
        return pbi.get_sink_inputs()

    @staticmethod
    def native_get_sources():
        return pbi.get_sources()

    @staticmethod
    def native_get_full_sources():
        return pbi.get_full_sources()

    @staticmethod
    def native_get_source_outputs():
        return pbi.get_source_outputs()

    @staticmethod
    def native_get_cards():
        return pbi.get_cards()

    @staticmethod
    def native_get_full_cards():
        return pbi.get_full_cards()

    @staticmethod
    def native_get_clients():
        return pbi.get_clients()

    @staticmethod
    def native_get_full_clients():
        return pbi.get_full_clients()

    @staticmethod
    def native_get_modules():
        return pbi.get_modules()

    @staticmethod
    def get_key_names(array):
        result = []
        for key in array:
            result.append(key)
        return result

    @staticmethod
    def parse_volume(volume):
        con = Controller
        channels = volume.replace('Volume: ', '').split(',   ')
        data = ''
        tmp_array = []
        for channel in channels:
            channel = channel.split(': ')
            tmp_array.append(channel[0])
            tmp_array.append(channel[1])
        if len(tmp_array) == 2:
            data = {
                tmp_array[0]: con.parse_volume_type(tmp_array[1])
            }
        elif len(tmp_array) == 4:
            data = {
                tmp_array[0]: con.parse_volume_type(tmp_array[1]),
                tmp_array[2]: con.parse_volume_type(tmp_array[3])
            }
        elif len(tmp_array) == 6:
            data = {
                tmp_array[0]: con.parse_volume_type(tmp_array[1]),
                tmp_array[2]: con.parse_volume_type(tmp_array[3]),
                tmp_array[4]: con.parse_volume_type(tmp_array[5])
            }
        return data

    @staticmethod
    def parse_volume_type(volume):
        volumes = volume.split(' / ')
        return {
            'value': volumes[0],
            'percentage': volumes[1].replace('%', ''),
            'db': volumes[2].replace(' dB', '')
        }
