import requests

from testcase.test_Login import test_login


def test_getInfo():
    token = test_login()
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
    }
    res = requests.get(url="", headers=headers, )
    print(res.json())
