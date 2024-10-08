#!/usr/bin/env python3
"""
Hashes a password using bcrypt."""

import bcrypt


def hash_password(password: str) -> bytes:
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# task 6 

def is_valid(hashed_password: bytes, password:str) -> bool:
    """check that provided pw matches the hashed pw"""
    return bcrypt.checkpw(password.encode(), hashed_password)


