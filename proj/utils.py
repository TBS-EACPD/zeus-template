import secrets
import string


def generate_password():
    alphabet = string.ascii_letters + string.digits + "-_"
    password = "".join(secrets.choice(alphabet) for i in range(16))
    return password
