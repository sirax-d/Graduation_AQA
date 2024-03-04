import logging
import allure
from allure_commons.types import AttachmentType
import curlify


def logging_helper(response):
    curl = curlify.to_curl(response.request)
    logging.info(curlify.to_curl(response.request))
    logging.info(response.request.url)
    logging.info(response.status_code)
    logging.info(response.text)
    allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
