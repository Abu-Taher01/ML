# ===================================================================================================
# Goal:      print func.__name__ of a decorated function.
# Deep Dive: It prints "wrapper", not the original name This confuses debuggers.
# Fix:       Use @functools.wraps(func) on the wrapper to copy the original metadata(name,docstring)
# to the new function.
# ===================================================================================================


# =====================================================================
#           without functool : func metadata is erased
# =====================================================================

def deco_no_func(func):
    def wrap():
        pass
    return wrap

@deco_no_func
def test_no_func():
    pass

print(test_no_func.__name__)


# =====================================================================
#                          with functool
# =====================================================================

from functools import wraps

def deco(func):
    @wraps(func)
    def wrap():
        pass
    return wrap

@deco
def test():
    pass

print(test.__name__)


# ======================================================================

import logging

# Configure logging to display messages
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_function_call(func):
    @wraps(func)  # for preserving function metadata
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(5, 10))