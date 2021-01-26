import json
import logging
import os
import sys
from logging import handlers

from cryptography.fernet import Fernet

from constanta import ENCRYPT_KEY

log_format = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
log = logging.getLogger('default')
log.setLevel(logging.DEBUG)

docker = True if os.getenv('DOCKER') else False
cipher_suite = Fernet(ENCRYPT_KEY)

if os.getenv('FLASK_ENV') or docker:
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(log_format)
    log.addHandler(ch)
else:
    fh = handlers.RotatingFileHandler('info.log', maxBytes=(1048576 * 5), backupCount=7)
    fh.setFormatter(log_format)
    log.addHandler(fh)

log_dict = {
    'debug': log.debug,
    'info': log.info,
    'warning': log.warning,
    'error': log.error,
}


def write(message, log_type='debug'):
    if type(message) != str:
        message = json.dumps(message)
    if docker:
        message = cipher_suite.encrypt(message.encode())
    log_dict[log_type](message)
