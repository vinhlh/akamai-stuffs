# to use hyper in MacOS, you have to upgrade openssl version
# http://stackoverflow.com/questions/18752409/updating-openssl-in-python-2-7

from hyper import HTTPConnection
import re

response_format = '{0:23} {1:3} {2}'

def get_favicon_url(country):
    return 'static-' + country +'.zacdn.com:443'

countries = ['hk', 'id', 'my', 'ph', 'sg', 'th', 'tw', 'vn']

urls = ['dynamic.zacdn.com:443']
for country in countries:
    urls.append(get_favicon_url(country))

for url in urls:
    connection = HTTPConnection(url)
    uri = '/images/favicon.png' if 'dynamic' not in url else '/85QZRTbD9wWnOgwv9jg-XG3npz0=/fit-in/236x345/filters:quality(95):fill(ffffff)/http://static.sg.zalora.net/p/zalora-3327-380904-1.jpg'

    try:
        connection.request('GET', uri)
        response = connection.get_response()
        print response_format.format(url, response.status, 'passed' if response.status == 200 else 'failed')
        response.close()
    except:
        print response_format.format(url, 'N/A', 'failed')


