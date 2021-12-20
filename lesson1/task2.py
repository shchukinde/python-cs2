# Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.

import locale
import platform
import ipaddress
from subprocess import Popen, PIPE

ENCODING = locale.getpreferredencoding()

def host_ping(host_list):

    param = '-n' if platform.system().lower() == 'windows' else '-c'

    dict_result = {}

    for host in host_list:

        try:
            addr = ipaddress.ip_address(host)
        except ValueError:
            addr = host

        args = ['ping', param, '3', str(addr)]
        reply = Popen(args, stdout=PIPE, stderr=PIPE)

        code = reply.wait()
        if code == 0:
            print(f'{host} доступен')
            dict_result[host] = 'доступен'
        else:
            print(f'{host} не доступен')
            dict_result[host] = 'не доступен'

    return "end"


def host_range_ping(ip_addr, range_ip):

    if int(ip_addr.split('.')[3]) + range_ip > 254:
        print('Указан слишком большой диапазон')
        return False
    else:
        ipv4 = ipaddress.ip_address(ip_addr)

        addr_list = []
        for i in range(range_ip):
            addr_list.append(str(ipv4 + i))

        host_ping(addr_list)


host_range_ping('192.168.1.250', 2)
