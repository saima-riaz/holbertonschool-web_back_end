#!/usr/bin/env python3
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Replaces sensitive information in a log message with redaction.

    Args:
        fields: A list of field names to obfuscate.
        redaction: The string to replace the field values with.
        message: The log message to be filtered.
        separator: The character separating fields in the log message.
    
    Returns:
        The filtered log message with obfuscated fields.
    """
    for f in fields:
        message = re.sub(f'{f}=[^ {separator}]*', f'{f}={redaction}', message)
    return message
