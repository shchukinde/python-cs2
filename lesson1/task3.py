# Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
# (использовать модуль tabulate).

import locale
import platform
import ipaddress
from subprocess import Popen, PIPE
from tabulate import tabulate

ENCODING = locale.getpreferredencoding()

def host_ping(host_list):

    param = '-n' if platform.system().lower() == 'windows' else '-c'

    dict_result = {'Reachable':[], 'Unreachable':[]}

    for host in host_list:

        try:
            addr = ipaddress.ip_address(host)
        except ValueError:
            addr = host

        args = ['ping', param, '3', str(addr)]
        reply = Popen(args, stdout=PIPE, stderr=PIPE)

        code = reply.wait()
        if code == 0:
            dict_result['Reachable'].append(host)
        else:
            dict_result['Unreachable'].append(host)

    print(tabulate(dict_result, headers='keys', tablefmt="pipe"))

    return "end"


def host_range_ping_tab(ip_addr, range_ip):

    if int(ip_addr.split('.')[3]) + range_ip > 254:
        print('Указан слишком большой диапазон')
        return False
    else:
        ipv4 = ipaddress.ip_address(ip_addr)

        addr_list = []
        for i in range(range_ip):
            addr_list.append(str(ipv4 + i))

        host_ping(addr_list)


host_range_ping_tab('192.168.1.1', 3)
