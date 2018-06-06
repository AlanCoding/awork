# Copyright 2015, Ansible, Inc.
# Luke Sneeringer <lsneeringer@ansible.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools
import warnings
import json

from requests.sessions import Session
from requests.auth import AuthBase, HTTPBasicAuth
from requests.packages import urllib3

from awork.conf import settings


class TokenAuth(AuthBase):

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer {}'.format(settings.oauth_token)
        return r


class Client(Session):

    @functools.wraps(Session.request)
    def request(self, method, url, *args, **kwargs):
        kwargs.setdefault(
            'auth',
            (
                TokenAuth() if settings.oauth_token else
                HTTPBasicAuth(self.username, self.password)
            )
        )

        headers = kwargs.get('headers', {})
        kwargs['headers'] = headers

        headers.setdefault('Content-Type', 'application/json')

        # If this is a JSON request, encode the data value.
        if headers.get('Content-Type', '') == 'application/json':
            kwargs['data'] = json.dumps(kwargs.get('data', {}))

        verify_ssl = True
        if (settings.verify_ssl is False) or hasattr(settings, 'insecure'):
            verify_ssl = False

        host = settings.host.strip('/')
        address = url.strip('/')
        if not address.startswith('api'):
            address = '/'.join(['api', 'v2', address])
        url = '/'.join([host, address])

        with warnings.catch_warnings():
            warnings.simplefilter(
                "ignore", urllib3.exceptions.InsecureRequestWarning)
            return super(Client, self).request(
                method, url, *args, verify=verify_ssl, **kwargs)


client = Client()
