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


def list_dir(request):
    folder = request.form['folder']

    data = []
    blobs = storage_client.list_blobs(bucket, prefix=folder, delimiter='/')
    for blob in blobs:
        if blob.name == folder:
            continue
        data.append(blob.name)

    return {'data': data}


def delete(request):
    path = request.form['path']

    blob = bucket.blob(path)
    blob.delete()

    return {'status': 'OK'}
