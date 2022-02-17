import os
import dotenv

dotenv.load_dotenv('.env')

LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']
R0dot1 = os.environ['R0dot1']



class Device(object):

    def __init__(self, device_type, host, username, password, port):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.port = port


ACS_0120_R0dot1 = Device('cisco_ios', R0dot1, LOGIN, PASSWORD, 22)

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.20.245.101',
    'username': 'sorokin.k',
    'password': 'T1p0svitch99',
    #    'secret': 'enablepass',
    'port': 22,
}
