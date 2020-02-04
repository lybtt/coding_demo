import time

import six
from werkzeug.exceptions import Unauthorized

from jose import JWTError, jwt

JWT_ISSUER = 'com.github'
JWT_SECRET = 'your_secret_key'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def login(body):
    username = body['username']
    password = body['password']
    # 此处可以数据库获取用户
    if username == 'username' and password == 'password':
        timestamp = _current_timestamp()
        payload = {
            "iss": JWT_ISSUER,
            "iat": int(timestamp),
            "exp": int(timestamp + JWT_LIFETIME_SECONDS),
            "sub": str(username),
        }
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    else:
        return "login failed", 401


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def get_secret(user, token_info) -> str:
    return '''
    You are user {user}.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())