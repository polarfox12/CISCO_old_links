import netmiko
from settings import devices


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
    interface_list = []
    for i in result:
        if 'up' in i or 'admin down' in i or 'Interface' in i:
            pass
        else:
            i = i.split(' ')
            interface_list.append(i[0])
    return interface_list


def main():
    for d in devices:
        active_session = create_session(d)
        interfaces_list = get_interfaces_list(active_session)
        print(d.name, interfaces_list)


if __name__ == '__main__':
    main()
