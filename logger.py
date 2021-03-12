import json
import logging
import sys

log_format = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
log = logging.getLogger('default')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(log_format)
log.addHandler(ch)

log_dict = {
    'debug': log.debug,
    'info': log.info,
    'warning': log.warning,
    'error': log.error,
}


def write(message, log_type='debug'):
    if type(message) != str:
        message = json.dumps(message)
    log_dict[log_type](message)
