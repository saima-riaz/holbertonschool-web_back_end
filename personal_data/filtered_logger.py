#!/usr/bin/env python3
""" Regex-ing """

import re
import logging
from typing import List

def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns a log message obfuscated."""
    for f in fields:
        message = re.sub(f'{f}=[^{separator}]*', f'{f}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to obfuscate"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record and obfuscate sensitive fields"""
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)