from src.pbi import PythonBashInterface

pbi = PythonBashInterface


class Controller:
    @staticmethod
    def get_stats():
        return pbi.get_stats()

    @staticmethod
    def get_info():
        return pbi.get_info()

    @staticmethod
    def get_sinks():
        return pbi.get_sinks()

    @staticmethod
    def get_sink_inputs():
        return pbi.get_sink_inputs()

    @staticmethod
    def get_sources():
        return pbi.get_sources()

    @staticmethod
    def get_source_outputs():
        return pbi.get_source_outputs()

    @staticmethod
    def get_cards():
        return pbi.get_cards()

    @staticmethod
    def get_clients():
        return pbi.get_clients()

    @staticmethod
    def get_modules():
        return pbi.get_modules()
