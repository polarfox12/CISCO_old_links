import os
import dotenv

dotenv.load_dotenv('.env')

# ACCOUNT
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

# DEVICES_IP_ADDRESSES
ip_R0dot1 = os.environ['R0dot1']
ip_R0dot2 = os.environ['R0dot2']

ip_R1dot1 = os.environ['R1dot1']
ip_R1dot2 = os.environ['R1dot2']
ip_R1dot3 = os.environ['R1dot3']
ip_R1dot4 = os.environ['R1dot4']
ip_R1dot5 = os.environ['R1dot5']
ip_R1dot6 = os.environ['R1dot6']
ip_R1dot7 = os.environ['R1dot7']
ip_R1dot8 = os.environ['R1dot8']
ip_R1dot9 = os.environ['R1dot9']


class Device(object):

    def __init__(self, device_type, host, username, password, name, port):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.name = name


devices = []
R0dot1 = Device('cisco_ios', ip_R0dot1, LOGIN, PASSWORD, 'R0dot1', 22)
R0dot2 = Device('cisco_ios', ip_R0dot2, LOGIN, PASSWORD, 'R0dot2', 22)

R1dot1 = Device('cisco_ios', ip_R1dot1, LOGIN, PASSWORD, 'R1dot1', 22)
R1dot2 = Device('cisco_ios', ip_R1dot2, LOGIN, PASSWORD, 'R1dot2', 22)
R1dot3 = Device('cisco_ios', ip_R1dot3, LOGIN, PASSWORD, 'R1dot3', 22)
R1dot4 = Device('cisco_ios', ip_R1dot4, LOGIN, PASSWORD, 'R1dot4', 22)
R1dot5 = Device('cisco_ios', ip_R1dot5, LOGIN, PASSWORD, 'R1dot5', 22)
R1dot6 = Device('cisco_ios', ip_R1dot6, LOGIN, PASSWORD, 'R1dot6', 22)
R1dot7 = Device('cisco_ios', ip_R1dot7, LOGIN, PASSWORD, 'R1dot7', 22)
R1dot8 = Device('cisco_ios', ip_R1dot8, LOGIN, PASSWORD, 'R1dot8', 22)
R1dot9 = Device('cisco_ios', ip_R1dot9, LOGIN, PASSWORD, 'R1dot9', 22)

devices.append(R0dot1)
devices.append(R0dot2)

devices.append(R1dot1)
devices.append(R1dot2)
devices.append(R1dot3)
devices.append(R1dot4)
devices.append(R1dot5)
devices.append(R1dot6)
devices.append(R1dot7)
devices.append(R1dot8)
devices.append(R1dot9)


cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.20.245.101',
    'username': 'sorokin.k',
    'password': 'T1p0svitch99',
    #    'secret': 'enablepass',
    'port': 22,
}
