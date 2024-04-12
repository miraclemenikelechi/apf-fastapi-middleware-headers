import logging
import os
import sys

log_file_path = os.path.join(os.getcwd(), "logs.txt")


if not os.path.exists(log_file_path):
    open(log_file_path, "x")


logger = logging.getLogger()
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(log_file_path)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]


logger.setLevel(logging.INFO)
