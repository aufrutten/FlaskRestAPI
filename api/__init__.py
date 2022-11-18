from flask_restful import Resource
from flask import request
import json


def dict_to_xml(data, root='XML'):
    """function for convert dict:python in XML"""
    xml = f'<{root}>'
    if isinstance(data, dict):
        for key, value in data.items():
            xml += dict_to_xml(value, key)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            xml += dict_to_xml(item, 'item')

    else:
        xml += str(data)

    xml += f'</{root}>'
    return xml


def get_class_parser(parser, version):
    """getting class of module, which class is version, and module that parser"""

    import importlib
    try:
        # check if module and class exist
        class_module = importlib.import_module(f'{__name__}.{parser}').__dict__[version]

    except ModuleNotFoundError:
        return {'status_code': 404, 'message': 'you wrote uncorrected parser?'}

    except KeyError:
        return {'status_code': 404, 'message': 'you wrote uncorrected version for parser?'}

    else:
        return {'status_code': 200, version: class_module}


def return_response(version, parser, req_format, method):
    """function for return response, check status_code and format in which must return"""

    parser = get_class_parser(parser, version)
    if parser['status_code'] == 200:
        if req_format == 'JSON':
            return json.dumps(parser[version].__dict__[method]())
        elif req_format == 'XML':
            return dict_to_xml(parser[version].__dict__[method]())
        else:
            return json.dumps({'status_code': 404, 'message': 'you wrote uncorrected format, JSON or XML'})
    else:
        return json.dumps(parser)


class API(Resource):

    def get(self, path):
        """method of API HTTP GET"""
        version, parser, *_ = path.split('/')
        req_format = request.values.get('format')

        if not (parser and version and req_format):
            return json.dumps({'status_code': 404, 'message': 'you forgot to specify required arguments'})

        return return_response(version, parser, req_format, 'get')

