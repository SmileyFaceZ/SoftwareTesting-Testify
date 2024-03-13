import unittest


class ReportingPlugin:
    def report_result(self, test_case, result):
        pass  # Placeholder method for reporting results


class UnittestRunner(unittest.TextTestRunner):
    def __init__(self, plugins=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plugins = plugins or []

    def run(self, test):
        result = super().run(test)
        for plugin in self.plugins:
            plugin.report_result(test, result)
        return result