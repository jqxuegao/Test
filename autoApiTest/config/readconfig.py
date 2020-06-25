import configparser


class ReadConfig():
    """定义一个读取配置文件的类"""

    def get_address(self):
        config = configparser.ConfigParser()
        config.read(r"C:\Users\Administrator\PycharmProjects\Test\autoApiTest\config\config.ini")
        value = config.get("EXCEL", "address")
        return value


if __name__ == '__main__':
    print(ReadConfig().get_address())