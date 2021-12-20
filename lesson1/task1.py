# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов. Аргументом
# функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

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


print(host_ping(['yandex.ru', '8.8.8.8', 'heheheh.hehe']))
