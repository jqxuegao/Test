import  requests

class Request():

    # def __init__(self,address,api,request_mode,request_data):
    #     self.address = address
    #     self.api = api
    #     self.request_mode = request_mode
    #     self.request_data = request_data

    def request(address,api,request_mode,request_data):

        if request_mode == 'get':
            re = requests.get(url = address+api,params=request_data)
            return re.status_code

        elif request_mode == 'post':
            headers = {'Content-Type': 'application/json'}
            re = requests.post(url = address+api, data = request_data,headers= headers)
            return re.status_code


if __name__ == '__main__':
    print(Request().request('https://tcc.taobao.com', '/cc/json/mobile_tel_segment.htm?tel=', 'get', 15521177989.0))