
import logging
import sys

logger = logging.getLogger('stripe')

__all__ = ['utf8']


def utf8(value):
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return value.encode('utf-8')
    return value
