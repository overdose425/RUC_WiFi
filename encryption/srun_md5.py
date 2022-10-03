import hmac
import hashlib


def get_md5(password, token):
    return hmac.new(token.encode(), password.encode(), hashlib.md5).hexdigest()


if __name__ == '__main__':
    password = "1234567"
    token = "1234567"
    print(get_md5(password, token))
