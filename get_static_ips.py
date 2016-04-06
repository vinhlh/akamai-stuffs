import socket

countries = ['hk', 'id', 'my', 'ph', 'sg', 'th', 'tw', 'vn']

def get_hosts(country, number):
    name = country + number
    return 'zstatic' + name + '-a.akamaihd.net.edgesuite-staging.net', 'zstatic' + name + '-a.akamaihd.net'

for country in countries:
    hosts = [get_hosts(country, '01'), get_hosts(country, '02')]

    for ping_server, host_name in hosts:
        ip = socket.gethostbyname(ping_server)
        print ip, host_name