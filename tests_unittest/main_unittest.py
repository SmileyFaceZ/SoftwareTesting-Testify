import unittest
from unittest_plugin_system import ReportingPlugin, UnittestRunner
from test_example_unittest import ExampleTest

class CustomReporterPlugin(ReportingPlugin):
    def report_result(self, test_case, result):
        for test_result in result.failures + result.errors:
            test_name = test_result[0].id() if hasattr(test_result[0], 'id') else str(test_result[0])
            print("Custom report:", test_name, test_result[1])

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ExampleTest)
    runner = UnittestRunner(plugins=[CustomReporterPlugin()])
    runner.run(suite)