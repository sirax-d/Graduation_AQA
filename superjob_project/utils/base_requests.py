import logging
import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import os
from dotenv import load_dotenv
from superjob_project.utils.logging_helper import logging_helper

load_dotenv()
email = os.getenv("EMAIL")


headers = {'X-Api-App-Id': 'v3.r.138210493.f6e873d40874c1d142ee4668617d9d28d08dd341.8e80b7d7318c5e78944f081e8eb768ac904c3c03'}
def get_request(url, period, keyword, **kwargs):
    params = {'period': period, 'keyword': keyword}
    base_url = "https://api.superjob.ru/2.0/"
    with step(f"GET {url}"):
        response = requests.get(base_url + url, params=params,headers=headers, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        logging_helper(response)
    return response

def post_request(url, **kwargs):
    params = {'email': email}
    base_url = "https://api.superjob.ru/2.0/"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, headers=headers, params=params,  **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        logging_helper(response)
    return response

def put_request(url, **kwargs):
    params = {'access_token': 'v3.r.138210493.8fd8f7cf8e6496f2e161e0e062f6968c1c1c2687.9edac1756ea0f0b7ce6e669ba4c312c5638bed4e',\
              'code': 'ba257f7eeb5a31a6b147061d2965e72a06878ce5e3f5d1c9c5caae673bfa524c.f44ef4096f2937a32a006e071f15ac25d141f878',\
              'redirect_uri': 'https://example.com', 'client_id': '3392',
              'client_secret': 'v3.r.138210493.f6e873d40874c1d142ee4668617d9d28d08dd341.8e80b7d7318c5e78944f081e8eb768ac904c3c03'}
    base_url = "https://api.superjob.ru/2.0/"
    with step(f"PUT {url}"):
        response = requests.put(base_url + url, params=params, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        logging_helper(response)
    return response

def delete_request(url, **kwargs):
    base_url = "https://api.superjob.ru/2.0/"
    with step(f"DELETE {url}"):
        response = requests.delete(base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        logging_helper(response)
    return response
