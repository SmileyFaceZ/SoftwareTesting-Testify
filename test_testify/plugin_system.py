class ReportingPlugin:
    def report_result(self, result):
        pass  # Placeholder method for reporting results


class TestifyReporter:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    def run_tests(self, test_suite):
        for test in test_suite:
            result = test.run()
            self.report_result(result)

    def report_result(self, result):
        for plugin in self.plugins:
            plugin.report_result(result)