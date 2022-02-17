import netmiko
from settings import ACS_0120_R0dot1

def create_session(device):
    cisco_router = {
        'device_type': device.device_type,
        'host': device.host,
        'username': device.username,
        'password': device.password,
        'port': device.port,
    }

    session = netmiko.ConnectHandler(**cisco_router)
    return session

def get_interfaces_list(session):
    result = session.send_command('sh int desc')
    result = result.split('\n')
    del result[0]
    inteface_list = []
    for i in result:
        i = i.split(' ')
        inteface_list.append(i[0])
    return inteface_list

def func(active_session, interface_list):
    for i in interface_list:
        active_session.send_command()


def main():
    active_session = create_session(ACS_0120_R0dot1)
    interfaces_list = get_interfaces_list(active_session)
    print(interfaces_list)

    new_int_list = []
    for i in interfaces_list:
        run_int = active_session.send_command('sh run int ' + i)
        if 'switchport mode trunk' in run_int:
            pass
        elif 'shutdown' in run_int:
            pass
        elif i == 'Interface':
            pass
        else:
            new_int_list.append(i)
    print(new_int_list)







if __name__ == '__main__':
    main()