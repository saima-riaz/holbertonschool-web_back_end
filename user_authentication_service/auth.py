#!/usr/bin/env python3
"""Auth module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if they don't already exist."""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates if a given email and
        password correspond to a valid user."""
        try:
            user = self._db.find_user_by(email=email)

            # Ensure user exists and hashed_password is available
            if user and hasattr(user, 'hashed_password'):
                # Compare the provided password with the stored hashed password
                if bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password
                ):
                    return True

            return False

        except NoResultFound:
            return False
    
    def _generate_uuid(self) -> str:
        """ Generates a new UUID and returns its string representation.
        """
        return str(uuid.uuid4())
