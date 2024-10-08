#!/usr/bin/env python3
""" Regex-ing """

from typing import List
import re
import logging
import os
import mysql.connector


# Define the PII fields tuple
PII_FIELDS = ("email", "ssn", "password", "address", "phone_number")


# Task 0. Regex-ing task

def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns a log message obfuscated."""
    for f in fields:
        message = re.sub(f'{f}=[^{separator}]*', f'{f}={redaction}', message)
    return message


# Task 1. Log formatter


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to obfuscate"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records using filter_datum"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)

# Task 2 Define the get_logger function


def get_logger() -> logging.Logger:
    """Returns a logger object configured for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


# Task 3  Connect to secure database


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Function that returns a connector to the database.
    """
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return connection








