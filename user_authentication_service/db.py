#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

# task 2
    def add_user(self, email: str, hashed_password: str) -> User:
        """Add and save a user to the database."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

# task 3

    def find_user_by(self, **kwargs) -> User:
        """Arbitrary keyword arguments return first row of user."""
        try:
            result = self._session.query(User).filter_by(**kwargs).first()

            if result is None:
                raise NoResultFound("No user found.")

            return result  # Moved outside the if block
        except NoResultFound:
            raise NoResultFound("No user found.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query parameters.")
