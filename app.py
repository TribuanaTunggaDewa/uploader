import os
import traceback

from dotenv import load_dotenv
from flask import Flask, Response
from flask import request

import logger
from constanta import AUTH

load_dotenv('.env')
bucket_name = os.getenv('BUCKET_NAME')

if bucket_name:
    logger.write('File will be saved to {} bucket'.format(bucket_name))
    from main import google_cloud as module
else:
    logger.write('File will be saved to local')
    from main import local as module

app = Flask(__name__)


def get_response(func, req):
    authorization = req.headers['Authorization']
    if authorization == AUTH:
        try:
            response = func(req)
        except Exception as e:
            logger.write(str(traceback.format_exc().encode()), 'error')
            response = Response(str(e), status=500)
    else:
        message = 'Unauthorized'
        logger.write(message, 'warning')
        response = Response(message, status=401)

    return response


@app.route('/', methods=['GET'])
def api_root():
    return 'OK'


@app.route('/uploader/', methods=['GET'])
def api_health():
    return 'Uploader is running...'


@app.route('/uploader/upload', methods=['POST'])
def api_upload():
    func = module.upload
    response = get_response(func, request)
    return response


@app.route('/uploader/list', methods=['POST'])
def api_list():
    func = module.list_dir
    response = get_response(func, request)
    return response


@app.route('/uploader/delete', methods=['POST'])
def api_delete():
    func = module.delete
    response = get_response(func, request)
    return response


if __name__ == '__main__':
    app.run()
