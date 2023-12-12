# import bcrypt

# def hash_password(password: str):
#     return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# def verify_password(stored_password_hash: bytes, provided_password: str):
#     return bcrypt.checkpw(provided_password.encode(), stored_password_hash)

import bcrypt

# Hardcoded hashed password for the username 'user'
hashed_password_demo = bcrypt.hashpw(b'password', bcrypt.gensalt())  # Hash for 'password'

def verify_password(provided_password: str):
    # Verifying the provided password against the hardcoded hashed password
    return bcrypt.checkpw(provided_password.encode(), hashed_password_demo)