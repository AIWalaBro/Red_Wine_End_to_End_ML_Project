import os
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logging_dir = "logs"
filename = os.path.join(logging_dir, "running_log.log")
os.makedirs(logging_dir, exist_ok = True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(filename),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("redwine_proj_logger")