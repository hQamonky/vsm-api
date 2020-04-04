from src.pbi import PythonBashInterface

pbi = PythonBashInterface


class Controller:
    @staticmethod
    def get_cards():
        # cards = pbi.get_cards()
        # sinks = pbi.get_sinks()
        # sink_inputs = pbi.get_sink_inputs()
        # sources = pbi.get_sources()
        # source_outputs = pbi.get_source_outputs()
        # clients = pbi.get_clients()
        #
        # data = []
        # for card in cards:

        return "Work in progress!"

    @staticmethod
    def get_sinks():
        sinks = pbi.get_sinks()
        sink_inputs = pbi.get_sink_inputs()
        clients = pbi.get_clients()

        data = []
        for sink in sinks:
            sink_clients = []
            for sink_input in sink_inputs:
                if sink_input['sink'] == sink['id']:
                    for client in clients:
                        if client['id'] == sink_input['client']:
                            sink_clients.append({'id': client['id'],
                                                 'application': client['application']})
            data.append({
                'id': sink['id'],
                'name': sink['name'],
                'driver': sink['driver'],
                'state': sink['state'],
                'applications': sink_clients
            })

        # TODO : replace id in array by actual sink id. Then add null to missing ids. And do the same for clients.

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
    def native_get_sink_inputs():
        return pbi.get_sink_inputs()

    @staticmethod
    def native_get_sources():
        return pbi.get_sources()

    @staticmethod
    def native_get_source_outputs():
        return pbi.get_source_outputs()

    @staticmethod
    def native_get_cards():
        return pbi.get_cards()

    @staticmethod
    def native_get_clients():
        return pbi.get_clients()

    @staticmethod
    def native_get_modules():
        return pbi.get_modules()
