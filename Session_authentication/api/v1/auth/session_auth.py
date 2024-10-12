#!/usr/bin/env python3
""" SessionAuth module
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class
    """
    # Class attribute to store user_id by session_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for the
        user_id and store it in user_id_by_session_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique session ID
        session_id = str(uuid.uuid4())

        # Store the session_id with the associated user_id
        self.user_id_by_session_id[session_id] = user_id

        # Return the session_id
        return session_id
