import logging

from utils.exception import AuthenticationException, ServerErrorException

from dotenv import load_dotenv
import os
import requests

load_dotenv()
condo_service_url = os.getenv("CONDO_SERVICE_URL")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
headers = {"ClientId": client_id, "ClientSecret": client_secret}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)
def fetch_facebook_condo():
    logger.info('Fetching facebook condo')
    try:
        response = requests.get(condo_service_url + '/facebook/fetch', headers=headers)
        if response.status_code == 401:
            logger.error("401 Error from facebook")
            raise AuthenticationException
        elif response.status_code != 200:
            return ServerErrorException
    except requests.exceptions.RequestException as e:
        logger.error("500 Error from facebook")
        return ServerErrorException
    logger.info('Fetching facebook condo done')
