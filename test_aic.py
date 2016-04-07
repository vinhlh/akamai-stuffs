import requests
import re

domains = [
    'com.hk',
    'co.id',
    'com.my',
    'com.ph',
    'sg',
    'co.th',
    'com.tw',
    'vn'
]

cookies = {
    'aic-rtt': '500'
}

headers = {
    'Pragma': 'akamai-x-get-extracted-values'
}

def get_alice(domain):
    return 'http://www.zalora.' + domain + '/all-products/'

def validate_image(image):
    response = requests.post(image, cookies = cookies, headers = headers)
    result = re.search('name=AIC_QUALITY; value=([0-9]+),', response.headers['X-Akamai-Session-Info'])
    if result:
        return result.group(1)
    return None

def validate(image_url_pattern, type):
    image_result = re.search(image_url_pattern, response.text)
    if image_result:
        image_quality = validate_image(image_result.group(1))
        print "{0:10} {1:10} {2:5}  {3}".format(domain, type, image_quality, 'Passed' if image_quality == '60' else 'Failed')
    else:
        print "{0:10} {1:10} error".format(domain, type)


for domain in domains:
    response = requests.get(get_alice(domain))

    validate('="(http://zstatic[a-z]{2}[0-9]{2}-a.akamaihd.net/[^\"]+.jpg)"', 'static')
    validate('"(http://n[1-2]{1}-zthumbor-a.akamaihd.net/[^\"]+.jpg)"', 'thumbor')


