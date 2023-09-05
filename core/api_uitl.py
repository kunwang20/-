from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    #请求地址
    def post_login(self, **kwargs):
        return self.post("/dl/login", **kwargs)


api_util = Api()