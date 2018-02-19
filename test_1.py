import requests
import json
import pytest
import io
import os
from requests.auth import HTTPBasicAuth


class HttpBin:

    def __init__(self):
        self.host = 'https://httpbin.org'

    def get_request(self, arg, value):
        response = requests.get("%s/get?%s=%s" % (self.host, arg, value))
        return response

    def stream_request(self, number_of_lines):
        response = requests.get("%s/stream/%s" % (self.host, str(number_of_lines)))
        return response

    def auth(self, username, password, username_url, password_url):
        response = requests.get("%s/basic-auth/%s/%s" % (self.host, username_url, password_url),
                                auth=HTTPBasicAuth(username, password))
        return response.status_code

    def post_string(self, arg, value):
        response = requests.post("%s/post?%s=%s" % (self.host, arg, value))
        return response

    def post_form_data(self, key, value):
        response = requests.post("%s/post" % self.host, data={key: value})
        return response

    def post_data(self, key, value):
        response = requests.post("%s/post" % self.host, data=key + value)
        return response

    def post_data_dumps(self, key, value):
        data = {key: value}
        response = requests.post("%s/post" % self.host, json.dumps(data))
        return response


test = HttpBin()

class TestHttpBinTests():

    def test_get_request(self):
        response = test.get_request('Name', 'Alesya')
        assert response.json()['args'] == {'Name': 'Alesya'}
        assert response.status_code == 200
	
    @pytest.mark.parametrize("number_of_lines, expected_count", [
            (50, 50),
            (120, 120)
    ])
    def test_stream_request_less_then_100(self, number_of_lines, expected_count):
        response = test.stream_request(number_of_lines)
        temp_file = '.\\temp.json'
        with open(temp_file, "w") as f:
            f.write(str(response.text))
        f.close()
        word = u'id'
        count = 0
        with io.open(temp_file, encoding='utf-8') as f:
            for line in f:
                if word in line:
                    count = count + 1
        f.close()
        os.remove(temp_file)
        assert response.status_code == 200
        assert count == expected_count

    @pytest.mark.parametrize("username, password, username_url, password_url, status_code", [
            ('user', 'passwd', 'user', 'passwd', 200), 
            ('users', 'passwd', 'user', 'passwd', 401)
 	])
    def test_auth(self, username, password, username_url, password_url, status_code):
        assert test.auth(username, password, username_url, password_url) == status_code


    def test_post_string(self):
        response = test.post_string('key', 'value')
        assert response.json()['args'] == {'key': 'value'}
        assert response.status_code == 200

    def test_post_form_data(self):
        response = test.post_form_data('key', 'value')
        assert response.json()['form'] == {'key': 'value'}
        assert response.status_code == 200

    def test_post_data(self):
        response = test.post_data('key', 'value')
        assert response.json()['data'] == 'keyvalue'
        assert response.status_code == 200

    def test_post_data_dumps(self):
        response = test.post_data_dumps('key', 'value')
        assert response.json()['data'] == '{"key": "value"}'
        assert response.json()['json'] == {"key": "value"}
        assert response.status_code == 200