import os

from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.bucket(os.getenv('BUCKET_NAME'))


def upload(request):
    f = request.files['file']
    folder = request.form['folder']
    path = '{}/{}'.format(folder, f.filename)

    blob = bucket.blob(path)
    blob.upload_from_string(f.read())
    blob.make_public()

    return {'upload': 'OK'}


def delete(request):
    path = request.form['path']

    blob = bucket.blob(path)
    blob.delete()

    return {'status': 'OK'}
