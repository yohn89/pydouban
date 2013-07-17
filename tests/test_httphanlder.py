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

class HttpTest(unittest.TestCase):

    def setUp(self):

        self.headers = { 
            'Host': 'www.baidu.com',
            'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:17.0) Gecko/17.0 Firefox/17.0',
            'Referer': 'http://www.baidu.com',
        }

    def test_get(self):
        http = HttpHanlder(session_key='test',headers=self.headers)
        self.assertTrue( u'百度一下，你就知道' in http.get('http://www.baidu.com'))


if __name__ == '__main__':
    unittest.main()
