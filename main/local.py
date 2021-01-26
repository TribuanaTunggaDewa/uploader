import os
import shutil

from constanta import UPLOAD_FOLDER


def upload(request):
    # get data
    f = request.files['file']
    folder = request.form['folder']
    path = '{}/{}'.format(UPLOAD_FOLDER, folder)

    # upload file
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    f.save(os.path.join(UPLOAD_FOLDER, folder, f.filename))
    return {'upload': 'OK'}


def delete(request):
    # get data
    temp = request.form['path']
    path = '{}/{}'.format(UPLOAD_FOLDER, temp)

    # delete folder
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except PermissionError:
        shutil.rmtree(path)

    return {'status': 'OK'}
