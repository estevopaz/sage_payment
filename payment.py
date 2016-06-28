'''
Sage payment helper.
'''

import base64
import json
import requests


CREDENTIALS = 'IntegrationKey:IntegrationPassword'
VENDOR_NAME = 'VendorName'

CREDENTIALS_b46 = base64.b64encode(CREDENTIALS.encode('ascii'))
URL = 'https://test.sagepay.com/api/v1/merchant-session-keys'


def get_merchant_session_key():
    '''
    Request merchantSessionKey for Sage authentication.
    '''

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Basic {}'.format(CREDENTIALS_b46.decode('ascii'))
    }
    data = {
        'vendorName': VENDOR_NAME
    }

    res = requests.post(URL, headers=headers, data=json.dumps(data))

    return res.json()
