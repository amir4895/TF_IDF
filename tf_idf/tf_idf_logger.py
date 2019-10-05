import logging
import time
import datetime
from os import path, mkdir


PROG_NAME = "TF_IDF"
LOG_PATH = path.expanduser("~/TF_IDF_LOGS")


ts = time.time()
time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
if not path.exists(LOG_PATH):
    mkdir(LOG_PATH)

log_path = path.join(LOG_PATH, time_stamp)
logging.basicConfig(filename=log_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.info("Running TF IDF")

LOG = logging.getLogger(PROG_NAME)
LOG.setLevel(logging.DEBUG)
