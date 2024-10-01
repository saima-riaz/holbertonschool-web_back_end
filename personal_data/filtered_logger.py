#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """
     Replaces the values of specified fields in a log message with a redaction string.
    """
    for field in fields:
        message = re.sub(
            f'{field}=[^ {separator}]+', f'{field}={redaction}', message
        )
    return message
