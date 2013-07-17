#encoding:utf-8
"""
Copyright 2013 TY<tianyu0915@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

""" Test Case 
"""

import unittest
from pydouban.client import DoubanClient
from configs import USERNAME,PASSWORD

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = DoubanClient(USERNAME,PASSWORD)

    def test_login(self):
        self.assertTrue(self.client.login())

    def test_get_topics(self):
        list = self.client.get_topics()
        self.assertTrue(list)
        self.assertTrue(len(list)==50)



if __name__ == '__main__':
    unittest.main()
