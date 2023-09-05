from core.api_uitl import api_util
from utils.read_data import base_data
from utils.response_util import process_response


def login_query():
     """
     登录接口传参
     :param json_data:
     :param haeders:
     :return:
     """
     json_data = base_data.read_data()['json']
     headers = base_data.read_data()['headers']
     response = api_util.post_login(json=json_data, headers=headers)
     return process_response(response)
