import traceback

from flask import Flask, Response
from flask import request

import logger
from constanta import AUTH
from main import local as module

app = Flask(__name__)


def get_response(func, req):
    authorization = req.headers['Authorization']
    if authorization == AUTH:
        try:
            response = func(req)
        except Exception as e:
            logger.write(traceback.format_exc(), 'error')
            response = Response(str(e), status=500)
    else:
        message = 'Unauthorized'
        logger.write(message, 'warning')
        response = Response(message, status=401)

    return response


@app.route('/uploader/upload', methods=['POST'])
def api_upload():
    func = module.upload
    response = get_response(func, request)
    return response


@app.route('/uploader/delete', methods=['POST'])
def api_delete():
    func = module.delete
    response = get_response(func, request)
    return response


if __name__ == '__main__':
    app.run()
