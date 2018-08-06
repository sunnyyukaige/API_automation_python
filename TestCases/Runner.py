import unittest

from Reporter.HTMLReport import HTMLReporter
from TestCases.CIC import TestCIC


class Runner:
    def testsuite(self):
# get all tests from class
      CIC = unittest.TestLoader().loadTestsFromTestCase(TestCIC)
# create a test suite
      test_suite = unittest.TestSuite([CIC])
      return test_suite

if __name__ == '__main__':
    filePath ='ResReport.html'
    fp = open(filePath,'wb')
    runner = HTMLReporter(
        stream=fp,
        tester="sunny"
        )
    runner.run(Runner().testsuite())