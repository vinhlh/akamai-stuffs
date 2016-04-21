import socket

countries = ['hk', 'id', 'my', 'ph', 'sg', 'th', 'tw', 'vn']

def get_static_hosts(country):
    return [
        'static-' + country + '.zacdn.com.edgekey-staging.net',
        'static-' + country + '.zacdn.com'
    ]

def get_thumbor_host():
    return [
        'dynamic.zacdn.com.edgekey-staging.net',
        'dynamic.zacdn.com'
    ]

def get_results(hosts):
    for ping_server, host_name in hosts:
        ip = socket.gethostbyname(ping_server)
        print ip, host_name

for country in countries:
    static_hosts = [get_static_hosts(country)]
    get_results(static_hosts)

thumbor_hosts = [get_thumbor_host()]
get_results(thumbor_hosts)
