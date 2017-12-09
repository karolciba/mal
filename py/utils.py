import sys

DEBUG = True
DEBUG = False

def debug(*args):
    DEBUG and print(*args, file=sys.stderr)
