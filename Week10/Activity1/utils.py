import secrets
from datetime import datetime, timedelta

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


def validate_input(value):
    return value is not None and value.strip() != ""


def hash_password(password):
    return generate_password_hash(password)


def verify_password(hash_value, password):
    return check_password_hash(hash_value, password)


def gen_reset_token():
    token = secrets.token_urlsafe(32)

    expires = datetime.now() + timedelta(hours=1)

    return token, expires


def send_email(email, token):
    # 实际项目可以使用 SMTP / SendGrid
    print()
    print("==== SEND EMAIL ====")
    print("To:", email)
    print(f"Reset link:")
    print(f"http://localhost:5000/reset-password/{token}")
    print("====================")