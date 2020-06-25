import  requests

class Request():

    # def __init__(self,address,api,request_mode,request_data):
    #     self.address = address
    #     self.api = api
    #     self.request_mode = request_mode
    #     self.request_data = request_data

    def request(self,apidata):

        address = apidata['地址']
        api = apidata['接口']
        request_mode = apidata['请求方式']
        request_data = apidata['请求内容']

        if request_mode == 'get':
            re = requests.get(url = address+api,params=request_data)
            return re.status_code

        elif request_mode == 'post':
            headers = {'Content-Type': 'application/json'}
            re = requests.post(url = address+api, data = request_data,headers= headers)
            return re.status_code


if __name__ == '__main__':
    Request().request( 'http://10.68.62.22/',  'api/api/v1/user/login',  'post', '{"loginName":"admin", "password":"admin"}')