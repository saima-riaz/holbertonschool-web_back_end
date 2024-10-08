#!/usr/bin/env python3
"""
Hashes a password using bcrypt."""

import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes a password with a new salt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())



