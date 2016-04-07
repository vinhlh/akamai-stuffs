import socket

countries = ['hk', 'id', 'my', 'ph', 'sg', 'th', 'tw', 'vn']

def get_static_hosts(country, number):
    name = country + number
    return [
        'zstatic' + name + '-a.akamaihd.net.edgesuite-staging.net',
        'zstatic' + name + '-a.akamaihd.net'
    ]

def get_thumbor_host(number):
    return [
        'zthumbor' + number + '-a.akamaihd.net.edgesuite-staging.net',
        'n' + number[1] + '-zthumbor-a.akamaihd.net'
    ]

def get_results(hosts):
    for ping_server, host_name in hosts:
        ip = socket.gethostbyname(ping_server)
        print ip, ping_server, host_name

for country in countries:
    static_hosts = [get_static_hosts(country, '01'), get_static_hosts(country, '02')]
    get_results(static_hosts)

thumbor_hosts = [get_thumbor_host('01'), get_thumbor_host('02')]
get_results(thumbor_hosts)
