from utils.exception import AuthenticationException, ServerErrorException

from dotenv import load_dotenv
import os
import requests
import logging

load_dotenv()
condo_service_url = os.getenv("CONDO_SERVICE_URL")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
headers = {"ClientId": client_id, "ClientSecret": client_secret}


def fetch_ddproperty_condo():
    logger.info('Fetch DDProperty condo')
    try:
        response = requests.get(condo_service_url + '/ddproperty/fetch', headers=headers)
        if response.status_code == 401:
            logger.error("401 Error from DDProperty")
            raise AuthenticationException
        elif response.status_code != 200:
            return ServerErrorException
    except requests.exceptions.RequestException as e:
        logger.error("500 Error from DDProperty")
        return ServerErrorException
    print('Fetch DDProperty condo done')
