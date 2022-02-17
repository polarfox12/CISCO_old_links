import os
import dotenv

dotenv.load_dotenv('.env')

# ACCOUNT
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

# DEVICES_IP_ADDRESSES
ip_R0dot1 = os.environ['R0dot1']
ip_R0dot2 = os.environ['R0dot2']


class Device(object):

    def __init__(self, device_type, host, username, password, port):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.port = port


devices = []
R0dot1 = Device('cisco_ios', ip_R0dot1, LOGIN, PASSWORD, 22)
R0dot2 = Device('cisco_ios', ip_R0dot2, LOGIN, PASSWORD, 22)

devices.append(R0dot1)
devices.append(R0dot2)

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.20.245.101',
    'username': 'sorokin.k',
    'password': 'T1p0svitch99',
    #    'secret': 'enablepass',
    'port': 22,
}
