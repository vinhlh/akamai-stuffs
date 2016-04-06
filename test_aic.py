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
    return 'http://www.zalora.' + domain

def validate_image(image):
    response = requests.post(image, cookies = cookies, headers = headers)
    result = re.search('name=AIC_QUALITY; value=([0-9]+),', response.headers['X-Akamai-Session-Info'])
    if result:
        return result.group(1)
    return None

for domain in domains:
    response = requests.get(get_alice(domain))
    # src="http://zstaticvn02-a.akamaihd.net/cms/images/120K.jpg"
    image_result = re.search('="(http://zstatic[a-z]{2}[0-9]{2}-a.akamaihd.net/[^\"]+.jpg)"', response.text)
    if image_result:
        image_quality = validate_image(image_result.group(1))
        # print domain, image_quality, 'Passed' if image_quality == '60' else 'Failed'
        print "{0:10} {1:5}  {2}".format(domain, image_quality, 'Passed' if image_quality == '60' else 'Failed')
    else:
        print "{0:10} error".format(domain)


