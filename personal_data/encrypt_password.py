#!/usr/bin/env python3
"""
Hashes a password using bcrypt."""

import bcrypt


def hash_password(password: str) -> bytes:
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
