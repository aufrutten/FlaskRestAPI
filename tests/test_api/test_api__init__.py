import requests

import sys
import pathlib

WORK_DIR_OF_PROJECT = pathlib.Path(__file__).parent.parent.parent
sys.path.append(WORK_DIR_OF_PROJECT)
import api


class TestDictToXML:

    def test_main_case(self):
        assert api.dict_to_xml({'name': 'John'}) == '<XML><name>John</name></XML>'

    def test_other_case(self):
        assert api.dict_to_xml(('name', 'John')) == '<XML><item>name</item><item>John</item></XML>'


class TestGetClassParser:

    def test_main_case(self):
        pass


class TestReturnResponse:

    def test_main_case(self):
        pass


class TestAPI:

    def test_main_case(self):
        pass


# r = requests.post('http://127.0.0.1:5000/api/ihor')
# print(requests.get('http://127.0.0.1:5000/api/V1/report/?format=JSON').json())
# print(requests.get('http://127.0.0.1:5000/api/V1/report/?format=JSON').json())
# print(requests.get('http://127.0.0.1:5000/api/V1/report/?format=XML').text)
