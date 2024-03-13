from plugin_system import ReportingPlugin, TestifyReporter
from test_example import ExampleTest


class CustomReporterPlugin(ReportingPlugin):
    def report_result(self, result):
        print("Custom report:", result)


if __name__ == "__main__":
    reporter = TestifyReporter()
    reporter.register_plugin(CustomReporterPlugin())
    reporter.run_tests([ExampleTest()])