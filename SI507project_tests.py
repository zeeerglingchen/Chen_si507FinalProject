# -*- coding: utf-8 -*-
import unittest
from SI507project_tests import *
from SI507project_tools import *


class Problem1(unittest.TestCase):
    def test_names_file(self):
        with open("1787211337.csv") as csvfile:
            self.assertTrue(csvfile is not None,"testing that file exists")
            cont = csvfile.read()
            self.assertTrue("Type" in cont.split("\n")[0])
            self.assertTrue("id" in cont)
            csvfile.close()



if __name__ == "__main__":
    unittest.main(verbosity=2)
