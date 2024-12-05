import time
import logging
import schedule

from dotenv import load_dotenv
import os

from facebook_service import fetch_facebook_condo
from ddproperty_service import fetch_ddproperty_condo
from living_insider_service import fetch_living_insider_condo

load_dotenv()
condo_service_url = os.getenv("CONDO_SERVICE_URL")
data_provider = os.getenv("DATA_PROVIDER")
fetching_interval_second = os.getenv("FETCHING_INTERVAL_SECOND")


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)
def fetch():
    if data_provider == 'facebook':
        fetch_facebook_condo()
    elif data_provider == 'living_insider':
        fetch_living_insider_condo()
    elif data_provider == 'ddproperty':
        fetch_ddproperty_condo()


schedule.every(int(fetching_interval_second)).seconds.do(fetch)
logger.info('Start schedule fetching at with interval:"' + fetching_interval_second + '" seconds')
logger.info('Start schedule fetching at with data_provider:"' + data_provider + '"')
while True:
    schedule.run_pending()
    time.sleep(1)
