import unittest
from BSTestRunner import BSTestRunner
import time, logging

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Mixpace Test Report', description='Mixpace Android app test report')
    logging.info('生成测试报告')
    runner.run(discover)