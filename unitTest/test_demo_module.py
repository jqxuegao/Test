import HTMLReport
import unittest
from test_demo_class import TestDemo

tests = [TestDemo("test_add"), TestDemo("test_div"), TestDemo("test_add_with_skip")]
for name in tests:
    unittest.TestCase().addTest(name)