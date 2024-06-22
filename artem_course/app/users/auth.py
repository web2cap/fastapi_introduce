import bcrypt


def hash_password(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password=pwd_bytes, salt=salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password_byte_enc = plain_password.encode("utf-8")
    hashed_password_byte_enc = hashed_password.encode("utf-8")

    return bcrypt.checkpw(
        password=plain_password_byte_enc, hashed_password=hashed_password_byte_enc
    )
