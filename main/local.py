import os

from constanta import UPLOAD_FOLDER


def upload(request):
    f = request.files['file']
    folder = request.form['folder']
    path = '{}/{}'.format(UPLOAD_FOLDER, folder)

    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    f.save(os.path.join(UPLOAD_FOLDER, folder, f.filename))
    return {'upload': 'OK'}


def delete(request):
    temp = request.form['path']
    path = '{}/{}'.format(UPLOAD_FOLDER, temp)

    try:
        os.remove(path)
    except FileNotFoundError:
        pass

    return {'status': 'OK'}
