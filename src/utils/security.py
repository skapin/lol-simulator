from passlib.hash import pbkdf2_sha256

"""
    Utilities function for psw/token generation. fuck yeah love cosmic algo
"""
# def hash_password(password):
#     return pbkdf2_sha256.encrypt(password, rounds=1000000, salt_size=16)

# def verify_password(xhash, password):
#     return pbkdf2_sha256.verify(password, xhash)


def hash_password(password):
    return pbkdf2_sha256.encrypt(password, rounds=1000000, salt_size=16)


def verify_password(xhash, password):
    return pbkdf2_sha256.verify(password, xhash)


ALLOWED_EXT = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename, allowed_extensions=None):
    ext = allowed_extensions if allowed_extensions else ALLOWED_EXT
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ext
