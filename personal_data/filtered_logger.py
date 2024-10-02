#!/usr/bin/env python3
""" Regex-ing """


import re


def filter_datum(fields, redaction, message, separator):
    """Returns a log message obfuscated."""
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]*', f'{field}={redaction}', message)
    return message
