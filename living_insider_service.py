import logging

from utils.exception import AuthenticationException, ServerErrorException

from dotenv import load_dotenv
import os
import requests

load_dotenv()
condo_service_url = os.getenv("CONDO_SERVICE_URL")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
headers = {"ClientId": client_id, "ClientSecret": client_secret}
def fetch_living_insider_condo():
    logger.info('Fetching living insider condo')
    try:
        response = requests.get(condo_service_url + '/living_insider/fetch', headers=headers)
        if response.status_code == 401:
            logger.error("401 Error from living insider")
            raise AuthenticationException
        elif response.status_code != 200:
            return ServerErrorException
    except requests.exceptions.RequestException as e:
        logger.error("500 Error from living insider")
        logger.error(e)
        return ServerErrorException
    logger.info('Fetch living insider condo done')
