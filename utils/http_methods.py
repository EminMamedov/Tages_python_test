import requests

from utils.logger import Logger

class http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=http_methods.headers, cookies=http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        Logger.add_response(result)
        return result

    """"Запрос get для негативного тестирования"""

    headers_negativ = {'Content-Type': ''}

    @staticmethod
    def get_negativ(url):
        Logger.add_request(url, method="GET_NEGATIV")
        result = requests.get(url, headers=http_methods.headers_negativ, cookies=http_methods.cookie)
        Logger.add_response(result)
        return result