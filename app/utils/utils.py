import uuid
import config

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])
def uuid4Str():
    test = str(uuid.uuid4())
    return test

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS